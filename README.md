# Turning-Cutting-Forces

## 📄 Descripción  
Este repositorio contiene los datos, gráficos y scripts utilizados para el análisis de fuerzas de corte en procesos de torneado.  
Incluye:  
- Datos experimentales obtenidos de distintos ensayos.  
- Procesamiento de señales y gráficos asociados.  
- Cálculo de parámetros como la presión específica de corte \(K_s\).
---

## 📁 Estructura del repositorio  

Turning-Cutting-Forces/  
│  
├── Ks/                               # Carpeta principal del análisis  
│   │  
│   ├── codigos extra/                # Scripts complementarios (no relacionados con tacómetro/avance/fuerzas)  
│   │  
│   ├── DATA/                         # Datos originales de los ensayos  
│   │   └── *.csv                     # Fuerzas, tiempo, rpm, avances, señales, etc.  
│   │  
│   ├── IMAGENES/                     # Gráficos generados  
│   │   └── *.png / *.jpg             # Resultados visuales del análisis  
│   │  
│   ├── INFORME/                      # Archivos utilizados para la elaboración del informe  
│   │   └── Imagenes/                 # Imágenes para el informe  
│   │  
│   ├── K_s/                          # Cálculo de la presión específica de corte  
│   │   ├── Datos.csv                 # Datos finales para el cálculo de K_s  
│   │   ├── Datos_v1.csv              # Datos tras inspección manual  
│   │   └── K_s.py                    # Script para ajuste y determinación de K_s  
│   │  
│   └── README_local.txt (si existe)  # Archivos de apoyo (opcional)  
│  
└── f_fixed/                          # Carpeta con datos o análisis bajo condiciones "f fijado"  
    └── (estructura variable según ensayos)



