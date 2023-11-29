# Nombre del archivo de entrada y salida
nombre_archivo_entrada = 'optimizacion/codigo_optimizado.txt'
nombre_archivo_salida = 'modificaciones/codigo_limpio.txt'

# Palabras clave que queremos buscar en las líneas
palabras_clave = ['|ENT|', '|REAL|', '|CAD|']

# Abrir el archivo de entrada en modo lectura
with open(nombre_archivo_entrada, 'r') as archivo_entrada:
    # Leer todas las líneas del archivo
    lineas = archivo_entrada.readlines()

# Filtrar las líneas eliminando aquellas que contienen las palabras clave
lineas_filtradas = [linea for linea in lineas if not any(palabra in linea for palabra in palabras_clave)]

# Abrir el archivo de salida en modo escritura y escribir las líneas filtradas
with open(nombre_archivo_salida, 'w') as archivo_salida:
    archivo_salida.writelines(lineas_filtradas)

print(f"Se han eliminado las líneas que contenían {', '.join(palabras_clave)} del archivo.")
