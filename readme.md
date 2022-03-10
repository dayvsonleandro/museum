# Museum


### Diretórios base para utilização do Jackal

Após clonar os repositórios certifique-se de mudar para a branch correta, quando não existir a branch "noetic" use a branch "melodic" essa orientação é válida para os repositórios da clearpath.

```
cd catkin_ws/src
git clone https://github.com/jackal/jackal.git
git clone https://github.com/clearpathrobotics/LMS1xx.git
git clone https://github.com/jackal/jackal_simulator.git
```

Instalar dependências
```
$rosdep install --from-paths src --ignore-src -r -y
```

### Referencias

- [Clearpath](https://www.clearpathrobotics.com/assets/guides/noetic/jackal/simulation.html0)