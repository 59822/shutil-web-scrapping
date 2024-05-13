#Copiar archivos de un directorio a otro:

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