# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:42:08 2021

@author: aeapo
"""

def check_epex(epe):
    check=False
    if epe =='pyro':
        check=True
    if epe =='cryo':
        check=True
    if epe =='electro':
        check=True
    if epe =='hydro':
        check=True
        print('Why would you ever run this?')
    if epe =='geo':
        check=True
    if check==False:
        print('Invalid Elemental Party Bonus Selection')
        print('Available choices are (pyro,cryo, electro, hydro, geo')
    return check