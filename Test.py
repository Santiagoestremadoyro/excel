import pandas as pd


path_file = "Carta.xlsx"
col_types = {"Platos" : str, "Ingredientes": str}
hoja = "Carta"
df = pd.read_excel(path_file, sheet_name=hoja, dtype=col_types)

outfile = "Resultados.xlsx"
writer = pd.ExcelWriter(outfile,engine="xlsxwriter")
df.to_excel(writer,sheet_name="Mayor a 200 páginas")
writer.save()