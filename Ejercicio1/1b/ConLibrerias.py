# -*- coding: utf-8 -*-
"""
@author: joswe
"""

import numpy as np
import pandas as pd
datos = pd.read_csv("mobile_phone_rating_rmv.csv", sep=",")

print("*************************PERCENTIL*************************")
print("Percentil 80: Este valor representa el punto debajo del cual se encuentra el 80% de los datos. Proporciona una medida similar al Q3, pero con un umbral ligeramente superior. Es útil para tener una idea más precisa de cómo se distribuyen los datos en el extremo superior.")
print("Percentil 80 de la camara: ", np.percentile(datos["camera"], 80))
print("Percentil 80 de selfie: ", np.percentile(datos["selfie"], 80))
print("Percentil 80 del audio: ", np.percentile(datos["audio"], 80))
print("Percentil 80 del display: ",np.percentile(datos["display"], 80))
print("Percentil 80 de la bateria: ",np.percentile(datos["battery"], 80),"\n")


print("*************************CUARTIL*************************")
print("Cuartil 3 (Q3 o percentil 75) Este valor representa el punto debajo del cual se encuentra el 75% de los datos. Es útil para entender la dispersión de la mayoría de los datos y detectar valores atípicos en la parte superior del conjunto de datos.\n")
print("Ultimo cuartil de la camara: ", np.quantile(datos["camera"], 0.75))
print("Ultimo cuartil de selfie: ", np.quantile(datos["selfie"], 0.75))
print("Ultimo cuartil del audio: ",np.quantile(datos["audio"], 0.75))
print("Ultimo cuartil del display: ",np.quantile(datos["display"], 0.75))
print("Ultimo cuartil de la bateria: ",np.quantile(datos["battery"], 0.75), "\n")

