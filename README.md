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


Código adicional para el estudio de Kp (Control Proporcional)

## Para seleccionar de manera sistemática los valores adecuados de ganancia proporcional (Kp), se implementó código adicional con fines exclusivamente experimentales.

Este código fue utilizado únicamente para analizar cinco configuraciones diferentes de Kp en el controlador P. No fue utilizado para el ajuste de PD, PI ni PID.

El objetivo fue:
- Evaluar el efecto del aumento de Kp en la respuesta del sistema
- Comparar velocidad de respuesta entre configuraciones
- Analizar tendencia a la oscilación
- Seleccionar un valor base de Kp estable y adecuado

Una vez seleccionado el mejor conjunto de Kp, este código experimental dejó de utilizarse.

Cómo ejecutar el estudio de Kp (VS Code)
## 1. Abrir el proyecto

File → Open Folder → selecciona la carpeta del proyecto.

## 2. Crear entorno virtual

Abrir terminal en VS Code:

Terminal → New Terminal

Ejecutar:

python -m venv .venv

## 3. Activar el entorno

En Windows:

.venv\Scripts\activate


En Linux / Mac:

source .venv/bin/activate

## 4. Seleccionar el intérprete

Ctrl + Shift + P

→ Python: Select Interpreter
→ selecciona .venv

## 5. Instalar dependencias
pip install -U pip
pip install mujoco numpy scipy pandas matplotlib dash plotly

## 6. Ejecutar el estudio de Kp
python run_kp_study.py


Este script:

Ejecuta la trayectoria requerida:

1. posición inicial → cero

2. mantener

3. regresar a posición inicial

4. mantener nuevamente

Aplica perturbaciones durante todo el movimiento

Evalúa cinco configuraciones distintas de Kp

Genera gráficas comparativas

## 7. Resultados
Las gráficas generadas se almacenan en:
results/P_kp_study/
Se crea una gráfica por cada articulación, donde se muestran las cinco configuraciones de Kp superpuestas.
Estas gráficas fueron utilizadas únicamente para seleccionar el valor final de Kp.

# Filosofía de selección de ganancias
- Se asignaron valores de Kp independientes por articulación.
-Las articulaciones proximales (hombro) utilizan mayores ganancias que las distales (muñeca).
- Se evaluaron cinco configuraciones.
- La selección final se basó en estabilidad, velocidad de respuesta y robustez ante perturbaciones.

