##Mover archivos de un directorio a otro:

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