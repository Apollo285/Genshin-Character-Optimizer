# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:07:21 2021

@author: aeapo
"""

from calc_damage import calc_damagex
import copy
from fill_artifact_rolls import fill_artifact_rollsx
def get_optimal_damagex(character,weapon,epe):
    attack=0.058
    em=23
    cr=0.039
    cd=0.078
    er=0.065
    hp=0.0583
    df=0.0729
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    att_bonus = 0
    em_bonus = 0
    er_bonus = 0
    d_bonus = 0
    cr_bonus = 0
    cd_bonus = 0
    hp_bonus = 0
    df_bonus = 0
    goblet_damage=0.466
    if character['element']=='physical':
        goblet_damage=0.583
    # Get weapon info
    if weapon['Main Stat']=='Attack':
        att_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Cr':
        cr_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Cd':
        cd_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Em':
        em_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Er':
        er_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Hp':
        hp_bonus+=weapon['Main Stat Bonus']
    elif weapon['Main Stat']=='Df':
        df_bonus+=weapon['Main Stat Bonus']
        
    if weapon['Passive']=='Attack':
        att_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Cr':
        cr_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Cd':
        cd_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Em':
        em_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Er':
        er_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Damage':
        d_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Hp':
        hp_bonus+=weapon['Passive Bonus']
    elif weapon['Passive']=='Df':
        df_bonus+=weapon['Passive Bonus']

    if weapon['Passive2']=='Attack':
        att_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Cr':
        cr_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Cd':
        cd_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Em':
        em_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Er':
        er_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Damage':
        d_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Hp':
        hp_bonus+=weapon['Passive Bonus']
    elif weapon['Passive2']=='Df':
        df_bonus+=weapon['Passive Bonus']
    
    cryo_crit=0
    pyro_attack_boost=0
    if epe['epe']=='pyro':
        pyro_attack_boost=0.25
    if epe['epe']=='cryo':
        cryo_crit=0.15
    if epe['epe2']=='pyro':
        pyro_attack_boost=0.25
    if epe['epe2']=='cryo':
        cryo_crit=0.15
        
    artifact = character['artifact']
    if artifact['set']=='2GF' or artifact['set2']=='2GF' or artifact['set']=='4GF':
        att_bonus += 0.18
    if character['element']=='cryo':
        if character['element reaction']=='freeze':
            if artifact['set']=='4BS':
                cr_bonus+=0.2+character['percent_react']*0.2
        else:
            if artifact['set']=='4BS':
                cr_bonus+=0.2
    if artifact['set']=='2WT' or artifact['set2']=='2WT' or artifact['set']=='4WT':
        em_bonus += 80
    if artifact['set']=='4TS':
        d_bonus += 0.35*0.75
    if artifact['set']=='2TF' or artifact['set2']=='2TF' or artifact['set']=='4TF':
        d_bonus += 0.15
    if artifact['set']=='2VV' or artifact['set2']=='2VV' or artifact['set']=='4VV':
        d_bonus += 0.15
    if artifact['set']=='2CW' or artifact['set2']=='2CW' or artifact['set']=='4CW':
        d_bonus+=0.15
    if artifact['set']=='4LW':
        d_bonus += 0.35*0.75
    if artifact['set']=='2BC' or artifact['set2']=='2BC' or artifact['set']=='4BC':
        d_bonus += 0.25
    if artifact['set']=='2AP' or artifact['set2']=='2AP' or artifact['set']=='4AP':
        d_bonus+=0.15
    if artifact['set']=='2BS' or artifact['set2']=='2BS' or artifact['set']=='4BS':
        d_bonus+=0.15
    if artifact['set']=='2HD' or artifact['set2']=='2HD' or artifact['set']=='4HD':
        d_bonus+=0.15
    if artifact['set']=='2TM' or artifact['set2']=='2TM' or artifact['set']=='4TM':
        hp_bonus+=0.2
    if artifact['set']=='2PF' or artifact['set2']=='2PF':
        d_bonus=0.25
    if artifact['set']=='4PF':
        d_bonus+=0.5
        att_bonus+=0.18
    if artifact['set']=='2EF' or artifact['set2']=='2EF' or artifact['set']=='4EF':
        er_bonus+=0.15
    if artifact['set']=='2SR' or artifact['set2']=='2SR' or artifact['set']=='4SR':
        att_bonus+=0.18

    artifact['sands_type']:'attack'
    artifact['goblet_type']='damage',
    artifact['circlet_type']='crit rate'
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
        grad = []
        artifact['sands_type']='attack'
        artifact['goblet_type']='damage'
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        init_damage = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=(n_er+1)*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_er = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=(n_em+1)*em+em_bonus
        artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_em = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_cr = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_cd = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = (n_attack+1)*attack+att_bonus+0.466+pyro_attack_boost
        damage_att = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=(n_hp+1)*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_hp = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=(n_df+1)*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_df = calc_damagex(character,weapon,artifact,epe)
        
        grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
        max_grad = max(grad)
        max_index = grad.index(max_grad)
        x=0
        while x!=1:
            if max_index==0:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[0]=grad[0]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==1:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[1]=grad[1]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==2:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[2]=grad[2]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==3:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[3]=grad[3]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==4:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[4]=grad[4]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==5:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[5]=grad[5]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==6:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[6]=grad[6]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
        n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
        n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
        n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
        n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
        n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
        n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
        n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
        artifact_cr = copy.deepcopy(artifact)#{}
        artifact_cr['hp']=n_hp*hp+hp_bonus
        artifact_cr['df']=(n_df)*df+df_bonus
        artifact_cr['er']=n_er*er+er_bonus
        artifact_cr['em']=n_em*em+em_bonus
        artifact_cr['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
        artifact_cr['cd']=n_cd*cd+0.5+cd_bonus
        artifact_cr['db']=goblet_damage+d_bonus
        artifact_cr['attack'] = (n_attack)*attack+att_bonus+0.466+pyro_attack_boost
        artifact_cr['total_damage'] = calc_damagex(character,weapon,artifact,epe)
        artifact_cr['er_rolls']=n_er
        artifact_cr['em_rolls']=n_em
        artifact_cr['cr_rolls']=n_cr
        artifact_cr['cd_rolls']=n_cd
        artifact_cr['hp_rolls']=n_hp
        artifact_cr['def_rolls']=n_df
        artifact_cr['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
        grad = []
        artifact['sands_type']='attack'
        artifact['d_type']='damage'
        artifact['circlet_type']='crit damage'
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        init_damage = calc_damagex(character,weapon,artifact,epe)

        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=(n_er+1)*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_er = calc_damagex(character,weapon,artifact,epe)

        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus        
        artifact['er']=n_er*er+er_bonus
        artifact['em']=(n_em+1)*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_em = calc_damagex(character,weapon,artifact,epe)

        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus        
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_cr = calc_damagex(character,weapon,artifact,epe)

        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus        
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=(n_cd+1)*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_cd = calc_damagex(character,weapon,artifact,epe)

        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus        
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = (n_attack+1)*attack+att_bonus+0.466+pyro_attack_boost
        damage_att = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=(n_hp+1)*hp+hp_bonus
        artifact['df']=n_df*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_hp = calc_damagex(character,weapon,artifact,epe)
        
        artifact['hp']=n_hp*hp+hp_bonus
        artifact['df']=(n_df+1)*df+df_bonus
        artifact['er']=n_er*er+er_bonus
        artifact['em']=n_em*em+em_bonus
        artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
        artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
        artifact['db']=goblet_damage+d_bonus
        artifact['attack'] = n_attack*attack+att_bonus+0.466+pyro_attack_boost
        damage_df = calc_damagex(character,weapon,artifact,epe)
        
        grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
        max_grad = max(grad)
        max_index = grad.index(max_grad)
        x=0
        while x!=1:
            if max_index==0:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[0]=grad[0]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==1:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[1]=grad[1]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==2:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[2]=grad[2]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==3:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[3]=grad[3]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==4:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[4]=grad[4]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==5:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[5]=grad[5]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
            if max_index==6:
                y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                if y!=False:
                    artifact=copy.deepcopy(y)
                    x=1
                else:
                    grad[6]=grad[6]-1e6
                    max_grad = max(grad)
                    max_index = grad.index(max_grad)
        n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
        n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
        n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
        n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
        n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
        n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
        n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
        artifact_cd = copy.deepcopy(artifact)
        artifact_cd['hp']=n_hp*hp+hp_bonus
        artifact_cd['df']=(n_df)*df+df_bonus
        artifact_cd['er']=n_er*er+er_bonus
        artifact_cd['em']=n_em*em+em_bonus
        artifact_cd['cr']=n_cr*cr+0.05+cryo_crit+cr_bonus
        artifact_cd['cd']=n_cd*cd+0.5+0.622+cd_bonus
        artifact_cd['db']=goblet_damage+d_bonus
        artifact_cd['attack'] = (n_attack)*attack+att_bonus+0.466+pyro_attack_boost
        artifact_cd['total_damage'] = calc_damagex(character,weapon,artifact,epe)
        artifact_cd['er_rolls']=n_er
        artifact_cd['em_rolls']=n_em
        artifact_cd['cr_rolls']=n_cr
        artifact_cd['cd_rolls']=n_cd
        artifact_cd['hp_rolls']=n_hp
        artifact_cd['def_rolls']=n_df
        artifact_cd['attack_rolls']=n_attack
    if artifact_cd['total_damage']>artifact_cr['total_damage']:
        artifact = artifact_cd
        artifact['circlet_type']='crit damage'
        #artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
    else:
        artifact = artifact_cr
        artifact['circlet_type']='crit rate'
        #artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
        
    artifact_att=copy.deepcopy(artifact)
    
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and artifact['em']>=187:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='em'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_em = copy.deepcopy(artifact)
            artifact_em['er']=n_er*er+er_bonus
            artifact_em['em']=n_em*em+em_bonus+187
            artifact_em['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_em['cd']=n_cd*cd+0.5+cd_bonus
            artifact_em['db']=goblet_damage+d_bonus
            artifact_em['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_em['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_em['er_rolls']=n_er
            artifact_em['em_rolls']=n_em
            artifact_em['cr_rolls']=n_cr
            artifact_em['cd_rolls']=n_cd
            artifact_em['hp_rolls']=n_hp
            artifact_em['def_rolls']=n_df
            artifact_em['attack_rolls']=n_attack
        # if artifact_att['total_damage']>artifact_em['total_damage']:
        #     artifact = artifact_att
        #     artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
        # else:
        #     artifact = artifact_em
        #     artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['hp scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='hp'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_hp = copy.deepcopy(artifact)
            artifact_hp['hp']=n_hp*hp+hp_bonus+0.466
            artifact_hp['df']=(n_df)*df+df_bonus
            artifact_hp['er']=n_er*er+er_bonus
            artifact_hp['em']=n_em*em+em_bonus
            artifact_hp['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_hp['cd']=n_cd*cd+0.5+cd_bonus
            artifact_hp['db']=goblet_damage+d_bonus
            artifact_hp['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_hp['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_hp['er_rolls']=n_er
            artifact_hp['em_rolls']=n_em
            artifact_hp['cr_rolls']=n_cr
            artifact_hp['cd_rolls']=n_cd
            artifact_hp['hp_rolls']=n_hp
            artifact_hp['def_rolls']=n_df
            artifact_hp['attack_rolls']=n_attack
            
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['def scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='df'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_df = copy.deepcopy(artifact)
            artifact_df['hp']=n_hp*hp+hp_bonus
            artifact_df['df']=(n_df)*df+df_bonus+0.466
            artifact_df['er']=n_er*er+er_bonus
            artifact_df['em']=n_em*em+em_bonus
            artifact_df['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_df['cd']=n_cd*cd+0.5+cd_bonus
            artifact_df['db']=goblet_damage+d_bonus
            artifact_df['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_df['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_df['er_rolls']=n_er
            artifact_df['em_rolls']=n_em
            artifact_df['cr_rolls']=n_cr
            artifact_df['cd_rolls']=n_cd
            artifact_df['hp_rolls']=n_hp
            artifact_df['def_rolls']=n_df
            artifact_df['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='er'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_er = copy.deepcopy(artifact)
            artifact_er['hp']=n_hp*hp+hp_bonus
            artifact_er['df']=(n_df)*df+df_bonus
            artifact_er['er']=n_er*er+er_bonus+0.518
            artifact_er['em']=n_em*em+em_bonus
            artifact_er['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_er['cd']=n_cd*cd+0.5+cd_bonus
            artifact_er['db']=goblet_damage+d_bonus
            artifact_er['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_er['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_er['er_rolls']=n_er
            artifact_er['em_rolls']=n_em
            artifact_er['cr_rolls']=n_cr
            artifact_er['cd_rolls']=n_cd
            artifact_er['hp_rolls']=n_hp
            artifact_er['def_rolls']=n_df
            artifact_er['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='er'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_era = copy.deepcopy(artifact)
            artifact_era['hp']=n_hp*hp+hp_bonus
            artifact_era['df']=(n_df)*df+df_bonus
            artifact_era['er']=n_er*er+er_bonus+0.518
            artifact_era['em']=n_em*em+em_bonus
            artifact_era['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_era['cd']=n_cd*cd+0.5+cd_bonus
            artifact_era['db']=d_bonus
            artifact_era['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_era['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_era['er_rolls']=n_er
            artifact_era['em_rolls']=n_em
            artifact_era['cr_rolls']=n_cr
            artifact_era['cd_rolls']=n_cd
            artifact_era['hp_rolls']=n_hp
            artifact_era['def_rolls']=n_df
            artifact_era['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='em'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_ema = copy.deepcopy(artifact)
            artifact_ema['hp']=n_hp*hp+hp_bonus
            artifact_ema['df']=(n_df)*df+df_bonus
            artifact_ema['er']=n_er*er+er_bonus
            artifact_ema['em']=n_em*em+em_bonus+187
            artifact_ema['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_ema['cd']=n_cd*cd+0.5+cd_bonus
            artifact_ema['db']=d_bonus
            artifact_ema['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_ema['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_ema['er_rolls']=n_er
            artifact_ema['em_rolls']=n_em
            artifact_ema['cr_rolls']=n_cr
            artifact_ema['cd_rolls']=n_cd
            artifact_ema['hp_rolls']=n_hp
            artifact_ema['def_rolls']=n_df
            artifact_ema['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='attack'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_aa = copy.deepcopy(artifact)
            artifact_aa['hp']=n_hp*hp+hp_bonus
            artifact_aa['df']=(n_df)*df+df_bonus
            artifact_aa['er']=n_er*er+er_bonus
            artifact_aa['em']=n_em*em+em_bonus
            artifact_aa['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_aa['cd']=n_cd*cd+0.5+cd_bonus
            artifact_aa['db']=d_bonus
            artifact_aa['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466+0.466
            artifact_aa['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_aa['er_rolls']=n_er
            artifact_aa['em_rolls']=n_em
            artifact_aa['cr_rolls']=n_cr
            artifact_aa['cd_rolls']=n_cd
            artifact_aa['hp_rolls']=n_hp
            artifact_aa['def_rolls']=n_df
            artifact_aa['attack_rolls']=n_attack
            
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='hp'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_ahp = copy.deepcopy(artifact)
            artifact_ahp['hp']=n_hp*hp+hp_bonus+0.466
            artifact_ahp['df']=(n_df)*df+df_bonus
            artifact_ahp['er']=n_er*er+er_bonus
            artifact_ahp['em']=n_em*em+em_bonus
            artifact_ahp['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_ahp['cd']=n_cd*cd+0.5+cd_bonus
            artifact_ahp['db']=d_bonus
            artifact_ahp['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_ahp['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_ahp['er_rolls']=n_er
            artifact_ahp['em_rolls']=n_em
            artifact_ahp['cr_rolls']=n_cr
            artifact_ahp['cd_rolls']=n_cd
            artifact_ahp['hp_rolls']=n_hp
            artifact_ahp['def_rolls']=n_df
            artifact_ahp['attack_rolls']=n_attack

    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit rate':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='df'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_adf = copy.deepcopy(artifact)
            artifact_adf['hp']=n_hp*hp+hp_bonus
            artifact_adf['df']=(n_df)*df+df_bonus+0.466
            artifact_adf['er']=n_er*er+er_bonus
            artifact_adf['em']=n_em*em+em_bonus
            artifact_adf['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_adf['cd']=n_cd*cd+0.5+cd_bonus
            artifact_adf['db']=d_bonus
            artifact_adf['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_adf['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_adf['er_rolls']=n_er
            artifact_adf['em_rolls']=n_em
            artifact_adf['cr_rolls']=n_cr
            artifact_adf['cd_rolls']=n_cd
            artifact_adf['hp_rolls']=n_hp
            artifact_adf['def_rolls']=n_df
            artifact_adf['attack_rolls']=n_attack

    if artifact['circlet_type']=='crit rate':
        lis=[artifact_att['total_damage'],artifact_er['total_damage'],artifact_hp['total_damage'],artifact_df['total_damage'],artifact_era['total_damage'],artifact_ema['total_damage'],artifact_aa['total_damage'],artifact_ahp['total_damage'],artifact_adf['total_damage'],artifact_em['total_damage']]
        max_lis = max(lis)
        max_lis = lis.index(max_lis)
        
        if character['forced_sands']=='hp':
            if artifact_ahp['total_damage']>artifact_hp['total_damage']:
                artifact=artifact_ahp
                artifact['sands_type']='hp'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_hp
                artifact['sands_type']='hp'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='er':
            if artifact_era['total_damage']>artifact_er['total_damage']:
                artifact=artifact_era
                artifact['sands_type']='er'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_er
                artifact['sands_type']='er'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='em':
            if artifact_ema['total_damage']>artifact_em['total_damage']:
                artifact=artifact_ema
                artifact['sands_type']='em'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_em
                artifact['sands_type']='em'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='df':
            if artifact_adf['total_damage']>artifact_df['total_damage']:
                artifact=artifact_adf
                artifact['sands_type']='df'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_df
                artifact['sands_type']='df'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='attack':
            if artifact_aa['total_damage']>artifact_att['total_damage']:
                artifact=artifact_aa
                artifact['sands_type']='attack'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_att
                artifact['sands_type']='attack'
                artifact['goblet_type']='damage'
                return artifact
        if max_lis==0:
            artifact=artifact_att
            artifact['sands_type']='attack'
            artifact['goblet_type']='damage'
        elif max_lis==1:
            artifact=artifact_er
            artifact['sands_type']='er'
            artifact['goblet_type']='damage'
        elif max_lis==2:
            artifact=artifact_hp
            artifact['sands_type']='hp'
            artifact['goblet_type']='damage'
        elif max_lis==3:
            artifact=artifact_df
            artifact['sands_type']='df'
            artifact['goblet_type']='damage'
        elif max_lis==4:
            artifact=artifact_era
            artifact['sands_type']='er'
            artifact['goblet_type']='attack'
        elif max_lis==5:
            artifact=artifact_ema
            artifact['sands_type']='em'
            artifact['goblet_type']='attack'
        elif max_lis==6:
            artifact=artifact_aa
            artifact['sands_type']='attack'
            artifact['goblet_type']='attack'
        elif max_lis==7:
            artifact=artifact_ahp
            artifact['sands_type']='hp'
            artifact['goblet_type']='attack'
        elif max_lis==8:
            artifact=artifact_adf
            artifact['sands_type']='df'
            artifact['goblet_type']='attack'
        elif max_lis==9:
            artifact=artifact_em
            artifact['sands_type']='em'
            artifact['goblet_type']='damage'
        return artifact
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and artifact['em']>=187:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='em'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_em = copy.deepcopy(artifact)
            artifact_em['er']=n_er*er+er_bonus
            artifact_em['em']=n_em*em+em_bonus+187
            artifact_em['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_em['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_em['db']=goblet_damage+d_bonus
            artifact_em['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_em['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_em['er_rolls']=n_er
            artifact_em['em_rolls']=n_em
            artifact_em['cr_rolls']=n_cr
            artifact_em['cd_rolls']=n_cd
            artifact_em['hp_rolls']=n_hp
            artifact_em['def_rolls']=n_df
            artifact_em['attack_rolls']=n_attack
        # if artifact_att['total_damage']>artifact_em['total_damage']:
        #     artifact = artifact_att
        #     artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
        # else:
        #     artifact = artifact_em
        #     artifact['attack'] = (artifact['attack']+1)*(character['base attack']+weapon['base attack'])+311
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['hp scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='hp'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_hp = copy.deepcopy(artifact)
            artifact_hp['hp']=n_hp*hp+hp_bonus+0.466
            artifact_hp['df']=(n_df)*df+df_bonus
            artifact_hp['er']=n_er*er+er_bonus
            artifact_hp['em']=n_em*em+em_bonus
            artifact_hp['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_hp['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_hp['db']=goblet_damage+d_bonus
            artifact_hp['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_hp['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_hp['er_rolls']=n_er
            artifact_hp['em_rolls']=n_em
            artifact_hp['cr_rolls']=n_cr
            artifact_hp['cd_rolls']=n_cd
            artifact_hp['hp_rolls']=n_hp
            artifact_hp['def_rolls']=n_df
            artifact_hp['attack_rolls']=n_attack
            
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['def scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='df'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_df = copy.deepcopy(artifact)
            artifact_df['hp']=n_hp*hp+hp_bonus
            artifact_df['df']=(n_df)*df+df_bonus+0.466
            artifact_df['er']=n_er*er+er_bonus
            artifact_df['em']=n_em*em+em_bonus
            artifact_df['cr']=(n_cr)*cr+0.311+0.05+cr_bonus+cryo_crit
            artifact_df['cd']=n_cd*cd+0.5+cd_bonus
            artifact_df['db']=goblet_damage+d_bonus
            artifact_df['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_df['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_df['er_rolls']=n_er
            artifact_df['em_rolls']=n_em
            artifact_df['cr_rolls']=n_cr
            artifact_df['cd_rolls']=n_cd
            artifact_df['hp_rolls']=n_hp
            artifact_df['def_rolls']=n_df
            artifact_df['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['er scaling']==True:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='er'
            artifact['goblet_type']='damage'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=goblet_damage+d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_er = copy.deepcopy(artifact)
            artifact_er['hp']=n_hp*hp+hp_bonus
            artifact_er['df']=(n_df)*df+df_bonus
            artifact_er['er']=n_er*er+er_bonus+0.518
            artifact_er['em']=n_em*em+em_bonus
            artifact_er['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_er['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_er['db']=goblet_damage+d_bonus
            artifact_er['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost
            artifact_er['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_er['er_rolls']=n_er
            artifact_er['em_rolls']=n_em
            artifact_er['cr_rolls']=n_cr
            artifact_er['cd_rolls']=n_cd
            artifact_er['hp_rolls']=n_hp
            artifact_er['def_rolls']=n_df
            artifact_er['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='er'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus+0.518
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_era = copy.deepcopy(artifact)
            artifact_era['hp']=n_hp*hp+hp_bonus
            artifact_era['df']=(n_df)*df+df_bonus
            artifact_era['er']=n_er*er+er_bonus+0.518
            artifact_era['em']=n_em*em+em_bonus
            artifact_era['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_era['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_era['db']=d_bonus
            artifact_era['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_era['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_era['er_rolls']=n_er
            artifact_era['em_rolls']=n_em
            artifact_era['cr_rolls']=n_cr
            artifact_era['cd_rolls']=n_cd
            artifact_era['hp_rolls']=n_hp
            artifact_era['def_rolls']=n_df
            artifact_era['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# em and attack
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='em'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus+187
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_ema = copy.deepcopy(artifact)
            artifact_ema['hp']=n_hp*hp+hp_bonus
            artifact_ema['df']=(n_df)*df+df_bonus
            artifact_ema['er']=n_er*er+er_bonus
            artifact_ema['em']=n_em*em+em_bonus+187
            artifact_ema['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_ema['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_ema['db']=d_bonus
            artifact_ema['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_ema['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_ema['er_rolls']=n_er
            artifact_ema['em_rolls']=n_em
            artifact_ema['cr_rolls']=n_cr
            artifact_ema['cd_rolls']=n_cd
            artifact_ema['hp_rolls']=n_hp
            artifact_ema['def_rolls']=n_df
            artifact_ema['attack_rolls']=n_attack
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='attack'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_aa = copy.deepcopy(artifact)
            artifact_aa['hp']=n_hp*hp+hp_bonus
            artifact_aa['df']=(n_df)*df+df_bonus
            artifact_aa['er']=n_er*er+er_bonus
            artifact_aa['em']=n_em*em+em_bonus
            artifact_aa['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_aa['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_aa['db']=d_bonus
            artifact_aa['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466+0.466
            artifact_aa['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_aa['er_rolls']=n_er
            artifact_aa['em_rolls']=n_em
            artifact_aa['cr_rolls']=n_cr
            artifact_aa['cd_rolls']=n_cd
            artifact_aa['hp_rolls']=n_hp
            artifact_aa['def_rolls']=n_df
            artifact_aa['attack_rolls']=n_attack

    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='hp'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus+0.466
            artifact['df']=n_df*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus+0.466
            artifact['df']=(n_df+1)*df+df_bonus
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_ahp = copy.deepcopy(artifact)
            artifact_ahp['hp']=n_hp*hp+hp_bonus+0.466
            artifact_ahp['df']=(n_df)*df+df_bonus
            artifact_ahp['er']=n_er*er+er_bonus
            artifact_ahp['em']=n_em*em+em_bonus
            artifact_ahp['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_ahp['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_ahp['db']=d_bonus
            artifact_ahp['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_ahp['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_ahp['er_rolls']=n_er
            artifact_ahp['em_rolls']=n_em
            artifact_ahp['cr_rolls']=n_cr
            artifact_ahp['cd_rolls']=n_cd
            artifact_ahp['hp_rolls']=n_hp
            artifact_ahp['def_rolls']=n_df
            artifact_ahp['attack_rolls']=n_attack
            
    n_attack=0
    n_em=0
    n_cr=0
    n_cd=0
    n_er=0
    n_hp=0
    n_df=0
    artifact['feather']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['flower']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['sands']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['goblet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    artifact['circlet']={'rolls':0,
                     'hp':0,
                     'df':0,
                     'er':0,
                     'em':0,
                     'attack':0,
                     'cr':0,
                     'cd':0}
    if artifact['circlet_type']=='crit damage':# and character['er scaling']==True and d_bonus>0.466:
        while (n_attack+n_em+n_cr+n_cd+n_er+n_hp+n_df)<45:
            grad = []
            artifact['sands_type']='df'
            artifact['goblet_type']='attack'
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            init_damage = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=(n_er+1)*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_er = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=(n_em+1)*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_em = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=(n_cr+1)*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cr = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=(n_cd+1)*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_cd = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = (n_attack+1)*attack+att_bonus+pyro_attack_boost+0.466
            damage_att = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=(n_hp+1)*hp+hp_bonus
            artifact['df']=n_df*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_hp = calc_damagex(character,weapon,artifact,epe)
            
            artifact['hp']=n_hp*hp+hp_bonus
            artifact['df']=(n_df+1)*df+df_bonus+0.466
            artifact['er']=n_er*er+er_bonus
            artifact['em']=n_em*em+em_bonus
            artifact['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact['db']=d_bonus
            artifact['attack'] = n_attack*attack+att_bonus+pyro_attack_boost+0.466
            damage_df = calc_damagex(character,weapon,artifact,epe)
            
            grad=[damage_er-init_damage,damage_em-init_damage,damage_cr-init_damage,damage_cd-init_damage,damage_att-init_damage, damage_hp-init_damage, damage_df-init_damage]
            max_grad = max(grad)
            max_index = grad.index(max_grad)
            x=0
            while x!=1:
                if max_index==0:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'er')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[0]=grad[0]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==1:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'em')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[1]=grad[1]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==2:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cr')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[2]=grad[2]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==3:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'cd')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[3]=grad[3]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==4:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'attack')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[4]=grad[4]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==5:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'hp')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[5]=grad[5]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
                if max_index==6:
                    y=fill_artifact_rollsx(copy.deepcopy(artifact),'df')
                    if y!=False:
                        artifact=copy.deepcopy(y)
                        x=1
                    else:
                        grad[6]=grad[6]-1e6
                        max_grad = max(grad)
                        max_index = grad.index(max_grad)
            n_hp = artifact['flower']['hp']+artifact['feather']['hp']+artifact['sands']['hp']+artifact['goblet']['hp']+artifact['circlet']['hp']
            n_er = artifact['flower']['er']+artifact['feather']['er']+artifact['sands']['er']+artifact['goblet']['er']+artifact['circlet']['er']
            n_em = artifact['flower']['em']+artifact['feather']['em']+artifact['sands']['em']+artifact['goblet']['em']+artifact['circlet']['em']
            n_attack = artifact['flower']['attack']+artifact['feather']['attack']+artifact['sands']['attack']+artifact['goblet']['attack']+artifact['circlet']['attack']
            n_df = artifact['flower']['df']+artifact['feather']['df']+artifact['sands']['df']+artifact['goblet']['df']+artifact['circlet']['df']
            n_cr = artifact['flower']['cr']+artifact['feather']['cr']+artifact['sands']['cr']+artifact['goblet']['cr']+artifact['circlet']['cr']
            n_cd = artifact['flower']['cd']+artifact['feather']['cd']+artifact['sands']['cd']+artifact['goblet']['cd']+artifact['circlet']['cd']
            artifact_adf = copy.deepcopy(artifact)
            artifact_adf['hp']=n_hp*hp+hp_bonus
            artifact_adf['df']=(n_df)*df+df_bonus+0.466
            artifact_adf['er']=n_er*er+er_bonus
            artifact_adf['em']=n_em*em+em_bonus
            artifact_adf['cr']=n_cr*cr+0.05+cr_bonus+cryo_crit
            artifact_adf['cd']=n_cd*cd+0.5+cd_bonus+0.622
            artifact_adf['db']=d_bonus
            artifact_adf['attack'] = (n_attack)*attack+att_bonus+pyro_attack_boost+0.466
            artifact_adf['total_damage'] = calc_damagex(character,weapon,artifact,epe)
            artifact_adf['er_rolls']=n_er
            artifact_adf['em_rolls']=n_em
            artifact_adf['cr_rolls']=n_cr
            artifact_adf['cd_rolls']=n_cd
            artifact_adf['hp_rolls']=n_hp
            artifact_adf['def_rolls']=n_df
            artifact_adf['attack_rolls']=n_attack
            
    if artifact['circlet_type']=='crit damage':
        lis=[artifact_att['total_damage'],artifact_er['total_damage'],artifact_hp['total_damage'],artifact_df['total_damage'],artifact_era['total_damage'],artifact_ema['total_damage'],artifact_aa['total_damage'],artifact_ahp['total_damage'],artifact_adf['total_damage'],artifact_em['total_damage']]
        max_lis = max(lis)
        max_lis = lis.index(max_lis)
        
        if character['forced_sands']=='hp':
            if artifact_ahp['total_damage']>artifact_hp['total_damage']:
                artifact=artifact_ahp
                artifact['sands_type']='hp'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_hp
                artifact['sands_type']='hp'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='er':
            if artifact_era['total_damage']>artifact_er['total_damage']:
                artifact=artifact_era
                artifact['sands_type']='er'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_er
                artifact['sands_type']='er'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='em':
            if artifact_ema['total_damage']>artifact_em['total_damage']:
                artifact=artifact_ema
                artifact['sands_type']='em'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_em
                artifact['sands_type']='em'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='df':
            if artifact_adf['total_damage']>artifact_df['total_damage']:
                artifact=artifact_adf
                artifact['sands_type']='df'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_df
                artifact['sands_type']='df'
                artifact['goblet_type']='damage'
                return artifact
        if character['forced_sands']=='attack':
            if artifact_aa['total_damage']>artifact_att['total_damage']:
                artifact=artifact_aa
                artifact['sands_type']='attack'
                artifact['goblet_type']='attack'
                return artifact
            else:
                artifact=artifact_att
                artifact['sands_type']='attack'
                artifact['goblet_type']='damage'
                return artifact
        if max_lis==0:
            artifact=artifact_att
            artifact['sands_type']='attack'
            artifact['goblet_type']='damage'
        elif max_lis==1:
            artifact=artifact_er
            artifact['sands_type']='er'
            artifact['goblet_type']='damage'
        elif max_lis==2:
            artifact=artifact_hp
            artifact['sands_type']='hp'
            artifact['goblet_type']='damage'
        elif max_lis==3:
            artifact=artifact_df
            artifact['sands_type']='df'
            artifact['goblet_type']='damage'
        elif max_lis==4:
            artifact=artifact_era
            artifact['sands_type']='er'
            artifact['goblet_type']='attack'
        elif max_lis==5:
            artifact=artifact_ema
            artifact['sands_type']='em'
            artifact['goblet_type']='attack'
        elif max_lis==6:
            artifact=artifact_aa
            artifact['sands_type']='attack'
            artifact['goblet_type']='attack'
        elif max_lis==7:
            artifact=artifact_ahp
            artifact['sands_type']='hp'
            artifact['goblet_type']='attack'
        elif max_lis==8:
            artifact=artifact_adf
            artifact['sands_type']='df'
            artifact['goblet_type']='attack'
        elif max_lis==9:
            artifact=artifact_em
            artifact['sands_type']='em'
            artifact['goblet_type']='damage'
        return artifact