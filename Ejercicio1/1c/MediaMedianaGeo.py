# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:17:52 2024

@author: joswe
"""

import numpy as np
import pandas as pd
import statistics
from scipy.stats import gmean
datos = pd.read_csv("cellphonesdata.csv", sep=",")

"""
Media: 6.787878787878788
Mediana: 8
Moda: 8
Media Geométrica: 6.242419463393983
"""

print("*************************MEDIA*************************")
print(" Media de la Memoria Interna: ", np.mean(datos["internal memory"]))
print(" Media de la RAM: ", np.mean(datos["RAM"]))
print(" Media del performance: ",np.mean(datos["performance"]))
print(" Media de la camara principal: ",np.mean(datos["main camera"]))
print(" Media de la camara frontal: ",np.mean(datos["selfie camera"]))
print(" Media del tamaño de la bateria: ",np.mean(datos["battery size"]))
print(" Media del tamaño de la pantalla: ",np.mean(datos["screen size"]))
print(" Media del peso: ",np.mean(datos["weight"]))
print(" Media del precio: ",np.mean(datos["price"]),"\n")


print("*************************MEDIANA*************************")
print(" Mediana de la Memoria Interna: ", np.median(datos["internal memory"]))
print(" Mediana de la RAM: ", np.median(datos["RAM"]))
print(" Mediana del performance: ",np.median(datos["performance"]))
print(" Mediana de la camara principal: ",np.median(datos["main camera"] ))
print(" Mediana de la camara frontal: ",np.median(datos["selfie camera"] ))
print(" Mediana del tamaño de la bateria: ",np.median(datos["battery size"] ))
print(" Mediana del tamaño de la pantalla: ",np.median(datos["screen size"] ))
print(" Mediana del peso: ",np.median(datos["weight"] ))
print(" Mediana del precio: ",np.median(datos["price"] ),"\n")

print("*************************MODA*************************")
print(" Moda de la marca de celular: ", statistics.mode(datos["brand"]))
print(" Moda del modelo: ", statistics.mode(datos["model"]))
print(" Moda del SO: ", statistics.mode(datos["operating system"]))
print("Moda de la Memoria Interna: ", statistics.mode(datos["internal memory"]))
print("Moda de la RAM: ", statistics.mode(datos["RAM"]))
print("Moda del performance: ",statistics.mode(datos["performance"]))
print("Moda de la camara principal: ",statistics.mode(datos["main camera"]))
print("Moda de la camara frontal: ",statistics.mode(datos["selfie camera"]))
print("Moda del tamaño de la bateria: ",statistics.mode(datos["battery size"]))
print("Moda del tamaño de la pantalla: ",statistics.mode(datos["screen size"]))
print("Moda del peso: ",statistics.mode(datos["weight"]))
print("Moda del precio: ",statistics.mode(datos["price"]),"\n")

print("*************************MEDIA GEOMETRICA*************************")
print("Media Geometrica de la RAM: ", gmean(datos["RAM"]))
print("Media Geometrica del performance: ",gmean(datos["performance"]))
print("Media Geometrica de la camara principal: ",gmean(datos["main camera"]))
print("Media Geometrica de la camara frontal: ",gmean(datos["selfie camera"]))
print("Media Geometrica del tamaño de la bateria: ",gmean(datos["battery size"]))
print("Media Geometrica del tamaño de la pantalla: ",gmean(datos["screen size"]))
print("Media Geometrica del peso: ",gmean(datos["weight"]))
print("Media Geometrica del precio: ",gmean(datos["price"]),"\n")

print("En un artículo científico, la elección de la medida de tendencia central depende del contexto de los datos:")
print("Media es útil para datos simétricos sin valores atípicos.")
print("Mediana es preferida para datos sesgados o con valores atípicos.")
print("Moda es adecuada para datos categóricos o para identificar el valor más frecuente.")
print("Media Geométrica es ideal para datos multiplicativos o cuando se trabaja con tasas de crecimiento.")
print("Cada medida tiene sus ventajas y desventajas, y la selección adecuada puede proporcionar una mejor interpretación y análisis de los datos en el contexto específico del estudio.")





















