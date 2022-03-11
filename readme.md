# Museum

## Preparando o ambiente

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
- [ ] Simulação de uma visita autônoma por um robô autônomo em simulação;
- [ ] Navegação e desvio de obstáculos pelo robô em simulação;
- [ ] Apresentação das obras.
