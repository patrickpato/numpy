# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
L =[1, 2] 
def area(l, w):
    ans = l * w
    print (ans)
area (2, 3)
L1 = [2, 3]
print (L + L1)
L2 = []
# in tests weather the values exist in the lists.
# zip function adds the values of individual lists correspondingly.
for e, f, in zip (L, L1):
    print (e + f)
#CONVERTING TO ARRAYS
A1 = numpy.array (L)
print (A1)
A2 = numpy.array(L1)
print (A2)
print (A1 + A2)
print (L + L1)
a = [2, 4]
b = [4, 7]
D1 = numpy.array(a)
print (D1)
# SOLVING THE DOT PRODUCT OF VECTORS
A = numpy.array([1, 3])
B = numpy.array([2, 4])
dot = 0
for e, f in zip (A, B):
    dot+= e*f
    print (dot)
numpy.dot (A, B)

