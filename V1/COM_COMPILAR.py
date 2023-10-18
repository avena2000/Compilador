import subprocess
import time

# Lista de nombres de archivos que deseas ejecutar en orden
archivos_a_ejecutar = [
    "COM_FORMATEADOR.py",
    "COM_SIMBOLOS.py",
    "COM_CONTADOR.py",
    "COM_DATOS.py",
    "COM_NUMEROS.py",
    "COM_FORMATDATOS.py",
    "COM_ERRORES.py",
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

        # Espera un segundo antes de ejecutar el siguiente archivo
        time.sleep(0)

    except Exception as e:
        print(f"Error al ejecutar {archivo}: {e}")
