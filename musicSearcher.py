import os
import shutil
""" 
Este script se encarga de, a partir de una carpeta "Madre", recorrer todas las subcarpetas existentes, para copiar y pegar todos los archivos musicales que encuentre
en su camino, en una carpeta llamada "Playlist", y disponer de todos los archivos en un unico repositorio.
"""
# Ruta de la carpeta madre
carpeta_madre = 'C:/Users/Estanislao/Documents/MusicApp' 

# Ruta de la carpeta destino
carpeta_destino = 'C:/Users/Estanislao/Music/Playlist' 

# Extensiones de archivo que queremos buscar
extensiones = ['.mp3', '.aiff', '.wav', '.flac']

# Función para copiar y pegar archivos
def copiar_archivos(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Copiando: {src} -> {dst}")
    except Exception as e:
        print(f"Error al copiar {src}: {e}")

# Recorre la carpeta madre y busca los archivos con las extensiones especificadas
for carpeta_actual, subcarpetas, archivos in os.walk(carpeta_madre):
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        if extension.lower() in extensiones:
            ruta_origen = os.path.join(carpeta_actual, archivo)
            ruta_destino = os.path.join(carpeta_destino, archivo)
            copiar_archivos(ruta_origen, ruta_destino)

print("Proceso completado.")
