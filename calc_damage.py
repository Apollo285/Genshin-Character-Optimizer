# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:56:58 2021

@author: aeapo
"""
def calc_damagex(character,weapon, artifacts,epe):
    attack = artifacts['attack']+character['Att_bonus']
    em = artifacts['em']+character['Em_bonus']
    er = artifacts['er']+character['Er_bonus']
    cr = artifacts['cr']+character['Cr_bonus']
    cd = artifacts['cd']+character['Cd_bonus']
    hp = artifacts['hp']+character['Hp_bonus']
    df =  artifacts['df']+character['Def_bonus']
    db = artifacts['db']+character['D_bonus']
    tba = character['base attack']+weapon['base attack']
    tdf=character['base defense']*(1+df)
    thp=(1+hp)*character['base hp']+4780
    geo_damage_boost=0
    electro_particle_boost=0
    if epe['epe']=='geo':
        geo_damage_boost=0.15
    elif epe['epe']=='electro':
        electro_particle_boost=0.5
    elif epe['epe2']=='geo':
        geo_damage_boost=0.15
    elif epe['epe2']=='electro':
        electro_particle_boost=0.5
    ta=tba*(1+attack)+311
    hp_conversion = 0
    er_conversion = 0
    def_conversion = 0
    em_conversion = 0
    hp_d_conversion = 0
    er_d_conversion = 0
    def_d_conversion = 0
    em_d_conversion = 0
    if character['bennett_boost']:
        if character['name']!='bennett':
            ta+=950*(character['bennett_er']/200)
        else:
            if er>1:
                ta+=950
            else:
                ta+=950*(1+er)/2
    # Check for weird scaling
    if character['hp scaling']==True:
        hp_conversion+=(character['hp conversion'])
    if character['er scaling']==True:
        er_conversion+=(character['er conversion'])
    if character['def scaling']==True:
        def_conversion+=(character['def conversion'])
    if character['em scaling']==True:
        em_conversion+=(character['em conversion'])

    if weapon['Passive']=='hp scaling':
        hp_conversion+=(weapon['hp conversion'])
    if weapon['Passive']=='er scaling':
        er_conversion+=(weapon['er conversion'])
    if weapon['Passive']=='def scaling':
        def_conversion+=(weapon['def conversion'])
    if weapon['Passive']=='em scaling':
        em_conversion+=(weapon['em conversion'])
        
    if weapon['Passive2']=='hp scaling':
        hp_conversion+=(weapon['hp conversion'])
    if weapon['Passive2']=='er scaling':
        er_conversion+=(weapon['er conversion'])
    if weapon['Passive2']=='def scaling':
        def_conversion+=(weapon['def conversion'])
    if weapon['Passive2']=='em scaling':
        em_conversion+=(weapon['em conversion'])
    if weapon['name']=='engulfing lightning':
        ta+=weapon['Passive Bonus']*er*(character['base attack']+weapon['base attack'])
    if character['name']=='Ei':
        db+=0.4*er
        
    if character['hp scaling']==True or  weapon['Passive2']=='hp scaling' or  weapon['Passive']=='hp scaling':
        ta+=hp_conversion*thp
    if character['er scaling']==True or weapon['Passive2']=='er scaling' or weapon['Passive']=='er scaling':
        ta+=er_conversion*(1+er)
    if character['def scaling']==True or weapon['Passive2']=='def scaling' or weapon['Passive']=='def scaling':
        ta+=def_conversion*tdf
    if character['em scaling']==True or weapon['Passive2']=='em scaling' or weapon['Passive']=='em scaling':
        ta+=em_conversion*em

    if character['hp d scaling']==True:
        hp_d_conversion+=(character['hp d conversion'])
    if character['er d scaling']==True:
        er_d_conversion+=(character['er d conversion'])
    if character['def d scaling']==True:
        def_d_conversion+=(character['def d conversion'])
    if character['em d scaling']==True:
        em_d_conversion+=(character['em d conversion'])

    if weapon['Passive']=='hp d scaling':
        hp_d_conversion+=(weapon['hp d conversion'])
    if weapon['Passive']=='er d scaling':
        er_d_conversion+=(weapon['er d conversion'])
    if weapon['Passive']=='def d scaling':
        def_d_conversion+=(weapon['def d conversion'])
    if weapon['Passive']=='em d scaling':
        em_d_conversion+=(weapon['em d conversion'])
        
    if weapon['Passive2']=='hp d scaling':
        hp_d_conversion+=(weapon['hp d conversion'])
    if weapon['Passive2']=='er d scaling':
        er_d_conversion+=(weapon['er d conversion'])
    if weapon['Passive2']=='def d scaling':
        def_d_conversion+=(weapon['def d conversion'])
    if weapon['Passive2']=='em d scaling':
        em_d_conversion+=(weapon['em d conversion'])
        
    if character['hp d scaling']==True or weapon['Passive2']=='hp d scaling' or  weapon['Passive']=='hp d scaling':
        db+=hp_d_conversion*thp
    if character['er d scaling']==True or weapon['Passive2']=='er d scaling' or weapon['Passive']=='er d scaling':
        db+=er_d_conversion*(1+er)
    if character['def d scaling']==True or weapon['Passive2']=='def d scaling' or weapon['Passive']=='def d scaling':
        db+=def_d_conversion*tdf
    if character['em d scaling']==True or weapon['Passive2']=='em d scaling' or weapon['Passive']=='em d scaling':
        db+=em_d_conversion*em

    db=1+db+geo_damage_boost
    em_bonus=1
    y=epe.keys()
    if 'fc' in y:
        if character['bennett_boost']:
            if character['name']!='bennett':
                ta-=950*(character['bennett_er']/200)
            else:
                if er>1:
                    ta-=950
                else:
                    ta-=950*(1+er)/2    
        dpss={'ta':ta,
             'tdf':tdf,
             'thp':thp,
             'db':db-geo_damage_boost,
             'er':1+er,
             'em':em,
             'cr':cr,
             'cd':cd}
        return dpss
    x=character['percent_react']
    if character['element reaction'] == 'vaporise' or character['element reaction']=='melt':
        em_bonus = character['em_mult']*(1+(2.78*em)/(1400+em))
        if artifacts['set']== '4CW':
            em_bonus = character['em_mult']*(1+(2.78*em)/(1400+em)+0.15)
            x=character['percent_react']
        if cr>1:
            cr=1
        y=ta*db*(1+cr*cd)*(x*em_bonus+(1-x))
        na_mult=1
        ca_mult=1
        e_mult=1
        q_mult=1
        if weapon['Passive']=='NA Bonus':
            na_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='CA Bonus':
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='NACA Bonus':
            na_mult+=weapon['Passive Bonus']
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='E Bonus':
            e_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='Q_bonus':
            q_mult+=weapon['Passive Bonus']
            
        if weapon['Passive2']=='NA Bonus':
            na_mult+=weapon['Passive Bonus']
        elif weapon['Passive2']=='CA Bonus':
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive2']=='NACA Bonus':
            na_mult+=weapon['Passive Bonus']
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive2']=='E Bonus':
            e_mult+=weapon['Passive Bonus']
        elif weapon['Passive2']=='Q_bonus':
            q_mult+=weapon['Passive Bonus']
    
        if artifacts['set']=='4GLD':
            na_mult+=0.35
        elif artifacts['set'] == '4WT':
            ca_mult+=0.35
        elif artifacts['set2'] == '2NB':
            q_mult+=0.2
        elif artifacts['set'] == '2NB':
            q_mult+=0.2
        elif artifacts['set'] == '4NB':
            q_mult+=0.2
        elif artifacts['set'] == '4RB':
            na_mult+=0.4
            ca_mult+=0.4
        elif artifacts['set'] == '4HD':
            na_mult+=0.3
            ca_mult+=0.3
        elif artifacts['set'] == '4ESF':
            q_mult+=er/4
        elif artifacts['set'] == '4SR':
            character['Q_cost']+=20 
        if character['play_style'] == 'main dps':
            number_NA = int(character['MDPS'][0])
            number_CA = int(character['MDPS'][1])
            number_E  = int(character['MDPS'][2])
            number_Q  = int(character['MDPS'][3])
            pps=2+electro_particle_boost
            Q_recharge = character['Q_cost']/(pps*(1+er))
            if Q_recharge<character['Q_cd']:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*q_mult)
            else:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*(character['Q_cd']/Q_recharge)*q_mult)
            return dps
        if character['play_style'] == 'quickswap':
            number_NA = int(character['QS'][0])
            number_CA = int(character['QS'][1])
            number_E  = int(character['QS'][2])
            number_Q  = int(character['QS'][3])
            pps=1+electro_particle_boost
            Q_recharge = character['Q_cost']/(pps*(1+er))
            if Q_recharge<character['Q_cd']:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*q_mult)
            else:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*(character['Q_cd']/Q_recharge)*q_mult)
            return dps
    elif character['element reaction']!='none' or character['element reaction'] != 'vaporise' or character['element reaction']!='melt':
        reaction_bonus=0
        if artifacts['set']== '4CW':
            if character['element reaction']=='overloaded':
                reaction_bonus=0.4
        if artifacts['set']== '4TF':
            if character['element reaction']=='overloaded' or character['element reaction']=='electro charged' or character['element reaction']=='superconduct':
                reaction_bonus=0.4
        if artifacts['set']== '4VV':
            if character['element reaction']=='swirl':
                reaction_bonus=0.6
        level_mult=0.00194*character['level']**3-0.319*character['level']**2+30.7*character['level']-868
        if character['element reaction']=='overloaded':
            em_bonus = 4*(1+(16*em)/(2000+em)+reaction_bonus)*level_mult
        if character['element reaction']=='shatter':
            em_bonus = 3*(1+(16*em)/(2000+em)+reaction_bonus)*level_mult
        if character['element reaction']=='electro charged':
            em_bonus = 2.4*(1+(16*em)/(2000+em)+reaction_bonus)*level_mult*1.5
        if character['element reaction']=='swirl':
            em_bonus = 1.2*(1+(16*em)/(2000+em)+reaction_bonus)*level_mult
        x=character['percent_react']
        if cr>1:
            cr=1
        y=ta*db*(1+cr*cd)
        na_mult=1
        ca_mult=1
        e_mult=1
        q_mult=1
        if weapon['Passive']=='NA Bonus':
            na_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='CA Bonus':
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='NACA Bonus':
            na_mult+=weapon['Passive Bonus']
            ca_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='E Bonus':
            e_mult+=weapon['Passive Bonus']
        elif weapon['Passive']=='Q_bonus':
            q_mult+=weapon['Passive Bonus']
    
        if artifacts['set']=='4GLD':
            na_mult+=0.35
        elif artifacts['set'] == '4WT':
            ca_mult+=0.35
        elif artifacts['set2'] == '2NB':
            q_mult+=0.2
        elif artifacts['set'] == '2NB':
            q_mult+=0.2
        elif artifacts['set'] == '4NB':
            q_mult+=0.2
        elif artifacts['set'] == '4RB':
            na_mult+=0.4
            ca_mult+=0.4
        elif artifacts['set'] == '4HD':
            na_mult+=0.3
            ca_mult+=0.3
        elif artifacts['set'] == '4ESF':
            q_mult+=er/4
        elif artifacts['set'] == '4SR':
            character['Q_cost']+=20
        if character['hp bonus_damage']:
            naca_bonus=character['naca hp bonus']*thp
            e_bonus=character['e hp bonus']*thp
            q_bonus=character['q hp bonus']*thp
        else: 
            naca_bonus=0
            e_bonus=0
            q_bonus=0
        if character['play_style'] == 'main dps':
            number_NA = int(character['MDPS'][0])
            number_CA = int(character['MDPS'][1])
            number_E  = int(character['MDPS'][2])
            number_Q  = int(character['MDPS'][3])
            pps=2+electro_particle_boost
            Q_recharge = character['Q_cost']/(pps*(1+er))
            if Q_recharge<character['Q_cd']:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*q_mult)+(number_NA+number_CA+number_E+number_Q)*x*em_bonus+(number_NA+number_CA)*naca_bonus+number_E*e_bonus+number_Q*q_bonus
            else:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*(character['Q_cd']/Q_recharge)*q_mult)+(number_NA+number_CA+number_E+number_Q)*x*em_bonus+(number_NA+number_CA)*naca_bonus+number_E*e_bonus+number_Q*q_bonus
            return dps
        if character['play_style'] == 'quickswap':
            number_NA = int(character['QS'][0])
            number_CA = int(character['QS'][1])
            number_E  = int(character['QS'][2])
            number_Q  = int(character['QS'][3])
            pps=1+electro_particle_boost
            Q_recharge = character['Q_cost']/(pps*(1+er))
            if Q_recharge<character['Q_cd']:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*q_mult)+(number_NA+number_CA+number_E+number_Q)*x*em_bonus+(number_NA+number_CA)*naca_bonus+number_E*e_bonus+number_Q*q_bonus
            else:
                dps = y*(number_NA*character['NA']*na_mult + number_CA*character['CA']*ca_mult + number_E*character['E']*e_mult + number_Q*character['Q']*(character['Q_cd']/Q_recharge)*q_mult)+(number_NA+number_CA+number_E+number_Q)*x*em_bonus+(number_NA+number_CA)*naca_bonus+number_E*e_bonus+number_Q*q_bonus
            return dps