import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

C = "Fz"

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

def select_middle_80(df):
    n = len(df)
    keep = int(n * 0.80)           
    start = (n - keep) // 2       
    end = start + keep            
    return df.iloc[start:end]

folder = "K_s"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])


datos = pd.read_csv("DATA/Datos_v3.csv")

inicios = datos["idx_inicio"].astype(int)
fines   = datos["idx_fin"].astype(int)

fig, axes = plt.subplots(4, 1, figsize=(16, 10))
axes = axes.flatten()

resultados_Fx = np.zeros(4)
resultados_Fy = np.zeros(4)
resultados_Fz = np.zeros(4) 

for i, file in enumerate(files):

    df = read_lvm_file(os.path.join(folder, file), inicios[i], fines[i])
    df_80 = select_middle_80(df)

    avance, prof = parse_filename(file)
    axes[i].plot(df["X_Value"], df[C], color="orange", alpha=0.8, label="Original")
    axes[i].plot(df_80["X_Value"], df_80[C], label=f"Avance {avance:.3f} mm")
    axes[i].legend()

    resultados_Fz[i] = round(np.mean(df_80["Fz"]), 3)
    resultados_Fx[i] = round(np.mean(df_80["Fx"]), 3)
    resultados_Fy[i] = round(np.mean(df_80["Fy"]), 3)

datos["Fz"] = resultados_Fz
datos["Fx"] = resultados_Fx
datos["Fy"] = resultados_Fy

datos.to_csv("DATA/Datos_v4.csv", index=False)

plt.tight_layout()
plt.savefig(f"IMAGENES/rango80.svg", format="svg")




