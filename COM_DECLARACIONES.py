
with open("optimizacion/codigo.txt", "r") as archivo_entrada:
    # Lee el contenido del archivo línea por línea
    lineas = archivo_entrada.readlines()

with open("optimizacion/codigo_optimizado.txt", 'w') as archivo_salida:
  for num_linea, linea in enumerate(lineas, start=1):
    elementos = linea.split()
    if "|ENT|" in linea or "|CAD|" in linea or "|REAL|" in linea:
      elementos_nuevos = []

      for num_elemento, elemento in enumerate(elementos, start=1):
        
        if elemento.startswith('JAM'):
          
          elemento_buscado = elemento
          encontrado = False
          for linea_restante in lineas[num_linea:]:
            if elemento_buscado in linea_restante or elemento_buscado + "++" in linea_restante or elemento_buscado + "--" in linea_restante:
              encontrado=True
              break
          if encontrado:
            print(elemento)
            elementos_nuevos.append(elemento)
        elif elemento != ";" and elemento != ",":
          elementos_nuevos.append(elemento)

      # Crea la nueva línea con los elementos modificados
      nueva_linea = ""
      for idx, elemento in enumerate(elementos_nuevos):
          if elemento.startswith('JAM'):
              nueva_linea += elemento
              if idx < len(elementos_nuevos) - 1:
                  nueva_linea += " , "
              else:
                  nueva_linea += " ;\n"
          else:
              nueva_linea += elemento + " "

      archivo_salida.write(nueva_linea)

    else:
      # Conserva las líneas que no comienzan con '|ENT|'
      archivo_salida.write(linea) 

            
