# -*- coding: utf-8 -*-
"""
@author: joswe
"""

import numpy as np
from itertools import permutations

# Creamos un array con 8 nodos
nodos = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Generar todas las permutaciones
permutaciones = list(permutations(nodos))
permutaciones2 = np.array(permutaciones)

for i in permutaciones2[:100]:##mostramos los primeros 100 para no sobrecargar el programa
    print(i)
print("La cantidad de permutaciones son:",len(permutaciones2))


