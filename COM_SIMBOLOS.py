import csv
import re

# Función para determinar el tipo de dato
def determinar_tipo(linea):
    if "|CAD|" in linea:
        return "|CAD|"
    elif "|REAL|" in linea:
        return "|REAL|"
    elif "|ENT|" in linea:
        return "|ENT|"
    else:
        return "Null"

# Función para leer el archivo "codigo.txt" y crear el archivo CSV
def crear_tabla_simbolos():
    # Diccionario para almacenar los lexemas únicos y su tipo de dato
    lexemas = {}

    # Abre el archivo de entrada "codigo.txt" en modo lectura
    with open("optimizacion/codigo_optimizado.txt", "r") as archivo_entrada:
        # Lee el contenido del archivo línea por línea
        for linea in archivo_entrada:
            # Divide la línea en palabras usando espacios como separadores
            palabras = linea.split()
            for palabra in palabras:
                # Si la palabra inicia con "JAM" y no está en el diccionario
                if palabra.startswith("JAM") and palabra not in lexemas:
                    if palabra.endswith("++") or palabra.endswith("--"):
                        break
                    else:
                        tipo_dato = determinar_tipo(linea)
                        lexemas[palabra] = tipo_dato
                elif palabra.startswith('"') and palabra.endswith('"'):
                    lexemas[palabra] = "|CAD|"
                # Comprueba si el palabra es un número entero manualmente
                elif all(caracter.isdigit() for caracter in palabra) and palabra.startswith('11') and palabra.endswith('11'):
                    lexemas[palabra] = "|ENT|"
                # Comprueba si el palabra es un número real manualmente
                elif (all((caracter.isdigit() or caracter == '.') for caracter in palabra) and 
                                                                    palabra.count('.') == 1 and 
                                                                    palabra.startswith("11") and 
                                                                    palabra.count("11.") == 1):
                    lexemas[palabra] = "|REAL|"
                # Comprueba si el palabra es un símbolo aritmético
                elif palabra in ("+", "-", "*", "/", "%"):
                    lexemas[palabra] = "OPA"
                # Comprueba si el palabra es un operador relacional
                elif palabra in (">", "<", ">=", "<=", "==", "!="):
                    lexemas[palabra] = "OPR"
                elif palabra in ("&&", "||"):
                    lexemas[palabra] = "LOG"
                elif palabra not in lexemas:
                    lexemas[palabra] = ""

    # Abre el archivo CSV "Tabla_Simbolos.csv" en modo escritura
    with open("salidas/Tabla_Simbolos.csv", "w", newline="") as archivo_csv:
        # Define las columnas del archivo CSV
        columnas = ["Lexemas", "Tipo de Dato"]

        # Crea el objeto escritor CSV
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=columnas)

        # Escribe la fila de encabezado en el archivo CSV
        escritor_csv.writeheader()

        # Escribe los lexemas y su tipo de dato en el archivo CSV
        for lexema, tipo_dato in lexemas.items():
            escritor_csv.writerow({"Lexemas": lexema, "Tipo de Dato": tipo_dato})

if __name__ == "__main__":
    crear_tabla_simbolos()
    print("Se ha creado el archivo CSV 'Tabla_Simbolos' con éxito.")
