# Turning-Cutting-Forces

## 📄 Descripción  
Este repositorio contiene los scripts asociados al análisis de fuerzas de corte en operaciones de torneado. Incluye:  
- Datos experimentales obtenidos de distintos ensayos de corte.  
- Scripts en Python para la **manipulación de señales**, **procesamiento de datos** y **generación de gráficos**.  
- Cálculo de la presión de corte específica \(K_s\).

## 📁 Estructura del repositorio  

Turning-Cutting-Forces/
├── K_s/                          # Cálculo de K_s y datos utilizados para su determinación
│   ├── Datos.csv                 # Datos finales utilizados para el cálculo de K_s
│   ├── Datos_v1.csv              # Datos obtenidos tras la inspección manual de límites
│   └── K_s.py                    # Script para el ajuste de curva potencial
│
├── DATA/                         # Datos originales de los ensayos
│   └── *.csv                     # Fuerzas, tiempo, rpm, avances, etc.
│
├── Imagenes/                     # Gráficos asociados a los ensayos de corte
│   └── *.png / *.jpg             # Resultados visuales
│
├── Codigos Extra/                # Scripts complementarios utilizados en el informe
│   ├── Tacometro.py              # Obtención de rpm desde señal del tacómetro
│   ├── Avance.py                 # Determinación de avances por ensayo
│   ├── Fuerzas.py                # Cálculo de fuerzas promedio
│   └── K_s_extra.py              # Variantes o pruebas relacionadas al cálculo de K_s
│
├── Informe/                   
│   └── Imagenes/                 # Imágenes asociadas a los códigos extra
│
├── Graficas.py                   # Script principal para generar gráficos
└── README.md                     # Documento actual


