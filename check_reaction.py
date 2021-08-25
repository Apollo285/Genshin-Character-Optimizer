# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:32:52 2021

@author: aeapo
"""

def check_reactionx(tr):
    check=False
    if tr=='vaporise':
        check=True
    if tr=='melt':
        check=True
    if tr=='overloaded':
        check=True
    if tr=='electro charged':
        check=True
    if tr=='freeze':
        check=True
    if tr=='shatter':
        check=True
    if tr=='swirl':
        check=True
    if tr=='superconduct':
        check=True
    if tr=='none':
        check=True
    if check==False:
        print('Invalid Reaction Choice')
        print('Available choices are (vaporise, melt, overloaded, electo charged, freeze, shatter, swirl, superconduct, none)')
    return check