import csv

# Función para buscar el lexema en el archivo "Direcciones.csv"
def buscar_lexema(num_linea, num_elemento):
    with open("Direcciones.csv", "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            if int(fila["Número de Línea"]) == num_linea and int(fila["Número de Elemento"]) == num_elemento:
                return fila["Elemento"]
    return None

# Abre el archivo "codigo_analizado.txt" en modo lectura
with open("codigo_analizado.txt", "r") as archivo_entrada:
    # Lee el contenido del archivo línea por línea
    lineas = archivo_entrada.readlines()

# Inicialización de variables
tabla_errores = []
contador_errores = 0
salto_linea = False

# Recorre las líneas del archivo "codigo_analizado"
for num_linea, linea in enumerate(lineas, start=1):
        # Divide la línea en elementos separados por espacios
    elementos = linea.split()

    #Detecta cualquier variable indefinida en la línea
    for num_elemento, elemento in enumerate(elementos, start=1):
        lexema = buscar_lexema(num_linea, num_elemento)
        if elemento == "Null":
            contador_errores += 1
            tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Variable Indefinida."])
        elif elementos[-1] != ";":
            if not elementos[-1] == "{":
                contador_errores += 1
                lexema= elementos[-1]
                num_elemento = len(elementos)
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "';' Faltante en línea o mal insertado."])
                break
        
    # Verifica las condiciones para detectar errores y registrarlos en la tabla de errores
    for num_elemento, elemento in enumerate(elementos, start=1):
        lexema = buscar_lexema(num_linea, num_elemento)
        indice = elementos.index(elemento)
        if elemento == "|ENT|" and elementos[indice+1] == "=":
            if "|CAD|" in elementos or "|REAL|" in elementos:
                listo=0
                while listo == 0:
                    for num2_elemento, elemento2 in enumerate(elementos, start=1):
                        if elemento2 == "|CAD|" or elemento2 == "|REAL|" and listo==0:
                            listo = 1
                            lexema = buscar_lexema(num_linea, num2_elemento)
                            contador_errores += 1
                            tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num2_elemento, lexema, "Incompatibilidad de Tipos |ENT|."])
                            print("listo")
                            break
            break
        elif elemento == "|REAL|" and elementos[indice+1] == "=":
            if "|CAD|" in elementos:
                listo=0
                while listo == 0:
                    for num2_elemento, elemento2 in enumerate(elementos, start=1):
                        if elemento2 == "|CAD|" and listo==0:
                            listo = 1
                            lexema = buscar_lexema(num_linea, num2_elemento)
                            contador_errores += 1
                            tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num2_elemento, lexema, "Incompatibilidad de Tipos |REAL|."])
                            print("listo")
                            break
            break
        elif elemento == "|CAD|":
            if "|REAL|" in elementos or "|ENT|" in elementos:
                contador_errores += 1
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Incompatibilidad de Tipos |CAD|"])
                break
        elif elemento == "11do11":
            if not "{" in elementos[1]:
                contador_errores += 1
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Falta '{'"])
                break
        elif elemento == "11while11":
            indice = elementos.index('(')
            if not "}" in elementos[0]:
                contador_errores += 1
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Falta '}'"])
            elif not "(" in elementos[2] or not ")" in elementos:
                contador_errores += 1
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Faltan símbolos completos '(' ')'"])
                break
            elif not "OPR" in elementos:
                contador_errores += 1
                tabla_errores.append(["ERSem" + str(contador_errores), num_linea, num_elemento, lexema, "Evaluación errónea"])
                break
      

# Abre un nuevo archivo CSV "Errores.csv" en modo escritura
with open("Errores.csv", "w", newline="") as archivo_csv:
    # Crea un escritor CSV
    escritor_csv = csv.writer(archivo_csv)

    # Escribe la cabecera del archivo CSV
    escritor_csv.writerow(["Token Error", "Línea", "Elemento", "Lexema", "Descripción"])

    # Escribe los errores en el archivo CSV
    for error in tabla_errores:
        escritor_csv.writerow(error)

print("Se ha creado el archivo 'Errores.csv' con la tabla de errores detectados.")
