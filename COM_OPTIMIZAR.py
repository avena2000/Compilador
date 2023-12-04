import shutil,  os

elementos_encontrados = []

contador_copia= 1

carpeta_a_borrar = 'optimizacion/'

try:
    archivos_en_carpeta = os.listdir(carpeta_a_borrar)
    
    for archivo in archivos_en_carpeta:
        ruta_completa = os.path.join(carpeta_a_borrar, archivo)
        os.remove(ruta_completa)
    
    print(f'Archivos en la carpeta {carpeta_a_borrar} han sido borrados exitosamente.')
except FileNotFoundError:
    print(f'La carpeta {carpeta_a_borrar} no fue encontrada.')
except Exception as e:
    print(f'Ocurrió un error al intentar borrar los archivos: {e}')


while True:
    if contador_copia == 1:
         # Genera un nuevo nombre de archivo para la copia
        nombre_copia_nuevo = f"optimizacion/codigo_{contador_copia}.txt"
        # Copiar el contenido de codigo.txt a un nuevo archivo
        shutil.copyfile("codigos/codigo.txt", nombre_copia_nuevo)
        with open("codigos/codigo.txt", "r") as archivo_entrada:
            # Lee el contenido del archivo línea por línea
            lineas = archivo_entrada.readlines()
    else:
        nombre_copia_nuevo = f"optimizacion/codigo_{contador_copia}.txt"
        nombre_copia_antes = f"optimizacion/codigo_{contador_copia-1}.txt"
        # Copiar el contenido de codigo.txt a un nuevo archivo
        shutil.copyfile(nombre_copia_antes, nombre_copia_nuevo)
        with open(nombre_copia_antes, "r") as archivo_entrada:
            # Lee el contenido del archivo línea por línea
            lineas = archivo_entrada.readlines()

    with open(nombre_copia_nuevo, 'w') as archivo_salida:
        en_ciclo=False
        borrado=False
        for num_linea, linea in enumerate(lineas, start=1):
            encontrado = False
            elementos = linea.split()
            if "11do11" in linea:
                en_ciclo=True
                linea_ciclo=num_linea
            elif "11while11" in linea:
                en_ciclo=False
            for num_elemento, elemento in enumerate(elementos, start=1):
                if elemento.startswith('JAM') and num_elemento < len(elementos) and elementos[num_elemento] == '=' and en_ciclo == False:
                    elemento_buscado = elemento
                    encontrado = False
                    for linea_restante in lineas[num_linea:]:
                        if elemento_buscado in linea_restante or elemento_buscado + "++" in linea_restante or elemento_buscado + "--" in linea_restante:
                            encontrado=True
                            archivo_salida.write(linea)
                            break
                    if not encontrado:
                        borrado = True
                        encontrado=True
                        if elemento not in elementos_encontrados:
                            elementos_encontrados.append(elemento)
                        print(f"No se encontró repetición para el elemento {elemento} en la línea {num_linea}.")
                elif elemento.startswith('JAM') and num_elemento < len(elementos) and elementos[num_elemento] == '=' and en_ciclo == True :
                    elemento_buscado = elemento
                    encontrado = False
                    for linea_restante in lineas[linea_ciclo:]:
                        if linea_restante != linea and (elemento_buscado in linea_restante or elemento_buscado + "++" in linea_restante or elemento_buscado + "--" in linea_restante):
                            encontrado=True
                            archivo_salida.write(linea)
                            break
                    if not encontrado:
                        borrado = True
                        encontrado=True
                        if elemento not in elementos_encontrados:
                            elementos_encontrados.append(elemento)
                        print(f"No se encontró repetición para el elemento {elemento} en la línea {num_linea}.")
                elif encontrado == False:
                    archivo_salida.write(linea)
                    break
    if not borrado:
        break
    contador_copia += 1

# Ruta del directorio donde se encuentran los archivos
directorio = "optimizacion"

# Obtén la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Filtra los archivos que comienzan con "codigo_" y son archivos
archivos_codigo = [archivo for archivo in archivos if archivo.startswith("codigo_") and os.path.isfile(os.path.join(directorio, archivo))]

# Ordena los archivos para asegurarse de que estén en orden numérico
archivos_codigo.sort()

# Si hay al menos dos archivos, borra todos excepto el último
if len(archivos_codigo) >= 2:
    archivos_a_borrar = archivos_codigo[:-1]
    for archivo in archivos_a_borrar:
        ruta_completa = os.path.join(directorio, archivo)
        os.remove(ruta_completa)
        print(f"Archivo {archivo} borrado.")
    ultimo_archivo = archivos_codigo[-1]
    ruta_completa_ultimo = os.path.join(directorio, ultimo_archivo)
    print(ruta_completa_ultimo)
    nuevo_nombre = os.path.join(directorio, "codigo.txt")
    try:
        os.remove(nuevo_nombre)
    except FileNotFoundError:
        print(f"El archivo {nuevo_nombre} no existe.")
    os.rename(ruta_completa_ultimo, nuevo_nombre)
else:
    print("No hay suficientes archivos para borrar.")

    

            
