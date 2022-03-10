# Museum

### Diretorios base para utilização do Jackal

- apos clonar os repositorios certifiquese de mudar para a branch correta, nos cassos onde não existir a branch "noetic" use a branche "melodic" essa orientação é valida para os repositorios da clearpath.

```
cd robos_autonomos_t2_ws/src
git clone https://github.com/jackal/jackal.git
```

```
cd robos_autonomos_t2_ws/src
git clone https://github.com/clearpathrobotics/LMS1xx.git
```

```
cd robos_autonomos_t2_ws/src
git clone https://github.com/jackal/jackal_simulator.git
```

```
https://github.com/ros-visualization/interactive_marker_twist_server.git
```
Instalar dependências
```
$rosdep install --from-paths src --ignore-src -r -y
```

### Referencias

- [Clearpath](https://www.clearpathrobotics.com/assets/guides/noetic/jackal/simulation.html0)