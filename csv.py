import csv
##
# importamos la librería csv, luego definimos una lista de listas, cada lista será una fila dentro de nuestro archivo
#  csv. Continuamos abriendo un archivo con las sentencias with y open, y le ponemos un alias al archivo que crearemos
#  en este caso nombres.csv. En las dos últimas líneas definimos un writer para nuestro archivo y finalmente escribimos
#  los datos que definimos en la lista de listas.

with open('swimming_pools.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      print(', '.join(row))


##En la primera línea lo que hacemos es importar la librería csv, siguiente a esto abrimos el archivo y el 
# asignamos un nombre alias. Luego declaramos el lector del archivo csv, finalmente, mediante el uso del ciclo
#  for recorremos las filas del archivo que para este momento se han vuelto una lista de Python, para mostrar el
#  contenido en un formato con comas hacemos uso de la instrucción join.

datos = [["Nombre", "Apellido", "Edad"], ["Ana", "Sevilla", "20"]]

with open ('nombres.csv', 'w') as csv_file:
    writer = csv.write(csv_file)
    writer.writerowsw(datos)