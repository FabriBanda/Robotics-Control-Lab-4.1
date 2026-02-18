# Robotics-Control-Lab-4.1
Robotics Control Lab 4.1 Equipo 2

# Simulación del Robot SO101 con MuJoCo

Este proyecto simula el brazo robótico SO101 usando MuJoCo y un controlador PID implementado en Python.  
El objetivo fue analizar el comportamiento del robot variando manualmente las ganancias del controlador.

---

Cómo ejecutar el proyecto (VS Code)

### 1. Abrir el proyecto
File → Open Folder → selecciona la carpeta del proyecto.

---

### 2. Crear entorno virtual
Abrir terminal en VS Code:

Terminal → New Terminal

Ejecutar:
python -m venv .venv

### 3. Activar el entorno
.venv\Scripts\activate

### 4. Seleccionar el intérprete
Ctrl + Shift + P

→ Python: Select Interpreter  
→ selecciona `.venv`


### 5. Instalar dependencias
pip install -U pip
pip install mujoco numpy scipy pandas matplotlib dash plotly

### 6. Ejecutar la simulación
python run_mujoco_simulation.py

Luego abrir:
http://127.0.0.1:8050 

##Qué hicimos en la práctica

Se evaluó el comportamiento del robot variando manualmente las ganancias del controlador.

Se probaron configuraciones:

- P
- PI
- PD
- PID

Las ganancias base se modificaron con multiplicadores (×0.25, ×0.5, ×1.5, ×2) para analizar:

- velocidad de respuesta
- sobrepaso
- oscilaciones
- error en estado estacionario
- estabilidad

Las ganancias se ajustaron directamente en:
so101_mujoco_pid_utils.py
