import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

componentes = ["Fz"]

def read_lvm_file(path):
    start_line = None
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if line.strip().startswith("X_Value"):
                start_line = i
                break
    df = pd.read_csv(path, sep="\t", skiprows=start_line)
    return df

def parse_filename(file):
    base = os.path.splitext(file)[0]
    f_part, a_part = base.split("_")
    avance = int(f_part.replace("f", "")) / 1000  
    prof   = int(a_part.replace("a", "")) / 100   
    return avance, prof 

folder = "K_s"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])
limites = pd.read_csv("DATA/Datos_v1.csv")

inicios = limites["idx_inicio"].astype(int)
fines   = limites["idx_fin"].astype(int)

idx_random = np.random.randint(0, len(files))

componentes = ["Fz"]

for C in componentes:
    
    fig, ax = plt.subplots(figsize=(16, 4))

    file = files[idx_random]
    df = read_lvm_file(os.path.join(folder, file))
    avance, prof = parse_filename(file)

    ax.plot(df["X_Value"], df[C], label=f"Avance = {avance:.3f} mm")

    x1 = df["X_Value"].iloc[inicios[idx_random]]
    x2 = df["X_Value"].iloc[fines[idx_random]]

    ax.axvline(x=x1, color="red", linestyle="--", alpha=0.7)
    ax.axvline(x=x2, color="red", linestyle="--", alpha=0.7)

    ax.legend(fontsize=10, loc="best")

    plt.tight_layout()
    plt.savefig(f"INFORME/RAW_{C}.svg", format="svg")
    plt.close(fig)
