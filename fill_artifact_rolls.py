# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:01:13 2021

@author: aeapo
"""
from check_possibility import check_possibilityx
import copy
def fill_artifact_rollsx(artifact,n_roll):
    x=False
    if artifact['flower']['rolls']<9:
        artifact2=copy.deepcopy(artifact)
        if n_roll == 'hp' and artifact['flower']['hp']<6:
            artifact['flower']['hp']+=1
            x=True
        elif n_roll == 'df' and artifact['flower']['df']<6:
            artifact['flower']['df']+=1
            x=True
        elif n_roll == 'attack' and artifact['flower']['attack']<6:
            artifact['flower']['attack']+=1
            x=True
        elif n_roll == 'er' and artifact['flower']['er']<6:
            artifact['flower']['er']+=1
            x=True
        elif n_roll == 'em' and artifact['flower']['em']<6:
            artifact['flower']['em']+=1
            x=True
        elif n_roll == 'cr' and artifact['flower']['cr']<6:
            artifact['flower']['cr']+=1
            x=True
        elif n_roll == 'cd' and artifact['flower']['cd']<6:
            artifact['flower']['cd']+=1
            x=True
        y=check_possibilityx(artifact['flower'])
        if not y:
            x=False
            artifact=copy.deepcopy(artifact2)
        
    if x:
        artifact['flower']['rolls']=(artifact['flower']['hp']+artifact['flower']['df']+artifact['flower']['attack']+artifact['flower']['er']+artifact['flower']['em']+artifact['flower']['cr']+artifact['flower']['cd'])
        return artifact
    else:
        if artifact['feather']['rolls']<9:
            artifact2=copy.deepcopy(artifact)
            if n_roll == 'hp' and artifact['feather']['hp']<6:
                artifact['feather']['hp']+=1
                x=True
            elif n_roll == 'df' and artifact['feather']['df']<6:
                artifact['feather']['df']+=1
                x=True
            elif n_roll == 'attack' and artifact['feather']['attack']<6:
                artifact['feather']['attack']+=1
                x=True
            elif n_roll == 'er' and artifact['feather']['er']<6:
                artifact['feather']['er']+=1
                x=True
            elif n_roll == 'em' and artifact['feather']['em']<6:
                artifact['feather']['em']+=1
                x=True
            elif n_roll == 'cr' and artifact['feather']['cr']<6:
                artifact['feather']['cr']+=1
                x=True
            elif n_roll == 'cd' and artifact['feather']['cd']<6:
                artifact['feather']['cd']+=1
                x=True
            y=check_possibilityx(artifact['feather'])
            if not y:
                x=False
                artifact=copy.deepcopy(artifact2)
            
    if x:
        artifact['feather']['rolls']=(artifact['feather']['hp']+artifact['feather']['df']+artifact['feather']['attack']+artifact['feather']['er']+artifact['feather']['em']+artifact['feather']['cr']+artifact['feather']['cd'])
        return artifact
    else:
        if artifact['sands_type']=='attack':
            if artifact['sands']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['sands']['hp']<6:
                    artifact['sands']['hp']+=1
                    x=True
                elif n_roll == 'df' and artifact['sands']['df']<6:
                    artifact['sands']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['sands']['er']<6:
                    artifact['sands']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['sands']['em']<6:
                    artifact['sands']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['sands']['cr']<6:
                    artifact['sands']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['sands']['cd']<6:
                    artifact['sands']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['sands'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['sands']['rolls']=(artifact['sands']['hp']+artifact['sands']['df']+artifact['sands']['attack']+artifact['sands']['er']+artifact['sands']['em']+artifact['sands']['cr']+artifact['sands']['cd'])
        return artifact
    else:
        if artifact['sands_type']=='hp':
            if artifact['sands']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'attack' and artifact['sands']['attack']<6:
                    artifact['sands']['attack']+=1
                    x=True
                elif n_roll == 'df' and artifact['sands']['df']<6:
                    artifact['sands']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['sands']['er']<6:
                    artifact['sands']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['sands']['em']<6:
                    artifact['sands']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['sands']['cr']<6:
                    artifact['sands']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['sands']['cd']<6:
                    artifact['sands']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['sands'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['sands']['rolls']=(artifact['sands']['hp']+artifact['sands']['df']+artifact['sands']['attack']+artifact['sands']['er']+artifact['sands']['em']+artifact['sands']['cr']+artifact['sands']['cd'])
        return artifact
    else:
        if artifact['sands_type']=='df':
            if artifact['sands']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['sands']['hp']<6:
                    artifact['sands']['hp']+=1
                    x=True
                elif n_roll == 'attack' and artifact['sands']['attack']<6:
                    artifact['sands']['attack']+=1
                    x=True
                elif n_roll == 'er' and artifact['sands']['er']<6:
                    artifact['sands']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['sands']['em']<6:
                    artifact['sands']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['sands']['cr']<6:
                    artifact['sands']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['sands']['cd']<6:
                    artifact['sands']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['sands'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['sands']['rolls']=(artifact['sands']['hp']+artifact['sands']['df']+artifact['sands']['attack']+artifact['sands']['er']+artifact['sands']['em']+artifact['sands']['cr']+artifact['sands']['cd'])
        return artifact
    else:
        if artifact['sands_type']=='er':
            if artifact['sands']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['sands']['hp']<6:
                    artifact['sands']['hp']+=1
                    x=True
                elif n_roll == 'df' and artifact['sands']['df']<6:
                    artifact['sands']['df']+=1
                    x=True
                elif n_roll == 'attack' and artifact['sands']['attack']<6:
                    artifact['sands']['attack']+=1
                    x=True
                elif n_roll == 'em' and artifact['sands']['em']<6:
                    artifact['sands']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['sands']['cr']<6:
                    artifact['sands']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['sands']['cd']<6:
                    artifact['sands']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['sands'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['sands']['rolls']=(artifact['sands']['hp']+artifact['sands']['df']+artifact['sands']['attack']+artifact['sands']['er']+artifact['sands']['em']+artifact['sands']['cr']+artifact['sands']['cd'])
        return artifact
    else:
        if artifact['sands_type']=='em':
            if artifact['sands']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['sands']['hp']<6:
                    artifact['sands']['hp']+=1
                    x=True
                elif n_roll == 'df' and artifact['sands']['df']<6:
                    artifact['sands']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['sands']['er']<6:
                    artifact['sands']['er']+=1
                    x=True
                elif n_roll == 'attack' and artifact['sands']['attack']<6:
                    artifact['sands']['attack']+=1
                    x=True
                elif n_roll == 'cr' and artifact['sands']['cr']<6:
                    artifact['sands']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['sands']['cd']<6:
                    artifact['sands']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['sands'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
    if x:
        artifact['sands']['rolls']=(artifact['sands']['hp']+artifact['sands']['df']+artifact['sands']['attack']+artifact['sands']['er']+artifact['sands']['em']+artifact['sands']['cr']+artifact['sands']['cd'])
        return artifact
    else:
        if artifact['goblet_type']=='attack':
            if artifact['goblet']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['goblet']['hp']<6:
                    artifact['goblet']['hp']+=1
                    x=True
                elif n_roll == 'df' and artifact['goblet']['df']<6:
                    artifact['goblet']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['goblet']['er']<6:
                    artifact['goblet']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['goblet']['em']<6:
                    artifact['goblet']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['goblet']['cr']<6:
                    artifact['goblet']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['goblet']['cd']<6:
                    artifact['goblet']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['goblet'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
            
    if x:
        artifact['goblet']['rolls']=(artifact['goblet']['hp']+artifact['goblet']['df']+artifact['goblet']['attack']+artifact['goblet']['er']+artifact['goblet']['em']+artifact['goblet']['cr']+artifact['goblet']['cd'])
        return artifact
    else:
        if artifact['goblet_type']=='damage':
            if artifact['goblet']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['goblet']['hp']<6:
                    artifact['goblet']['hp']+=1
                    x=True
                elif n_roll == 'attack' and artifact['goblet']['attack']<6:
                    artifact['goblet']['attack']+=1
                    x=True
                elif n_roll == 'df' and artifact['goblet']['df']<6:
                    artifact['goblet']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['goblet']['er']<6:
                    artifact['goblet']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['goblet']['em']<6:
                    artifact['goblet']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['goblet']['cr']<6:
                    artifact['goblet']['cr']+=1
                    x=True
                elif n_roll == 'cd' and artifact['goblet']['cd']<6:
                    artifact['goblet']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['goblet'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)            
    if x:
        artifact['goblet']['rolls']=(artifact['goblet']['hp']+artifact['goblet']['df']+artifact['goblet']['attack']+artifact['goblet']['er']+artifact['goblet']['em']+artifact['goblet']['cr']+artifact['goblet']['cd'])
        #print(y,artifact['goblet'])
        return artifact
    else:
        if artifact['circlet_type']=='crit rate':
            if artifact['circlet']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['circlet']['hp']<6:
                    artifact['circlet']['hp']+=1
                    x=True
                elif n_roll == 'attack' and artifact['circlet']['attack']<6:
                    artifact['circlet']['attack']+=1
                    x=True
                elif n_roll == 'df' and artifact['circlet']['df']<6:
                    artifact['circlet']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['circlet']['er']<6:
                    artifact['circlet']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['circlet']['em']<6:
                    artifact['circlet']['em']+=1
                    x=True
                elif n_roll == 'cd' and artifact['circlet']['cd']<6:
                    artifact['circlet']['cd']+=1
                    x=True
                y=check_possibilityx(artifact['circlet'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['circlet']['rolls']=(artifact['circlet']['hp']+artifact['circlet']['df']+artifact['circlet']['attack']+artifact['circlet']['er']+artifact['circlet']['em']+artifact['circlet']['cr']+artifact['circlet']['cd'])
        return artifact
    else:
        if artifact['circlet_type']=='crit damage':
            if artifact['circlet']['rolls']<9:
                artifact2=copy.deepcopy(artifact)
                if n_roll == 'hp' and artifact['circlet']['hp']<6:
                    artifact['circlet']['hp']+=1
                    x=True
                elif n_roll == 'attack' and artifact['circlet']['attack']<6:
                    artifact['circlet']['attack']+=1
                    x=True
                elif n_roll == 'df' and artifact['circlet']['df']<6:
                    artifact['circlet']['df']+=1
                    x=True
                elif n_roll == 'er' and artifact['circlet']['er']<6:
                    artifact['circlet']['er']+=1
                    x=True
                elif n_roll == 'em' and artifact['circlet']['em']<6:
                    artifact['circlet']['em']+=1
                    x=True
                elif n_roll == 'cr' and artifact['circlet']['cr']<6:
                    artifact['circlet']['cr']+=1
                    x=True
                y=check_possibilityx(artifact['circlet'])
                if not y:
                    x=False
                    artifact=copy.deepcopy(artifact2)
                
    if x:
        artifact['circlet']['rolls']=(artifact['circlet']['hp']+artifact['circlet']['df']+artifact['circlet']['attack']+artifact['circlet']['er']+artifact['circlet']['em']+artifact['circlet']['cr']+artifact['circlet']['cd'])
        return artifact
    else:
        return False
                