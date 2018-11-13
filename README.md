# SVG TO JSON #

Script for transform SVG files to JSON, it asign a unique ID for each path of canvas.
*Script que transforma los SVG a JSON, otorgandole ID a cada trazado.*

A unique Id Path, allow us identify specific elements, for example in a loop iteration.
*un unico id por forma nos permite identificar elementos especificos, por ejemplo dentro en un loop iteration.*


### Requisitos de archivo / Requeriments ###

- Crear archivo SVG en ilustrator o similar. *create SCG file in illustrator or similar*
- Abrir archivo en [Inkscape](https://inkscape.org/release), selecciona todo (crtl + a) y se convierten los trazados a path (Shift+Ctrl+C), guardar archivo. *Open File in [Inkscape](https://inkscape.org/release) , select All (crtl + a), and convert to paths (Shift+Ctrl+C).*
- Guardar archivo en carpeta del script y seguir instrucciones. *Save file in script folder and next with instructions*


## Instrucciones / Instructions:

```bash
$ git clone https://github.com/manucg7/py-svg-to-json.git
```

#### 1.2 - Instalar virtualenv (macOS con Homebrew)
*Solo si no lo tiene actualmente instalado sino saltar al paso 2:
*if you aldready installed it, follow with the step 2.

```bash
$ pip install virtualenv
```

#### 1.2 - Crear entorno virtual
```bash
$ virtualenv env --python=python3
```

#### 2 - Activar entorno virtual
```bash
$ source env/bin/activate
```
#### 3 - Iniciar Script
```
cd py-svg-to-json
python ./main.py

```
