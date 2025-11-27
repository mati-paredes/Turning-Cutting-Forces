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
                "A0","A0_cal","Fx","Fy","Fz",
                "F0","F0_cal"]

df["F0"] = round(df["F0"],3)
df["F0_cal"] = round(df["F0_cal"],3)

df = df[column_order]
df.to_csv("Datos.csv", index=False)



