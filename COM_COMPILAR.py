import subprocess
import time

# Lista de nombres de archivos que deseas ejecutar en orden
archivos_a_ejecutar = [
    "COM_OPTIMIZAR.py",
    "COM_DECLARACIONES.py",
    "COM_SIMBOLOS.py",
    "COM_REMOVE_VAR.py",
    "COM_DICCIONARIO.py",
    "COM_DATOS.py",
    "COM_NUMEROS.py",
    "COM_ERRORES.py",
    "COM_TRIPLO.py"
]

# Itera sobre la lista y ejecuta cada archivo esperando a que termine

for archivo in archivos_a_ejecutar:
    comando = ["python", archivo]
    try:
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, errores = proceso.communicate()

        if proceso.returncode == 0:
            print(f"Ejecución de {archivo} exitosa.")
        else:
            print(f"Error al ejecutar {archivo}.")
            if salida:
                print("Salida:")
                print(salida.decode("utf-8"))
            if errores:
                print("Errores:")
                print(errores.decode("utf-8"))

    except Exception as e:
        print(f"Error al ejecutar {archivo}: {e}")
    # time.sleep(1)
