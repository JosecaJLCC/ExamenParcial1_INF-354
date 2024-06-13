# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:29:31 2024

@author: joswe
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()


datos = pd.read_csv("mobile_phone_rating_rmv.csv", sep=",")

miDataSet = open("mobile_phone_rating_rmv.csv", "r")

res=miDataSet.read();
precio=[]
lanza=[]
camara=[]
selfie=[]
audio=[]
display=[]
bateria=[]

array=res.split("\n")
for i in range (1, len(array)-2):
    x=array[i].split(",")
    precio.append(x[1])
    lanza.append(x[2])
    camara.append(x[3])
    selfie.append(x[4])
    audio.append(x[5])
    display.append(x[6])
    bateria.append(x[7])
    
sprecio=set(precio)
slanza=set(lanza)
scamara=set(camara)
sselfie=set(selfie)
saudio=set(audio)
sdisplay=set(display)
sbateria=set(bateria)

print(sprecio, "\n")
print(slanza, "\n")
print(scamara, "\n")
print(sselfie, "\n")
print(saudio, "\n")
print(sdisplay, "\n")
print(sbateria, "\n")


"""fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()"""