# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:45:46 2021

@author: aeapo
"""

def get_weapon_infox(weapon,refinement):
    if weapon.lower()== 'black sword':
        weapon = {'base attack': 510,
                  'name':'black sword',
                  'Main Stat':'Cr',
                  'Main Stat Bonus': 0.276,
                  'Refinement': 1,
                  'Passive':'NACA Bonus',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
        weapon['Passive Bonus']=weapon['Passive Bonus']+0.05*(refinement-1)
    elif weapon.lower() == "lion's roar" or weapon == 'lions roar':
         weapon = {'base attack': 510,
                   'name': 'lions roar',
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.413,
                  'Refinement': 1,
                  'Passive':'Damage',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.04*(refinement-1)
    elif weapon.lower() == "wolf's gravestone" or weapon == 'wolfs gravestone':
         weapon = {'base attack': 608,
                   'name': 'wolfs gravestone',
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.496,
                  'Refinement': 1,
                  'Passive':'Attack',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.05*(refinement-1)
    elif weapon.lower() == "deathmatch":
         weapon = {'base attack': 454,
                   'name':'deathmatch',
                  'Main Stat':'Cr',
                  'Main Stat Bonus': 0.368,
                  'Refinement': 1,
                  'Passive':'Attack',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.04*(refinement-1)
    elif weapon.lower() == "skyward atlas":
         weapon = {'base attack': 674,
                  'name':'skyward atlas',
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.331,
                  'Refinement': 1,
                  'Passive':'Damage',
                  'Passive2':'None',
                  'Passive Bonus': 0.12}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.03*(refinement-1)
    elif weapon.lower() == "sacrificial sword":
         weapon = {'base attack': 454,
                   'name':'sacrificial sword',
                  'Main Stat':'Er',
                  'Main Stat Bonus': 0.613,
                  'Refinement': 1,
                  'Passive':'None',
                  'Passive2':'None',
                  'Passive Bonus': 0}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.1*(refinement-1)
    elif weapon.lower() == "staff of homa":
         weapon = {'base attack': 608,
                  'name':'staff of homa',
                  'Main Stat':'Cd',
                  'Main Stat Bonus': 0.662,
                  'Refinement': 1,
                  'Passive':'Hp',
                  'Passive2':'hp scaling',
                  'Passive Bonus': 0.2,
                  'hp conversion':0.018}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.05*(refinement-1)
         weapon['hp conversion']=weapon['hp conversion']+0.004*(refinement-1)
    elif weapon.lower()== 'harbinger of dawn':
        weapon = {'base attack': 401,
                  'name':'harbinger of dawn',
                  'Main Stat':'Cd',
                  'Main Stat Bonus': 0.469,
                  'Refinement': 1,
                  'Passive':'Cr',
                  'Passive2':'None',
                  'Passive Bonus 2':'none',
                  'Passive Bonus': 0.14}
        weapon['Passive Bonus']=weapon['Passive Bonus']+0.035*(refinement-1)
    elif weapon.lower()== 'engulfing lightning':
        weapon = {'base attack': 608,
                  'name':'engulfing lightning',
                  'Main Stat':'Er',
                  'Main Stat Bonus': 0.559,
                  'Refinement': 1,
                  'Passive':'none',
                  'Passive2':'Er',
                  'Passive Bonus 2':0.3,
                  'Passive Bonus': 0.28}
        weapon['Passive Bonus']=weapon['Passive Bonus']+0.07*(refinement-1)
        weapon['Passive Bonus 2']=weapon['Passive Bonus 2']+0.05*(refinement-1)
    else:
        print('Invalid Weapon Selection')
        return False
    return weapon