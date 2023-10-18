import csv

# Abre el archivo de texto en modo lectura
with open('codigo_formateado.txt', 'r') as archivo_entrada:
    lineas = archivo_entrada.readlines()

# Abre el archivo CSV en modo escritura con las columnas especificadas
with open('Direcciones.csv', 'w', newline='') as archivo_salida:
    columnas = ['Elemento', 'Número de Línea', 'Número de Elemento']
    writer = csv.DictWriter(archivo_salida, fieldnames=columnas)
    writer.writeheader()
    
    # Inicializa el contador de línea
    numero_linea = 0
    
    # Recorre cada línea del archivo de texto
    for linea in lineas:
        # Ignora las líneas que empiezan con |REAL|, |CAD|, |ENT|
        if not linea.startswith(' |REAL|') and not linea.startswith(' |CAD|') and not linea.startswith(' |ENT|'):
            # Divide la línea en elementos por espacio
            elementos = linea.split()
            
            # Si la línea tiene elementos, añade una entrada en la tabla CSV
            if elementos:
                # Incrementa el contador de línea
                numero_linea += 1
                
                # Recorre los elementos de la línea y añade una fila por cada elemento
                for numero_elemento, elemento in enumerate(elementos):
                    writer.writerow({'Elemento': elemento, 'Número de Línea': numero_linea, 'Número de Elemento': numero_elemento + 1})
