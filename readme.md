# Museum

## Preparando o ambiente

### Baixar e compilar o ambiente
Clone po repositorio do github em um ambiente catkin:


``` shell
cd catkin_ws/src
git clone https://github.com/dayvsonleandro/museum.git
```

Para a primeira compilação:
```
cd catkin_ws
source /opt/ros/noetic/setup.bash
catkin_make
```

Para compilar o ambiente apos edições:
```
cd catkin_ws
source devel/setup.bash
catkin_make
```


### Executar simulação do museu

``` shell
cd catkin_ws
source devel/setup.bash
roslaunch museum museum.launch
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

### Referências

- [Clearpath](https://www.clearpathrobotics.com/assets/guides/noetic/jackal/simulation.html0)
- [aws-robomaker-bookstore-world](https://github.com/aws-robotics/aws-robomaker-bookstore-world)

### Atividades

- [ ] Criação de uma simulação “mundo” de um museu;
- [ ] Simulação de uma visita autônoma por um robô autônomo em simulação;(codigo python)
- [x] Navegação e desvio de obstáculos pelo robô em simulação;
- [ ] Apresentação das obras.(codigo python)


### Editando o museu (Não funcionou, não carrega os objetos do diretorio model)

```
cd catkin_ws/src/museum
gazebo worlds/bookstore.world
```

### Mapeando um ambiente no gazebo

```
cd catkin_ws
source devel/setup.bash
roslaunch museum mapping_gazebo.launch
```

Salvando o mapa do ambiente

```
cd catkin_ws/src
source devel/setup.bash
rosrun map_server map_saver -f bookstore_clean
```