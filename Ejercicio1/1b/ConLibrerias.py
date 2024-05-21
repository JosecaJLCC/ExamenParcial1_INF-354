# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:46:37 2024

@author: joswe
"""

import numpy as np
import pandas as pd
datos = pd.read_csv("cellphonesdata.csv", sep=",")

print("*************************PERCENTIL*************************")
print("Percentil 80 de la Memoria interna: ", np.percentile(datos["internal memory"], 80))
print("Percentil 80 de la RAM: ", np.percentile(datos["RAM"], 80))
print("Percentil 80 del performance: ",np.percentile(datos["performance"], 80))
print("Percentil 80 de la camara principal: ",np.percentile(datos["main camera"], 80))
print("Percentil 80 de la camara frontal: ",np.percentile(datos["selfie camera"], 80))
print("Percentil 80 del tamaño de la bateria: ",np.percentile(datos["battery size"], 80))
print("Percentil 80 del tamaño de la pantalla: ",np.percentile(datos["screen size"], 80))
print("Percentil 80 del peso: ",np.percentile(datos["weight"], 80))
print("Percentil 80 del precio: ",np.percentile(datos["price"], 80),"\n")

print("*************************CUARTIL*************************")
print("Ultimo cuartil de la Memoria interna: ", np.quantile(datos["internal memory"], 0.75))
print("Ultimo cuartil de la RAM: ", np.quantile(datos["RAM"], 0.75))
print("Ultimo cuartil del performance: ",np.quantile(datos["performance"], 0.75))
print("Ultimo cuartil de la camara principal: ",np.quantile(datos["main camera"], 0.75))
print("Ultimo cuartil de la camara frontal: ",np.quantile(datos["selfie camera"], 0.75))
print("Ultimo cuartil del tamaño de la bateria: ",np.quantile(datos["battery size"], 0.75))
print("Ultimo cuartil del tamaño de la pantalla: ",np.quantile(datos["screen size"], 0.75))
print("Ultimo cuartil del peso: ",np.quantile(datos["weight"], 0.75))
print("Ultimo cuartil del precio: ",np.quantile(datos["price"], 0.75),"\n")

print("El último cuartil, o tercer cuartil (Q3), es el valor por debajo del cual se encuentra el 75% de los datos. En otras palabras, es el percentil 75.\n")
print("El percentil 80 es el valor por debajo del cual se encuentra el 80% de los datos.")

"""
*************************PERCENTIL*************************
204.8
8.0
8.49
50.0
27.2
5000.0
6.7
213.0
888.2
*************************CUARTIL*************************
128.0
8.0
7.94
50.0
16.0
5000.0
6.7
207.0
840.0
"""