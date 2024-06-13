# -*- coding: utf-8 -*-
"""
@author: joswe
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
datos = pd.read_csv("mobile_phone_rating.csv", sep=",")
prepro = SimpleImputer(missing_values=np.nan, strategy="mean")


selected_columns = datos[['selfie', 'audio','display', 'battery']]
matrix = selected_columns.values
x2=prepro.fit_transform(matrix)
print(x2)

