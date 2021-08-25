# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:08:43 2021

@author: aeapo
"""

def convert_artix(arti):
    attack=5.8
    em=23
    er=6.5
    hp=5.83
    df=7.29
    cr=3.9
    cd=7.8
    artif={}
    
    if arti['hp']!=0:
        artif['hp']=arti['hp']*hp
        
    if arti['df']!=0:
        artif['df']=arti['df']*df
        
    if arti['attack']!=0:
        artif['attack']=arti['attack']*attack
        
    if arti['er']!=0:
        artif['er']=arti['er']*er
        
    if arti['em']!=0:
        artif['em']=arti['em']*em
        
    if arti['cr']!=0:
        artif['cr']=arti['cr']*cr
        
    if arti['cd']!=0:
        artif['cd']=arti['cd']*cd
    return artif