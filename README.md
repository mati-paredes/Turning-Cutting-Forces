# Turning-Cutting-Forces

## 📄 Descripción  
Este repositorio contiene los datos, gráficos y scripts utilizados para el análisis de fuerzas de corte en procesos de torneado.  
Incluye:  
- Datos experimentales obtenidos de distintos ensayos.  
- Procesamiento de señales y gráficos asociados.  
- Cálculo de parámetros como la presión específica de corte \(K_s\).
---
## 📁 Estructura del repositorio  

```text

Turning-Cutting-Forces/  
│
├── Ks/                               # Carpeta con scripts para determinar Ks
│   │
│   ├── CodigosExtra/                 # Scripts complementarios para generar gráficos adicionales
│   │
│   ├── DATA/                         # Datos procesados relevantes para cada etapa
│   │   └── *.csv                     # Fuerzas, tiempo, rpm, avances, señales, etc.
│   │
│   ├── IMAGENES/                     # Gráficos principales del informe
│   │
│   ├── INFORME/                      # Imágenes asociadas a los CodigosExtra
│   │   └── Imagenes/                 # Material visual utilizado en el informe
│   │
│   ├── K_s/                          # Datos medidos por el sensor (raw data del ensayo)
│   │
│   ├── 1_Graficas.py                 # Generación de los gráficos principales
│   ├── 2_Tacometro.py                # Determinación de rpm mediante la señal del tacómetro
│   ├── 3_Avance.py                   # Determinación de los avances para cada ensayo
│   ├── 4_Fuerzas.py                  # Cálculo de fuerzas promedio por ensayo
│   ├── 5_Ks.py                       # Ajuste de curva potencial para estimar K_s
│   │
│   ├── Datos.csv                     # Datos finales de ensayos 1–4 para la determinación de K_s
│   └── Datos_v1.csv                  # Datos base obtenidos tras inspección manual (entrada para scripts)
│
└── f_fixed/                          # Ensayos con avance fijo para calcular fuerzas
|   |
│   ├── A_p/                          # Datos medidos por el sensor (raw data del ensayo)
│   │
│   ├── DATA/                         # Datos procesados relevantes para cada etapa
│   │   └── *.csv                     # Fuerzas, tiempo, rpm, avances, señales, etc.
│   │
│   ├── IMAGENES/                     # Gráficos principales del informe
│   │
│   ├── 1_Graficas.py                 # Generación de los gráficos principales
│   ├── 2_Tacometro.py                # Determinación de rpm mediante la señal del tacómetro
│   ├── 3_Avance.py                   # Determinación de los avances para cada ensayo
│   ├── 4_Fuerzas.py                  # Cálculo de fuerzas promedio por ensayo
│   ├── 5_Ks.py                       # Determinacion de Fuerzas mediante Ks
│   │
│   ├── Datos.csv                     # Datos finales de ensayos 1–4 para la determinación de K_s
│   └── Datos_v1.csv                  # Datos base obtenidos tras inspección manual (entrada para scripts)

