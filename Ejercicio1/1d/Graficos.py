# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:29:31 2024

@author: joswe
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()


datos = pd.read_csv("cellphonesdata.csv", sep=",")


miDataSet = open("cellphonesdata.csv", "r")
res=miDataSet.read();
array=res.split('\n');
array2=array[0].split(",")
fruits=[]
for i in range(4,12):
    fruits.append(array2[i])

print(fruits)
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()