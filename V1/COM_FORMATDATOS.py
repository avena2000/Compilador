def formatear_texto(texto):
    lineas = texto.split('\n')
    resultado = []
    
    for linea in lineas:
        # Eliminar espacios en blanco al inicio y final de la línea
        linea = linea.strip()
        
        # Reemplazar más de dos espacios en blanco por uno solo
        linea = ' '.join(linea.split())
        
        # Agregar un espacio en blanco al inicio y final de la línea
        linea = ' ' + linea + ' '
        
        resultado.append(linea)
    
    texto_formateado = '\n'.join(resultado)
    
    return texto_formateado

# Leer el contenido del archivo "codigo.txt"
try:
    with open("codigo_analizado.txt", "r") as archivo:
        texto_original = archivo.read()

    # Aplicar el formato al texto leído
    texto_formateado = formatear_texto(texto_original)

    # Guardar el texto formateado en el mismo archivo
    with open("codigo_analizado.txt", "w") as archivo:
        archivo.write(texto_formateado)

    print("Texto formateado y guardado exitosamente en 'codigo.txt'.")

except FileNotFoundError:
    print("El archivo 'codigo.txt' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
