# -*- coding: utf-8 -*-
"""
@author: joswe
"""

from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
x1=np.array([
     [-1,2,3],
     [4,0,5],
     [2,1,1]
     ])

prepro=KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
x2=prepro.fit_transform(x1)
print(x2)