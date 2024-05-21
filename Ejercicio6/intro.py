# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:05:54 2024

@author: joswe
"""

import numpy as np

##Array normal
lista = [1,2,3,4,5,6]
print(lista)

##Array con la libreria numpy

##El np.array quita las comas al array lista
array21 = np.array(lista)
print(array21)
##El np.asarray quita las comas al array lista
array22 = np.asarray(lista)
print(array22)

##Para crear matrices con numpy

##El np.resize(array,(rows, columns)) es para crear una matriz con el array de n filas (rows) y m columnas(columns)
array23 =np.resize(lista, (2,3))
print(array23)

##Sumar una matriz con la ayuda de la libreria numpy
print(np.sum(array23))

##Sumar una matriz por columnas 
print(np.sum(array23, axis=0))
##Sumar una matriz por filas 
print(np.sum(array23, axis=1))

print("*************************MEDIA*************************")
##Hallar la media i1+i2+...+in/n (la media es el percentil 50)
print(np.mean(array23))

##Hallar la media por columna
print(np.mean(array23, axis=0))

##Hallar la media por filas
print(np.mean(array23, axis=1))

print("*************************MEDIANA*************************")
##Hallar la mediana (La mediana es el numero del medio)
##Si existe un nro par de numeros en el array, se agarra los dos numeros del medio dividido entre dos, esa es la mediana
print(np.median(array23))

##Hallar la media por columna
print(np.median(array23, axis=0))

##Hallar la media por filas
print(np.median(array23, axis=1))

print("*************************DESVIACION STANDAR*************************")
print(np.std(array23))

##Hallar la media por columna
print(np.std(array23, axis=0))

##Hallar la media por filas
print(np.std(array23, axis=1))

lista1=[3710, 3755, 3850, 3880, 3880, 3890, 3920, 3940, 3950, 4050, 4130, 4325]
print("*************************PERCENTILES*************************")

##Para la formula del percentil
"""
Cabe mencionar que empezamos desde la posicion cero en el array
n=percentil
N=cantidad de elementos
P=indice del percentil

P=(n*N-1)/100
E=La parte entera del percentil P
F=La parte fraccionaria del percentil P
V_1=La posicion E del array
V_2=La posicion E+1 del array

V=V_1+(V_2-V_1)*F

V=El valor porcentil
 
"""

## link de mi dataset https://www.kaggle.com/datasets/sazidthe1/global-inflation-data

print(np.percentile(array23, 50)) ##El percentil 50 es la media en todo caso
print(np.percentile(array23, 95)) ##El percentil 50 es la media en todo caso
print(np.percentile(lista1, 80)) ##El percentil 50 es la media en todo caso
print(np.quantile(lista1, 0.75))
print(np.percentile(lista1, 75))

print("*************************CUARTILES*************************")
##Para la formula del quartil 
"""
Q1=Primer cuartil
Q2=Segundo cuartil
Q3=Tercer cuartil
n=cantidad de elementos
Q=indice del Quartil

Q=(n)*(Q_i/4)

"""
##print(np.quantile(lista, 75))

