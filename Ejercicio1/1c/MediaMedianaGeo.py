# -*- coding: utf-8 -*-
"""
@author: joswe
"""
import numpy as np
import pandas as pd
import statistics
from scipy.stats import gmean
datos = pd.read_csv("mobile_phone_rating_rmv.csv", sep=",")


print("*************************MEDIA*************************")
print(" Media de la camara: ", np.mean(datos["camera"]))
print(" Media de la camara frontal: ", np.mean(datos["selfie"]))
print(" Media del audio: ",np.mean(datos["audio"]))
print(" Media del display: ",np.mean(datos["display"]))
print(" Media de la bateria: ",np.mean(datos["battery"]),"\n")


print("*************************MEDIANA*************************")
print(" Mediana de la camara: ", np.median(datos["camera"]))
print(" Mediana de la camara frontal: ", np.median(datos["selfie"]))
print(" Mediana del audio: ",np.median(datos["audio"]))
print(" Mediana del display: ",np.median(datos["display"] ))
print(" Mediana de la bateria: ",np.median(datos["battery"] ),"\n")

print("*************************MODA*************************")
print(" Moda de la marca de celular: ", statistics.mode(datos["model"]))
print(" Moda del precio: ", statistics.mode(datos["price"]))
print(" Moda del lanzamiento: ", statistics.mode(datos["launch"]))
print("Moda de la camara: ", statistics.mode(datos["camera"]))
print("Moda de la camara frontal: ", statistics.mode(datos["selfie"]))
print("Moda del audio: ",statistics.mode(datos["audio"]))
print("Moda del display: ",statistics.mode(datos["display"]))
print("Moda de la bateria: ",statistics.mode(datos["battery"]),"\n")

print("*************************MEDIA GEOMETRICA*************************")
print("Media Geometrica de la camara: ", gmean(datos["camera"]))
print("Media Geometrica del camara frontal: ",gmean(datos["selfie"]))
print("Media Geometrica del audio: ",gmean(datos["audio"]))
print("Media Geometrica del display: ",gmean(datos["display"]))
print("Media Geometrica de la bateria: ",gmean(datos["battery"]),"\n")

print("En un artículo científico, la elección de la medida de tendencia central depende del contexto de los datos:")
print("Media es útil para datos simétricos sin valores atípicos.")
print("Mediana es preferida para datos sesgados o con valores atípicos.")
print("Moda es adecuada para datos categóricos o para identificar el valor más frecuente.")
print("Media Geométrica es ideal para datos multiplicativos o cuando se trabaja con tasas de crecimiento.")
print("Cada medida tiene sus ventajas y desventajas, y la selección adecuada puede proporcionar una mejor interpretación y análisis de los datos en el contexto específico del estudio.")





















