# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:45:46 2021

@author: aeapo
"""

def get_weapon_infox(weapon,refinement):
    if weapon.lower()== 'black sword':
        weapon = {'base attack': 510,
                  'Main Stat':'Cr',
                  'Main Stat Bonus': 0.276,
                  'Refinement': 1,
                  'Passive':'NACA Bonus',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
        weapon['Passive Bonus']=weapon['Passive Bonus']+0.05*(refinement-1)
    elif weapon.lower() == "lion's roar" or weapon == 'lions roar':
         weapon = {'base attack': 510,
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.413,
                  'Refinement': 1,
                  'Passive':'Damage',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.04*(refinement-1)
    elif weapon.lower() == "wolf's gravestone" or weapon == 'wolfs gravestone':
         weapon = {'base attack': 608,
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.496,
                  'Refinement': 1,
                  'Passive':'Attack',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.05*(refinement-1)
    elif weapon.lower() == "deathmatch":
         weapon = {'base attack': 454,
                  'Main Stat':'Cr',
                  'Main Stat Bonus': 0.368,
                  'Refinement': 1,
                  'Passive':'Attack',
                  'Passive2':'None',
                  'Passive Bonus': 0.2}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.04*(refinement-1)
    elif weapon.lower() == "skyward atlas":
         weapon = {'base attack': 674,
                  'Main Stat':'Attack',
                  'Main Stat Bonus': 0.331,
                  'Refinement': 1,
                  'Passive':'Damage',
                  'Passive2':'None',
                  'Passive Bonus': 0.12}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.03*(refinement-1)
    elif weapon.lower() == "sacrificial sword":
         weapon = {'base attack': 454,
                  'Main Stat':'Er',
                  'Main Stat Bonus': 0.613,
                  'Refinement': 1,
                  'Passive':'None',
                  'Passive2':'None',
                  'Passive Bonus': 0}
         weapon['Passive Bonus']=weapon['Passive Bonus']+0.1*(refinement-1)
    elif weapon.lower() == "staff of homa":
         weapon = {'base attack': 608,
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
                  'Main Stat':'Cd',
                  'Main Stat Bonus': 0.469,
                  'Refinement': 1,
                  'Passive':'Cr',
                  'Passive2':'None',
                  'Passive2 Bonus':'none',
                  'Passive Bonus': 0.14}
        weapon['Passive Bonus']=weapon['Passive Bonus']+0.035*(refinement-1)
    else:
        print('Invalid Weapon Selection')
        return False
    return weapon