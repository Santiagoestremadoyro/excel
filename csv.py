import csv
##importamos la librería csv, luego definimos una lista de listas, cada lista será una fila dentro de nuestro archivo
#  csv. Continuamos abriendo un archivo con las sentencias with y open, y le ponemos un alias al archivo que crearemos
#  en este caso nombres.csv. En las dos últimas líneas definimos un writer para nuestro archivo y finalmente escribimos
#  los datos que definimos en la lista de listas.


datos = [["Nombre", "Apellido", "Edad"], ["Ana", "Sevilla", "20"]]

with open ('nombres.csv', 'w') as csv_file:
    writer = csv.write(csv_file)
    writer.writerowsw(datos)