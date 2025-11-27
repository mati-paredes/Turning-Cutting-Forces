import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def read_lvm_file(path):
    start_line = None
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if line.strip().startswith("X_Value"):
                start_line = i
                break
    df = pd.read_csv(path, sep="\t", skiprows=start_line)
    return df

folder = "A_p"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])

fig, axes = plt.subplots(len(files), 1, figsize=(12, 8))
axes = axes.flatten()

resultados = []

for i, file in enumerate(files):
    full_path = os.path.join(folder, file)
    df = read_lvm_file(full_path)

    t = df["X_Value"].values
    taco = df["Taco"].values

    axes[i].plot(t, taco, label=file)
    axes[i].legend()

    thr = (taco.max() + taco.min()) / 5
    edges = np.where((taco[:-1] < thr) & (taco[1:] > thr))[0]

    t_edges = t[edges]
    periodos = np.diff(t_edges)

    periodos = periodos[(periodos > 0) & (periodos < 1)]

    periodo_rep = np.median(periodos)
    rpm = round(60 / periodo_rep, -1)

    resultados.append(rpm)

axes[-1].set_xlabel("Tiempo (s)")
plt.tight_layout()

datos = pd.read_csv("DATA/Datos_v1.csv")
datos["rpm"] = resultados
datos.to_csv("DATA/Datos_v2.csv", index=False)
