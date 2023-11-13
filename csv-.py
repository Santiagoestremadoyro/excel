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


def read_csv(file_path):
    """
    Read data from a CSV file and return a DataFrame.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def write_csv(data_frame, file_path, index=False):
    """
    Write data to a CSV file.

    Parameters:
    - data_frame (pd.DataFrame): DataFrame to be written to the CSV file.
    - file_path (str): Path to the CSV file.
    - index (bool): Whether to include row indices. Default is False.
    """
    data_frame.to_csv(file_path, index=index)

def manipulate_csv(data_frame):
    """
    Perform some data manipulation on the CSV data.

    Parameters:
    - data_frame (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: Manipulated DataFrame.
    """
    # Your data manipulation logic here
    manipulated_data = data_frame  # Placeholder, replace with actual manipulation
    return manipulated_data