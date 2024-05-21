# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:16:22 2024

@author: joswe
"""

miDataSet = open("cellphonesdata.csv", "r")
res=miDataSet.read();
array=res.split('\n');
v1=[]
v2=[]
v3=[]
v4=[]
v5=[]
v6=[]
v7=[]
v8=[]
v9=[]

for i in range(1, 34):
    x=array[i].split(",")

    v1.append(float(x[4]))
    v2.append(float(x[5]))
    v3.append(float(x[6]))
    v4.append(float(x[7]))
    v5.append(float(x[8]))
    v6.append(float(x[9]))
    v7.append(float(x[10]))
    v8.append(float(x[11]))
    v9.append(float(x[12]))
    
v1.sort()
v2.sort()
v3.sort()
v4.sort()
v5.sort()
v6.sort()
v7.sort()
v8.sort()
v9.sort()
total_N=len(array)-2

print("*************************PERCENTIL*************************")
percentil_n=80
indice_P=percentil_n*(total_N-1)/100
E=percentil_n*(total_N-1)//100
F=(percentil_n*(total_N-1)%100)/100

v11=float(v1[E])
v22=float(v1[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v2[E])
v22=float(v2[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v3[E])
v22=float(v3[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v4[E])
v22=float(v4[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v5[E])
v22=float(v5[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v6[E])
v22=float(v6[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v7[E])
v22=float(v7[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v8[E])
v22=float(v8[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v9[E])
v22=float(v9[E+1])
v=v11+(v22-v11)*F
print(v)

print("*************************CUARTIL*************************")
quartil_n=75
indice_P=quartil_n*(total_N-1)/100
E=quartil_n*(total_N-1)//100
F=(quartil_n*(total_N-1)%100)/100

v11=float(v1[E])
v22=float(v1[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v2[E])
v22=float(v2[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v3[E])
v22=float(v3[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v4[E])
v22=float(v4[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v5[E])
v22=float(v5[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v6[E])
v22=float(v6[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v7[E])
v22=float(v7[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v8[E])
v22=float(v8[E+1])
v=v11+(v22-v11)*F
print(v)

v11=float(v9[E])
v22=float(v9[E+1])
v=v11+(v22-v11)*F
print(v)
