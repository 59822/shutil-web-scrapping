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

### `shutil.copytree()´
Copia un directorio completo, incluyendo todos sus archivos y subdirectorios.

``` python
import shutil

# Copiar un directorio completo
shutil.copytree('directorio_origen', 'ruta/destino/directorio_destino')


```
## Mover archivos y directorios
### `shutil.move()´
Mueve un archivo o directorio desde una ubicación de origen a una ubicación de destino.

```python
import shutil

# Mover un archivo o directorio
shutil.move('ruta/origen/archivo_o_directorio', 'ruta/destino/')

```
## Eliminar archivos y directorios
### `shutil.rmtree()´
Elimina un directorio y todo su contenido de forma recursiva.

```python
import shutil

# Eliminar un directorio y su contenido
shutil.rmtree('directorio_a_eliminar')

```

## Archivos temporales
### `shutil.tempfile´
Proporciona funciones para trabajar con archivos temporales.

```python
import shutil

# Crear un archivo temporal
with tempfile.NamedTemporaryFile() as temp:
    temp.write(b'Contenido del archivo temporal')
    print(temp.name)

```

## Archivos y dearchivar archivos
### `shutil.make_archive()´
Crea archivos de formato común (como ZIP o TAR) a partir de un directorio.
``` python
 import shutil

# Crear un archivo ZIP a partir de un directorio
shutil.make_archive('archivo_comprimido', 'zip', 'directorio_a_comprimir')

```
### `shutil.unpack_archive()´
Descomprime archivos en un directorio especificado.
```python

import shutil

# Descomprimir un archivo ZIP en un directorio
shutil.unpack_archive('archivo.zip', 'directorio_destino')
```
## Comprobar si un archivo o directorio existe
### `shutil.exists()´
Comprueba si un archivo o directorio existe en la ruta especificada.

```python
import shutil

# Comprobar si un archivo o directorio existe
if shutil.exists('archivo_o_directorio'):
    print('El archivo o directorio existe.')
else:
    print('El archivo o directorio no existe.')

```