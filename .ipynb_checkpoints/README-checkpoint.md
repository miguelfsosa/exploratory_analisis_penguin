## Readme.md - Análisis Exploratorio - Dataset Penguin Palmer

En este repositorio pretendo hacer un Análisis Exploratorio del Dataset Penguin Palmers, partiendo de un conocimiento y limpieza de los datos,
siguiendo con un análisis univariado para entender cómo se distribuye cada una de las variables para posteriormente analizar las relaciones
en un análisis multivariado y terminar con la definición de modelos de regresión simple y múltiple con el fin de predecir características de nuevos pingüinos en el estudio como el peso o el tamaño de las alas, y modelos de regresión logística con el objetivo de clasificar nuevos pingüinos en el estudio según su sexo o especie a partir de los datos analizados.

Las conclusiones del análisis se irán desarrollando en el Notebook y los detalles del código serán comentados con el fin que este ejercicio pueda servir
a alguien más para sus propios análisis.

### Datos que se encontrarán y se analizarán en este ejercicio
- species (object): Contiene la especie de los pingüinos (Adelie, Gentoo, Chinstrap)
- island (object): Contiene la isla donde habitan los pingüinos: (Torgersen, Biscoe Dream)
- bill_length_mm (float64): Longitud del pico en milímetros
- bill_depth_mm (float64): Profundida del pico en milímetros
- flipper_length_mm (float64): Longitud de las alas en milímetros
- body_mass_g (float64): Peso en gramos de los pingüinos
- sex (object): Sexo de los pingüinos (Male, Female)
- year (int64): Año en el que se tomó la observación

### Archivos que encontrarás en el repositorio:
-Analisis_Exploratorio.ipynb (Notebook con el análsis)
-dataset_penguins.csv (Dataset)
-ms_functions.py (Funciones genéricas que podrán ser útiles en otros análisis)
-pip_install_lib.txt (Comandos para instalar las librerías en el kernell en caso que no compile la importación inicial)
