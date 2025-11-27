import pandas as pd

datos = pd.read_csv("DATA/Datos_v2.csv")

l = datos["L"]
t = datos["time"]
n = datos["rpm"]
ap = 1
datos["f_cal"] = round((60 * l) / (t * n),3)
datos["A0"] = ap*datos["f"]
datos["A_cal"] = datos["f_cal"]*ap
datos.to_csv("DATA/Datos_v3.csv", index=False)

