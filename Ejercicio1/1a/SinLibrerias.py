# -*- coding: utf-8 -*-
"""
@author: joswe
"""

miDataSet = open("mobile_phone_rating_rmv.csv", "r")
res=miDataSet.read();
array=res.split('\n');
v1=[]
v2=[]
v3=[]
v4=[]
v5=[]

print(len(array))
for i in range(1, len(array)-1):
    ##print(i, array[i])
    x=array[i].split(",")

    v1.append(float(x[3]))
    v2.append(float(x[4]))
    v3.append(float(x[5]))
    v4.append(float(x[6]))
    v5.append(float(x[7]))
    
v1.sort()
v2.sort()
v3.sort()
v4.sort()
v5.sort()

total_N=len(array)-2

print("*************************PERCENTIL*************************")

print("Percentil 80: Este valor representa el punto debajo del cual se encuentra el 80% de los datos. Proporciona una medida similar al Q3, pero con un umbral ligeramente superior. Es útil para tener una idea más precisa de cómo se distribuyen los datos en el extremo superior.")
percentil_n=80
indice_P=percentil_n*(total_N-1)/100
E=percentil_n*(total_N-1)//100
F=(percentil_n*(total_N-1)%100)/100

v11=float(v1[E])
v22=float(v1[E+1])
v=v11+(v22-v11)*F
print("Percentil 80 de la camara: ", v)

v11=float(v2[E])
v22=float(v2[E+1])
v=v11+(v22-v11)*F
print("Percentil 80 de selfie: ", v)

v11=float(v3[E])
v22=float(v3[E+1])
v=v11+(v22-v11)*F
print("Percentil 80 del audio: ", v)

v11=float(v4[E])
v22=float(v4[E+1])
v=v11+(v22-v11)*F
print("Percentil 80 del display: ",v)

v11=float(v5[E])
v22=float(v5[E+1])
v=v11+(v22-v11)*F
print("Percentil 80 de la bateria: ",v)


print("*************************CUARTIL*************************")
print("Cuartil 3 (Q3 o percentil 75) Este valor representa el punto debajo del cual se encuentra el 75% de los datos. Es útil para entender la dispersión de la mayoría de los datos y detectar valores atípicos en la parte superior del conjunto de datos.\n")
quartil_n=75
indice_P=quartil_n*(total_N-1)/100
E=quartil_n*(total_N-1)//100
F=(quartil_n*(total_N-1)%100)/100

v11=float(v1[E])
v22=float(v1[E+1])
v=v11+(v22-v11)*F
print("Ultimo cuartil de la camara: ", v)

v11=float(v2[E])
v22=float(v2[E+1])
v=v11+(v22-v11)*F
print("Ultimo cuartil de selfie: ", v)

v11=float(v3[E])
v22=float(v3[E+1])
v=v11+(v22-v11)*F
print("Ultimo cuartil del audio: ", v)

v11=float(v4[E])
v22=float(v4[E+1])
v=v11+(v22-v11)*F
print("Ultimo cuartil del display: ", v)

v11=float(v5[E])
v22=float(v5[E+1])
v=v11+(v22-v11)*F
print("Ultimo cuartil de la bateria: ", v)


"""
*************************PERCENTIL*************************
Percentil 80 de la camara:  119.60000000000002
Percentil 80 de selfie:  87.069444
Percentil 80 del audio:  66.60000000000002
Percentil 80 del display:  82.375
Percentil 80 de la bateria:  74.351852 

*************************CUARTIL*************************
Ultimo cuartil de la Memoria interna:  117.0
Ultimo cuartil de la RAM:  87.069444
Ultimo cuartil del performance:  65.7258065
Ultimo cuartil de la camara principal:  82.375
Ultimo cuartil de la camara frontal:  74.351852 
"""

