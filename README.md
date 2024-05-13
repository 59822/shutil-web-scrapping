# Web Scrapping
# Shutil: Librería de Manipulación de Archivos y Directorios en Python

La librería `shutil` de Python proporciona una variedad de operaciones de alto nivel para manipular archivos y directorios de manera eficiente. Esta guía de referencia rápida describe las principales funciones de `shutil` junto con ejemplos de uso.

## Copiar archivos y directorios

### `shutil.copy()`

Copia un archivo desde una ruta de origen a una ruta de destino.

```python
import shutil

# Copiar un archivo
shutil.copy('archivo_origen.txt', 'ruta/destino/archivo_destino.txt')
```

### `shutil.copytree()`
Copia un directorio completo, incluyendo todos sus archivos y subdirectorios.

``` python
import shutil

# Copiar un directorio completo
shutil.copytree('directorio_origen', 'ruta/destino/directorio_destino')


```
## Mover archivos y directorios
### `shutil.move()`
Mueve un archivo o directorio desde una ubicación de origen a una ubicación de destino.

```python
import shutil

# Mover un archivo o directorio
shutil.move('ruta/origen/archivo_o_directorio', 'ruta/destino/')

```
## Eliminar archivos y directorios
### `shutil.rmtree()`
Elimina un directorio y todo su contenido de forma recursiva.

```python
import shutil

# Eliminar un directorio y su contenido
shutil.rmtree('directorio_a_eliminar')

```

## Archivos temporales
### `shutil.tempfile`
Proporciona funciones para trabajar con archivos temporales.

```python
import shutil

# Crear un archivo temporal
with tempfile.NamedTemporaryFile() as temp:
    temp.write(b'Contenido del archivo temporal')
    print(temp.name)

```

## Archivos y dearchivar archivos
### `shutil.make_archive()`
Crea archivos de formato común (como ZIP o TAR) a partir de un directorio.
``` python
 import shutil

# Crear un archivo ZIP a partir de un directorio
shutil.make_archive('archivo_comprimido', 'zip', 'directorio_a_comprimir')

```
### `shutil.unpack_archive()`
Descomprime archivos en un directorio especificado.
```python

import shutil

# Descomprimir un archivo ZIP en un directorio
shutil.unpack_archive('archivo.zip', 'directorio_destino')
```
## Comprobar si un archivo o directorio existe
### `shutil.exists()`
Comprueba si un archivo o directorio existe en la ruta especificada.

```python
import shutil

# Comprobar si un archivo o directorio existe
if shutil.exists('archivo_o_directorio'):
    print('El archivo o directorio existe.')
else:
    print('El archivo o directorio no existe.')

```

# EJERCICIOS
### 1. Copiar archivos de un directorio a otro:
```PYTHON
import shutil
import os

def copiar_archivos(ruta1, ruta_final):
    if not os.path.exists(ruta_final):
        os.makedirs(ruta_final)
    
    archivos = os.listdir(ruta1)
    
    for i in archivos:
        ruta_vieja = os.path.join(ruta1, i)
        ruta_nueva = os.path.join(ruta_final, i)
        shutil.copy(ruta_vieja, ruta_nueva)
        print(f"Se ha copiado el archivo {i} a la ruta {ruta_final}")
        
ruta1 = "D:\Downloads\helloo"
ruta_final = "D:\Downloads\helloo2"

copiar_archivos(ruta1, ruta_final)
```
### 2. Mover archivos de un directorio a otro:

``` python 
import os
import shutil

def mover(ruta1, ruta2):
    if not os.path.exists(ruta2):
        os.makedirs(ruta2)
    
    archivos = os.listdir(ruta1)
    
    for i in archivos:
        ruta_vieja = os.path.join(ruta1, i)
        ruta_nueva = os.path.join(ruta2, i)
        shutil.move(ruta_vieja, ruta_nueva)
        print(f"Se ha movido el archivo {i} a la ruta {ruta2}")

ruta1 = "D:\Downloads\helloo"
ruta2 = "D:\Downloads\helloo2"
objeto = mover(ruta1, ruta2)
print(objeto)
```

### 3. Crear una copia de seguridad de un directorio:
```python 
import os
import shutil

def segurity(ruta1, ruta2):
    shutil.copytree(ruta1, ruta2)
    print(f"Se ha creado una copia de seguridad en la ruta {ruta2}")

ruta1 = "D:\Downloads\helloo2"
ruta2 = "D:\Downloads\helloo3"
objeto = segurity(ruta1, ruta2)
print(objeto)

```

### 4. Eliminar un directorio y su contenido
```python
import shutil

# Eliminar un directorio y su contenido
shutil.rmtree("D:\Downloads\helloo2")
```