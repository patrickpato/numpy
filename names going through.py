# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:04:01 2018

@author: Webster
"""

names = ["pato" , "jamo" , "domi" , "kama" , "dani" , "ezra" , "ruto"]
users = ["fred" , "izo" , "corneli" , "kithinji" , "dani" , "ruto" , "ezra"]
for user in users:
    if user in names:
        print (user.title() + "is taken, try another name")
    else:
        print (user.title() + "is available for use")
        
        