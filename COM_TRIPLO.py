import csv

# Inicializamos una lista para almacenar los datos a guardar en el CSV
triplo = []
linea_triplo=0
with open("modificaciones/codigo_limpio.txt", "r") as archivo_entrada:
    # Lee el contenido del archivo línea por línea
    lineas = archivo_entrada.readlines()

for num_linea, linea in enumerate(lineas, start=1):
  elementos = linea.split()

  if "11do11" in linea:
    if linea_triplo == 0:
      do_jmp = 1
    else:
      do_jmp = linea_triplo + 1
    print

  elif "11while11" in linea:
    for num_elemento, elemento in enumerate(elementos, start=1):
      if elemento == '(':
        indice = elementos.index(elemento)
        if indice > 0 and indice < len(elementos) - 1:
          #Primera Condición: T1 = "x"
          linea_triplo+=1
          triplo.append([linea_triplo,"T1", elementos[indice + 1], "="])
          #Primera Condición: T1 OPR "y"
          linea_triplo+=1
          triplo.append([linea_triplo,"T1", elementos[indice + 3], elementos[indice + 2]])
          if elementos[indice + 4] == "||": #OR
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "TRUE", do_jmp])
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "FALSE", linea_triplo+1])
          elif elementos[indice + 4] == "&&": #AND
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "TRUE", linea_triplo+2])
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "FALSE", linea_triplo+5])
          else:
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "TRUE", do_jmp])
            linea_triplo+=1
            triplo.append([linea_triplo,"TR1", "FALSE", linea_triplo+1])
      elif elemento == "||" or elemento =="&&":
        indice = elementos.index(elemento)
        #Segunda Condición: T1 = "x"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", elementos[indice + 1], "="])
        #Segunda Condición: T1 OPR "y"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", elementos[indice + 3], elementos[indice + 2]])
        if elementos[indice] == "||": #OR
          linea_triplo+=1
          triplo.append([linea_triplo,"TR1", "TRUE", do_jmp])
          linea_triplo+=1
          triplo.append([linea_triplo,"TR1", "FALSE", linea_triplo+1])
        elif elementos[indice] == "&&": #AND
          linea_triplo+=1
          triplo.append([linea_triplo,"TR1", "TRUE", do_jmp])
          linea_triplo+=1
          triplo.append([linea_triplo,"TR1", "FALSE", linea_triplo+1])

  elif "=" in linea and not any(op in linea for op in ['+', '-', '*', '/']):
    for num_elemento, elemento in enumerate(elementos, start=1):
      if elemento == '=':
        indice = elementos.index(elemento)
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", elementos[indice + 1], "="])
        linea_triplo+=1
        triplo.append([linea_triplo,elementos[indice - 1], "T1", "="])
        
  elif "=" in linea and any(op in linea for op in ['+', '-', '*', '/']):
    for num_elemento, elemento in enumerate(elementos, start=1):
      if elemento == '=':
        indice = elementos.index(elemento)
        if indice > 0 and indice < len(elementos) - 1:
          #Imprimir en el Triplo Operación T1 = "x"
          linea_triplo+=1
          triplo.append([linea_triplo,"T1", elementos[indice + 1], "="])
          #Imprimir en el Triplo Operación T1 OPR "y"
          linea_triplo+=1
          triplo.append([linea_triplo,"T1", elementos[indice + 3], elementos[indice + 2]])
          #Imprimir en el Triplo Asignación "Z" = T1
          linea_triplo+=1
          triplo.append([linea_triplo,elementos[indice - 1], "T1", "="])
  #Añadir ++ en el triplo
  else:
    for num_elemento, elemento in enumerate(elementos, start=1):
      if elemento.endswith("++"):
        #Imprimir en el Triplo Operación T1 = "x"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", elemento.rstrip("+-"), "="])
        #Imprimir en el Triplo Operación T1 OPR "y"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", 1, "+"])
        #Imprimir en el Triplo Asignación "Z" = T1
        linea_triplo+=1
        triplo.append([linea_triplo,elemento.rstrip("+-"), "T1", "="])
      if elemento.endswith("--"):
        #Imprimir en el Triplo Operación T1 = "x"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", elemento.rstrip("+-"), "="])
        #Imprimir en el Triplo Operación T1 OPR "y"
        linea_triplo+=1
        triplo.append([linea_triplo,"T1", 1, "-"])
        #Imprimir en el Triplo Asignación "Z" = T1
        linea_triplo+=1
        triplo.append([linea_triplo,elemento.rstrip("+-"), "T1", "="])
#Línea Final para mostar salida
linea_triplo+=1
triplo.append([linea_triplo,"", "", "end"])
# Guardamos los datos en un archivo CSV
with open("salidas/Triplo.csv", 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["#","Dato objeto", "Dato Fuente", "Operador"])
    escritor.writerows(triplo)

print(f"Se han guardado los datos en el archivo CSV")
