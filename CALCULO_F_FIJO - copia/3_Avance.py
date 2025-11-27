import pandas as pd

datos = pd.read_csv("DATA/Datos_v2.csv")

l = datos["L"]
t = datos["time"]
n = datos["rpm"]
f = 0.104

datos["f_cal"] = round((60 * l) / (t * n),3)


datos["A0"] = datos["ap"]*f
datos["A0_cal"] = datos["ap"]*datos["f_cal"]
datos.to_csv("DATA/Datos_v3.csv", index=False)

