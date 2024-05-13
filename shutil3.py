import os
import shutil

def segurity(ruta1, ruta2):
    shutil.copytree(ruta1, ruta2)
    print(f"Se ha creado una copia de seguridad en la ruta {ruta2}")

ruta1 = "D:\Downloads\helloo2"
ruta2 = "D:\Downloads\helloo3"
objeto = segurity(ruta1, ruta2)
print(objeto)