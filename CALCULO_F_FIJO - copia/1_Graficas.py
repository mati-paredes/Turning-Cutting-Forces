import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

componentes = ["Fx", "Fy", "Fz"]

def read_lvm_file(path, ind_i, ind_f):
    start_line = None
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if line.strip().startswith("X_Value"):
                start_line = i
                break
    df = pd.read_csv(path, sep="\t", skiprows=start_line)
    return df.iloc[ind_i:ind_f]

def parse_filename(file):
    base = os.path.splitext(file)[0]
    f_part, a_part = base.split("_")
    avance = int(f_part.replace("f", "")) / 1000  
    prof   = int(a_part.replace("a", "")) / 100   
    return avance, prof 

folder = "A_p"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])
limites = pd.read_csv("DATA/Datos_v1.csv")
inicios = limites["idx_inicio"].astype(int)
fines   = limites["idx_fin"].astype(int)

for C in componentes:
    fig, axes = plt.subplots(4, 1, figsize=(16, 10))
    axes = axes.flatten()

    for i, file in enumerate(files):
        df = read_lvm_file(os.path.join(folder, file), inicios[i], fines[i])
        avance, prof = parse_filename(file)
        axes[i].plot(
        df["X_Value"], df[C], 
        label=fr"$a_{{p}} = {prof:.3f}\,\mathrm{{mm}}$")
        axes[i].legend(fontsize=10, loc="lower center")

    plt.tight_layout()
    plt.savefig(f"IMAGENES/RAW{C}_f.svg", format="svg")
    plt.close(fig)

    fig2, ax2 = plt.subplots(figsize=(14, 7))
    for i, file in enumerate(files):
        df = read_lvm_file(os.path.join(folder, file), inicios[i], fines[i])
        avance, prof = parse_filename(file)
        label=fr"$a_{{p}} = {prof:.3f}\,\mathrm{{mm}}$"
        ax2.plot(df["X_Value"] - df["X_Value"].min(), df[C], label=label, alpha=0.8)

    ax2.set_xlabel("t")
    ax2.set_ylabel(C)
    ax2.legend(loc="best")
    plt.tight_layout()
    plt.savefig(f"IMAGENES/Complete_{C}_f.svg", format="svg")
    plt.close(fig2)

