# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:32:16 2018

@author: Webster
"""
import numpy
import pandas as pd
A = pd.read_csv("data_1d.csv", header = None).as_matrix()
x = A[:, 0]
y = A[:, 1]
plt.scatter(x, y)
plt.show()
