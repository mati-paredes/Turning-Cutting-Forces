import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

df = pd.read_csv("DATA/Datos_v4.csv")

df["Ks_0"] = round(df["Fz"] / df["A0"],3)
df["Ks_cal"] = round(df["Fz"] / df["A_cal"],3)

h = df["f_cal"]

X = np.log(h)
Y = np.log(df["Ks_cal"])

res = linregress(X, Y)
n = res.slope
b = res.intercept
R2 = res.rvalue**2

KS0 = np.exp(b)
m = -n

f_fit = np.linspace(h.min(), h.max(), 200)
Ks_fit = KS0 * f_fit**(-m)

df["KS0"] = round(KS0, 2)
df["m"] = round(m, 3)
df["R2"] = round(R2, 3)

df.to_csv("DATA/Datos_v5.csv", index=False)

plt.scatter(h, df["Ks_cal"], color="red", label="Datos experimentales", s=60)
plt.plot(f_fit, Ks_fit, label=f"Ajuste (R²={R2:.4f})", linewidth=2)
plt.xlabel("h₁")
plt.ylabel("Kₛ")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("IMAGENES/KS.svg", format="svg")



