# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:51:15 2021

@author: aeapo
"""

def get_character_infox(character):
    if character == 'keqing':
        info={'element':'electo',
          'E':4,
          'NA': 0.81,
          'CA': 3.2,
          'Q':7.41,
          'E_cd':7,
          'Q_cd':12,
          'Q_cost': 40,
          'base attack':323,
          'base defense':799,
          'base hp': 13103,
          'D_bonus':0,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0.384,
          'Cr_bonus': 0.1,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'1211',
          'MDPS':'1411',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'def scaling': False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'name':'Keqing',
          'pronoun':'her'}
    elif character == 'hu tao':
        info={'element':'pyro',
          'E':1.15,
          'NA': 0.85,
          'CA': 2.42,
          'Q':6.1744,
          'E_cd':16,
          'Q_cd':15,
          'Q_cost': 60,
          'base attack':106,
          'base defense':876,
          'base hp': 15552,
          'D_bonus':0.33,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0.384,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'1211',
          'MDPS':'1411',
          'level':90,
          'hp scaling': True,
          'er scaling': False,
          'def scaling':False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'hp conversion':0.0626,
          'name': 'Hu Tao',
          'pronoun':'her'}
    elif character == 'ayaka':
        info={'element':'cryo',
          'E':4.3,
          'NA': 0.9,
          'CA': 3.27,
          'Q':40.428,
          'E_cd':7,
          'Q_cd':20,
          'Q_cost': 80,
          'base attack':342,
          'base defense':799,
          'base hp': 13103,
          'D_bonus':0.18,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0.384,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'1211',
          'MDPS':'1411',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'em scaling': False,
          'def scaling':False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'name': 'Ayaka',
          'pronoun':'her'}
    elif character == 'eula':
        info={'element':'physical',
          'E':0.5,
          'NA': 1.128*2,
          'CA': 2.42,
          'Q':14.8,
          'E_cd':16,
          'Q_cd':15,
          'Q_cost': 60,
          'base attack':342,
          'base defense':751,
          'base hp': 13226,
          'D_bonus':0,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0.384,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'3011',
          'MDPS':'5011',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'def scaling':False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'name': 'Eula',
          'pronoun':'her'}
    elif character == 'mona':
        info={'element':'hydro',
          'E':3.5,
          'NA': 0.67,
          'CA': 2.42,
          'Q':7.96,
          'E_cd':12,
          'Q_cd':15,
          'Q_cost': 60,
          'base attack':287,
          'base defense':653,
          'base hp': 10409,
          'D_bonus':0,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0.32,
          'Cd_bonus': 0,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'1011',
          'MDPS':'3311',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'def scaling':False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': True,
          'def d scaling':False,
          'em d scaling': False,
          'er d conversion':0.2,
          'name': 'Mona',
          'pronoun':'her'}
    elif character == 'xingqui':
        info={'element':'hydro',
          'E':6.45,
          'NA': 0.9,
          'CA': 2.02,
          'Q':34.195,
          'E_cd':21,
          'Q_cd':20,
          'Q_cost': 80,
          'base attack':202,
          'base defense':758,
          'base hp': 10222,
          'D_bonus':0.2,
          'Att_bonus':0.24,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'0021',
          'MDPS':'2221',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'def scaling':False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'name': 'Xingqui',
          'pronoun':'his'}
    elif character == 'zhongli':
        info={'element':'geo',
          'E':2.5,
          'NA': 0.75,
          'CA': 2.2,
          'Q':9,
          'E_cd':12,
          'Q_cd':12,
          'Q_cost': 40,
          'base attack':251,
          'base defense':738,
          'base hp': 14695,
          'D_bonus':0.288,
          'Att_bonus':0,
          'Em_bonus':0,
          'Er_bonus': 0,
          'Cd_bonus': 0,
          'Cr_bonus': 0,
          'Hp_bonus': 0,
          'Def_bonus':0,
          'QS':'1011',
          'MDPS':'4111',
          'level':90,
          'hp scaling': False,
          'er scaling': False,
          'def scaling':False,
          'em scaling': False,
          'hp d scaling': False,
          'er d scaling': False,
          'def d scaling':False,
          'em d scaling': False,
          'hp bonus_damage':True,
          'naca hp bonus':0.0139,
          'e hp bonus': 0.019,
          'q hp bonus': 0.33,
          'name': 'Zhongli',
          'pronoun':'his'}
    else:
        print('Invalid Character Selection')
        return False
    return info
    