import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

df = pd.read_csv("DATA/Datos_v4.csv")

ruta_modelo = r"C:\Users\pared\Desktop\Nivel 7\NORMAS FABRI\LABORATORIO 2\CALCULO KS\Datos.csv"
modelo = pd.read_csv(ruta_modelo)

KS0 = modelo.loc[0, "KS0"]
m = modelo.loc[0, "m"]

h = 0.104
Ks = KS0 * (h ** -m)
df["F0"] = Ks * df["A0"]
df["F0_cal"] = Ks * df["A0_cal"]

os.makedirs("DATA", exist_ok=True) 
df.to_csv("DATA/Datos_v5.csv", index=False)

