# Abre el archivo "codigo_reemplazado.txt" en modo lectura
with open("codigo_reemplazado.txt", "r") as archivo_entrada:
    # Lee el contenido del archivo línea por línea
    lineas = archivo_entrada.readlines()

# Abre un nuevo archivo "codigo_analizado.txt" en modo escritura
with open("codigo_analizado.txt", "w") as archivo_salida:
    # Recorre las líneas del archivo "codigo_reemplazado"
    for linea in lineas:
        # Divide la línea en elementos separados por espacios
        elementos = linea.split()
        nueva_linea = ""

        # Analiza cada elemento en la línea
        for elemento in elementos:
            if elemento == "|ENT|":
                # Es un número entero
                nueva_linea += "|ENT| "
            elif elemento == "|REAL|":
                # Es un número real
                nueva_linea += "|REAL| "
            else:
                # Comprueba si el elemento inicia y termina con comillas dobles
                if elemento.startswith('"') and elemento.endswith('"'):
                    nueva_linea += "|CAD| "
                # Comprueba si el elemento es un número entero manualmente
                elif all(caracter.isdigit() for caracter in elemento):
                    nueva_linea += "|ENT| "
                # Comprueba si el elemento es un número real manualmente
                elif all((caracter.isdigit() or caracter == '.') for caracter in elemento) and elemento.count('.') == 1:
                    nueva_linea += "|REAL| "
                # Comprueba si el elemento es un símbolo aritmético
                elif elemento in ("+", "-", "*", "/", "%"):
                    nueva_linea += "OPA "
                # Comprueba si el elemento es un operador relacional
                elif elemento in (">", "<", ">=", "<=", "==", "!="):
                    nueva_linea += "OPR "
                else:
                    # Si no es ninguno de los casos anteriores, conserva el elemento tal como está
                    nueva_linea += elemento + " "

        # Escribe la línea modificada en el archivo de salida
        archivo_salida.write(nueva_linea.strip() + "\n")

print("Se ha creado el archivo 'codigo_analizado.txt' con los elementos analizados y reemplazados según las reglas definidas.")
