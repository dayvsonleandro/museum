# Museum

## Preparando o ambiente

### Baixar e compilar o ambiente
Clone po repositorio do github em um ambiente catkin:


``` shell
cd catkin_ws/src
git clone https://github.com/dayvsonleandro/museum.git
```

Para a primeira compilação:
``` shell
cd catkin_ws
source /opt/ros/noetic/setup.bash
catkin_make
```

Para compilar o ambiente apos edições:
``` shell
cd catkin_ws
source devel/setup.bash
catkin_make
```
### Diretórios base para utilização do Jackal

Após clonar os repositórios certifique-se de mudar para a branch correta, quando não existir a branch "noetic" use a branch "melodic" essa orientação é válida para os repositórios da clearpath.

``` shell
cd catkin_ws/src
git clone https://github.com/jackal/jackal.git
git clone https://github.com/clearpathrobotics/LMS1xx.git
git clone https://github.com/jackal/jackal_simulator.git
```

Instalar dependências

``` shell
$rosdep install --from-paths src --ignore-src -r -y
```

## Utilizando o pacote


### Executar simulação do museu

``` shell
cd catkin_ws
source devel/setup.bash
roslaunch museum museum.launch
```

### Mapeando um ambiente no gazebo

``` shell
cd catkin_ws
source devel/setup.bash
roslaunch museum mapping_gazebo.launch
```

Salvando o mapa do ambiente
``` shell
cd catkin_ws/src
source devel/setup.bash
rosrun map_server map_saver -f bookstore
```


### Editando o museu (Não funcionou, não carrega os objetos do diretorio model)

``` shell
cd catkin_ws/src/museum/museum
gazebo worlds/bookstore_clean.world
```

### Referências

- [Clearpath](https://www.clearpathrobotics.com/assets/guides/noetic/jackal/simulation.html0)
- [Husky](https://github.com/husky/husky.git)
- [aws-robomaker-bookstore-world](https://github.com/aws-robotics/aws-robomaker-bookstore-world)
- [python-sending-goals](https://answers.ros.org/question/80646/python-sending-goals-to-the-navigation-stack/)

### Atividades

- [ ] Criação de uma simulação “mundo” de um museu;
- [x] Simulação de uma visita autônoma por um robô autônomo em simulação;(codigo python)
- [x] Navegação e desvio de obstáculos pelo robô em simulação;
- [x] Apresentação das obras; (codigo python)
- [ ] Adicionar obstaculo movel.

### Desafios 

- O laser do robô não conseguiu identificar a presença do obstaculo movel do tipo "actor", após pesquisas foi identificado a nescessidade de alterar a tag do sensor no arquivo sick_lms1xx.urdf.xacro, conforme mostrado abaixo

de:
``` html
 <sensor type="ray" name="${frame}">
```
para:
``` html
 <sensor type="gpu_ray" name="${frame}">
```

Após a modificação a simulação passou a não funcionar, sendo o provavel motivo a incompatibilidade da placa de video do computador utilizado no desenvolvimento, sendo nescessario mais pesquisas para identificação e correção da causa raiz do problema.

OBS: Gazebo apresentou problema e foi nescessario desativar firewall
https://github.com/osrf/subt/issues/1033

### Informações sobre as obras apresentadas

- [MONA LISA – LEONARDO DA VINCI](https://arteeartistas.com.br/mona-lisa-leonardo-da-vinci/)
- [MULHER COM SOMBRINHA (O PASSEIO) – CLAUDE MONET](https://arteeartistas.com.br/mulher-com-sombrinha-o-passeio-claude-monet/)
- [O NASCIMENTO DE VÊNUS – SANDRO BOTTICELLI](https://arteeartistas.com.br/o-nascimento-de-venus-sandro-botticelli/)
- [NOITE ESTRELADA, A OBRA PRIMA DE VINCENT VAN GOGH](https://arteeartistas.com.br/noite-estrelada-a-obra-prima-de-vincent-van-gogh/)
- [A TRAIÇÃO DAS IMAGENS DE RENÉ MAGRITTE (ISTO NÃO É UM CACHIMBO)](https://arteeartistas.com.br/a-traicao-das-imagens-de-rene-magritte/)