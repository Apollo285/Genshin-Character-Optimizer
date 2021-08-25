# -*- coding: utf-8 -*-
"""
Created on Sun Aug 33 10:39:37 3021

@author: aeapo
"""

def check_possibilityx(artifact):
    if artifact['hp']==6:
        if artifact['attack']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
            return False
    if artifact['attack']==6:
        if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
            return False
    if artifact['er']==6:
        if artifact['attack']>1 or artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
            return False
    if artifact['em']==6:
        if artifact['attack']>1 or artifact['er']>1 or artifact['hp']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
            return False
    if artifact['df']==6:
        if artifact['attack']>1 or artifact['er']>1 or artifact['hp']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
            return False
    if artifact['cr']==6:
        if artifact['attack']>1 or artifact['er']>1 or artifact['hp']>1 or artifact['df']>1 or artifact['em']>1 or artifact['cd']>1:
            return False
    if artifact['cd']==6:
        if artifact['attack']>1 or artifact['er']>1 or artifact['hp']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['em']>1:
            return False
 ## Now check 5       
    if artifact['hp']==5:
        if artifact['attack']>2 or artifact['er']>2 or artifact['em']>2 or artifact['df']>2 or artifact['cr']>2 or artifact['cd']>2:
            return False
        if artifact['attack']==2:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==2:
            if artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==2:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==2:
            if artifact['attack']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==2:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['em']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['em']>1:
                return False
            
    if artifact['attack']==5:
        if artifact['hp']>2 or artifact['er']>2 or artifact['em']>2 or artifact['df']>2 or artifact['cr']>2 or artifact['cd']>2:
            return False
        if artifact['hp']==2:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==2:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['er']==5:
        if artifact['attack']>2 or artifact['hp']>2 or artifact['em']>2 or artifact['df']>2 or artifact['cr']>2 or artifact['cd']>2:
            return False
        if artifact['hp']==2:
            if artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==2:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==2:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==2:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==2:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
           if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['em']==5:
        if artifact['attack']>2 or artifact['er']>2 or artifact['hp']>2 or artifact['df']>2 or artifact['cr']>2 or artifact['cd']>2:
            return False
        if artifact['hp']==2:
            if artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==2:
           if artifact['hp']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
           if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['df']==5:
        if artifact['attack']>2 or artifact['er']>2 or artifact['hp']>2 or artifact['em']>2 or artifact['cr']>2 or artifact['cd']>2:
            return False
        if artifact['hp']==2:
            if artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==2:
           if artifact['hp']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False

    if artifact['cr']==5:
        if artifact['attack']>2 or artifact['er']>2 or artifact['hp']>2 or artifact['df']>2 or artifact['em']>2 or artifact['cd']>2:
            return False
        if artifact['hp']==2:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['er']==2:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['em']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['df']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==2:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1:
                return False
    if artifact['cd']==5:
        if artifact['attack']>2 or artifact['er']>2 or artifact['hp']>2 or artifact['df']>2 or artifact['cr']>2 or artifact['em']>2:
            return False
        if artifact['hp']==2:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['er']==2:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['em']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['df']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['attack']==2:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
        if artifact['cr']==2:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1:
                return False

## Now check 4
    if artifact['hp']==4:
        if artifact['attack']>3 or artifact['er']>3 or artifact['em']>3 or artifact['df']>3 or artifact['cr']>3 or artifact['cd']>3:
            return False
        if artifact['attack']==3:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==3:
            if artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==3:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==3:
            if artifact['attack']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==3:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['em']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
            if artifact['attack']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['em']>1:
                return False
            
    if artifact['attack']==4:
        if artifact['hp']>3 or artifact['er']>3 or artifact['em']>3 or artifact['df']>3 or artifact['cr']>3 or artifact['cd']>3:
            return False
        if artifact['hp']==3:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==3:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['er']==4:
        if artifact['attack']>3 or artifact['hp']>3 or artifact['em']>3 or artifact['df']>3 or artifact['cr']>3 or artifact['cd']>3:
            return False
        if artifact['hp']==3:
            if artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==3:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==3:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==3:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==3:
            if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
           if artifact['hp']>1 or artifact['attack']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['em']==4:
        if artifact['attack']>3 or artifact['er']>3 or artifact['hp']>3 or artifact['df']>3 or artifact['cr']>3 or artifact['cd']>3:
            return False
        if artifact['hp']==3:
            if artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==3:
           if artifact['hp']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['df']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
           if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
            
    if artifact['df']==4:
        if artifact['attack']>3 or artifact['er']>3 or artifact['hp']>3 or artifact['em']>3 or artifact['cr']>3 or artifact['cd']>3:
            return False
        if artifact['hp']==3:
            if artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['er']==3:
           if artifact['hp']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['em']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['attack']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['cr']>1 or artifact['cd']>1:
                return False
        if artifact['cr']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False

    if artifact['cr']==4:
        if artifact['attack']>3 or artifact['er']>3 or artifact['hp']>3 or artifact['df']>3 or artifact['em']>3 or artifact['cd']>3:
            return False
        if artifact['hp']==3:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['er']==3:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['em']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['df']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cd']>1:
                return False
        if artifact['attack']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cd']>1:
                return False
        if artifact['cd']==3:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1:
                return False
            
    if artifact['cd']==4:
        if artifact['attack']>3 or artifact['er']>3 or artifact['hp']>3 or artifact['df']>3 or artifact['attack']>3 or artifact['em']>3:
            return False
        if artifact['hp']==3:
            if artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['er']==3:
           if artifact['hp']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['em']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['df']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['df']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['attack']>1 or artifact['cr']>1:
                return False
        if artifact['attack']==3:
            if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['cr']>1:
                return False
        if artifact['cr']==3:
           if artifact['hp']>1 or artifact['er']>1 or artifact['em']>1 or artifact['df']>1 or artifact['attack']>1:
                return False
#Now check for 3-3-3
    if artifact['hp']==3:
        if artifact['attack']==3:
            if artifact['er']==3 or artifact['em']==3 or artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['er']==3:
            if artifact['em']==3 or artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['em']==3:
            if artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['df']==3:
            if artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['cr']==3:
            if artifact['cd']==3:
                return False
            
    if artifact['attack']==3:
        if artifact['er']==3:
            if artifact['em']==3 or artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['em']==3:
            if artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['df']==3:
            if artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['cr']==3:
            if artifact['cd']==3:
                return False
        
    if artifact['er']==3:
        if artifact['em']==3:
            if artifact['df']==3 or artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['df']==3:
            if artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['cr']==3:
            if artifact['cd']==3:
                return False
            
    if artifact['em']==3:
        if artifact['df']==3:
            if artifact['cr']==3 or artifact['cd']==3:
                return False
        if artifact['cr']==3:
            if artifact['cd']==3:
                return False
            
    if artifact['df']==3:
        if artifact['cr']==3:
            if artifact['cd']==3:
                return False
    return True