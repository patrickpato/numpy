# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:44:55 2018

@author: Webster
"""

import numpy
def density (mass, volume):
    ans = mass/volume
    print (ans)
density (56, 2)
def schwarzchild_radius (gravitationalconstant, massofthebody, speedoflight):
    radius = (gravitationalconstant  * massofthebody) / speedoflight
    print (radius)
schwarzchild_radius (6.67 * 10**-23, 5.98 * 10*24, 3*10*8)
