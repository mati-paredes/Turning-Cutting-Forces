import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def read_lvm_file(path, ind_i, ind_f):
    start_line = None
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if line.strip().startswith("X_Value"):
                start_line = i
                break
    df = pd.read_csv(path, sep="\t", skiprows=start_line)
    return df.iloc[ind_i:ind_f]

def select_middle_80(df):
    n = len(df)
    keep = int(n * 0.80)
    start = (n - keep) // 2
    end = start + keep
    return df.iloc[start:end]

folder = "K_s"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])

file = files[0]

datos = pd.read_csv("DATA/Datos_v3.csv")
ind_i = int(datos.loc[0, "idx_inicio"])
ind_f = int(datos.loc[0, "idx_fin"])

df = read_lvm_file(os.path.join(folder, file), ind_i, ind_f)
df_80 = select_middle_80(df)

plt.figure(figsize=(12,4))
plt.plot(df["X_Value"], df["Fz"], alpha=0.5, label="Original")
plt.plot(df_80["X_Value"], df_80["Fz"], label="Rango medio 80%")

plt.xlabel("Tiempo (s)")
plt.ylabel("Fz (N)")
plt.title(f"Cálculo de fuerza promedio Fz")
plt.legend()
plt.tight_layout()
plt.savefig(f"INFORME/fuerza.svg", format="svg")
plt.show()
