# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:15:04 2020

@author: Prateek Sohlot
"""
while True:    
    
    a = input().split()
    
    if len(a) == 1:
        break
    
    a = map(float, a)
    x1, y1, x2, y2, p = a
       
    print("%.8f" % (1/p).__rpow__(abs(x1-x2)**p + abs(y1-y2)**p))
    
