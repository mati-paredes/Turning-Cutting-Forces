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

folder = "K_s"
files = sorted([f for f in os.listdir(folder) if f.lower().endswith(".lvm")])

file = files[0]
full_path = os.path.join(folder, file)

df = read_lvm_file(full_path)

t = df["X_Value"].values
taco = df["Taco"].values

thr = (taco.max() + taco.min()) / 2
taco_thr = (taco > thr).astype(int)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

axes[0].plot(t, taco, label="Señal original")
axes[0].set_title("Señal original")
axes[0].set_xlabel("Tiempo (s)")
axes[0].set_xlim(0,0.10)
axes[0].set_ylabel("Amplitud")
axes[0].legend()

axes[1].plot(t, taco_thr, label="Binaria", c= "r")
axes[1].set_title("Señal tras aplicar threshold")
axes[1].set_xlabel("Tiempo (s)")
axes[1].set_xlim(0,0.10)
axes[1].set_ylabel("0/1")
axes[1].set_ylim(-0.2, 1.2)
axes[1].legend()

plt.tight_layout()
plt.savefig(f"INFORME/TACOMETROEXTRA.svg", format="svg")
plt.show()
