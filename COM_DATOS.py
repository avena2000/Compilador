import csv
import re

# Función para cargar el diccionario de la tabla de símbolos desde "Tabla_Simbolos.csv"
def cargar_tabla_simbolos():
    tabla_simbolos = {}
    with open("salidas/Tabla_Simbolos.csv", "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            lexema = fila["Lexemas"]
            tipo_dato = fila["Tipo de Dato"]
            tabla_simbolos[lexema] = tipo_dato
    return tabla_simbolos

# Función para reemplazar elementos JAM en el archivo "codigo_formateado"
def reemplazar_elementos_jam():
    tabla_simbolos = cargar_tabla_simbolos()

    # Abre el archivo de entrada "codigo_formateado" en modo lectura
    with open("optimizacion/codigo_optimizado.txt", "r") as archivo_entrada:
        # Lee el contenido del archivo línea por línea
        lineas = archivo_entrada.readlines()

    # Abre el archivo de salida "codigo_reemplazado.txt" en modo escritura
    with open("modificaciones/tipos_JAM.txt", "w") as archivo_salida:
        # Recorre las líneas del archivo "codigo_formateado"
        for linea in lineas:
            # Si la línea contiene "|ENT|", "|CAD|", o "|REAL|", se escribe tal como está
            if "|ENT|" in linea or "|CAD|" in linea or "|REAL|" in linea:
                archivo_salida.write("")
                continue

            # Busca elementos que inician con "JAM" en la línea
            elementos_jam = re.findall(r'JAM\w*', linea)
            for elemento_jam in elementos_jam:
                # Reemplaza el elemento JAM por su Tipo de Dato
                if elemento_jam in tabla_simbolos:
                    linea = linea.replace(elemento_jam, tabla_simbolos[elemento_jam])
            # Escribe la línea modificada en el archivo de salida
            archivo_salida.write(linea)

if __name__ == "__main__":
    reemplazar_elementos_jam()
    print("Se ha creado el archivo 'codigo_reemplazado.txt' con los elementos JAM reemplazados por Tipo de Dato, conservando las líneas con '|ENT|', '|CAD|', o '|REAL|'.")
