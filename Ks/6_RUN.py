import subprocess
import pandas as pd
import numpy as np

scripts = ["1_Graficas.py", "2_Tacometro.py", "3_Avance.py", "4_Fuerzas.py", "5_Ks.py"]

for script in scripts:
    subprocess.run(["python", script])
    
df = pd.read_csv("DATA/Datos_v5.csv")
columnas = ["archivo","idx_inicio","x_inicio","idx_fin",
            "x_fin"]
df = df.drop(columns=columnas)

df["Ensayo"] = [1,2,3,4]

column_order = ["Ensayo","L","time","rpm","f","f_cal",
                "A0","A_cal","Fx","Fy","Fz",
                "Ks_0","Ks_cal","KS0",
                "m","R2"]

df = df[column_order]
df.to_csv("Datos.csv", index=False)


