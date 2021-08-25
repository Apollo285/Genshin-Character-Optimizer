# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:40:25 2021

@author: aeapo
"""
from get_character_info import get_character_infox
from get_weapon_info import get_weapon_infox
from process_artifactx import process_artifact
from get_optimal_damage import get_optimal_damagex
from calc_damage import calc_damagex
from check_reaction import check_reactionx
from check_epe import check_epex
from check_possibility import check_possibilityx
from fill_artifact_rolls import fill_artifact_rollsx
from convert_arti import convert_artix
import copy
from calc_damage2 import calc_damagex2
def main():
    print('Spelling is immensely important, double check inputs')
    print("Don't worry about capitalization")
    character=False
    while character==False:
        character=input('Enter Character Name:')
        character = character.lower()
        character= get_character_infox(character)
    weapon =  False
    refinement = input('Enter Weapon Refinement (1-5):')
    refinement =  int(refinement)
    while weapon==False:
        weapon = input('Enter Weapon Name:')
        weapon =  weapon.lower()
        weapon =  get_weapon_infox(weapon,refinement)
    arti_set1 = False
    arti_set2 = False
    artifact = False
    temp=False
    na=input('Are you using 2 piece or 4 piece artifact? (2 or 4):')
    if int(na)==4:
        while artifact==False:
            artifact= input('What 4 piece set are you using? i.e crimson witch:')
            arti_set1=artifact
            artifact = process_artifact(arti_set1,arti_set2)
    if int(na)==2:
        while temp==False:
            temp= input('What 2 piece set are you using? i.e crimson witch:')
            arti_set1=temp
            temp = process_artifact(arti_set1,arti_set2)
        while artifact==False:
            artifact= input('What other 2 piece set are you using?:')
            arti_set2=artifact
            artifact = process_artifact(arti_set1,arti_set2)
    if arti_set2!= False:
        if arti_set1.lower()=='maiden beloved' or arti_set2.lower()=='maiden beloved':
            print("Don't Use This Set")
            return
    else:
        if arti_set1.lower()=='maiden beloved':
            print("Don't Use This Set")
            return
    if arti_set1.lower()=="shimenawa's reminiscence" and arti_set2.lower()=='false':
        print("This set is not best in slot on any character")
    character['artifact']=artifact
    check=False
    while check==False:
        type_reaction = input('What reaction do you use (type none if none):')
        type_reaction = type_reaction.lower()
        check = check_reactionx(type_reaction)
    if type_reaction != 'none':
        percent_react= input('What perctage of attacks get a reaction (i.e. 75 for 75%):')
        percent_react= int(percent_react)/100
    else:
        percent_react = 0
    if type_reaction =='vaporise':
        if character['element']=='pyro':
            character['em_mult']=1.5
        elif character['element']=='hydro':
            character['em_mult']=2
    elif type_reaction == 'melt':
        if character['element']=='pyro':
            character['em_mult']=2
        elif character['element']=='cryo':
            character['em_mult']=1.5
    character['element reaction']=type_reaction
    play_style = input('Main DPS or Quickswap?:')
    play_style = play_style.lower()
    while True:
        if play_style=='main dps' or play_style=='quickswap':
            break
        else:
            print("Enter Main DPS or Quickswap")
            play_style = input('Main DPS or Quickswap?:')
            play_style = play_style.lower()
    character['play_style']=play_style
    character['percent_react']=percent_react
    ntb = input('How many elemental party effects (0 or 1 or 2):')
    ntb=int(ntb)
    if ntb==2:
        temp=False
        while temp==False:
            epe =  input('List elemental party effect (i.e. pyro, geo...):')
            epe= epe.lower()
            temp=check_epex(epe)
        temp2=False
        while temp2==False:
            epe2 = input('List elemental party effect #2 (i.e. pyro, geo...):')
            epe2= epe2.lower()
            temp2=check_epex(epe2)
        epe= {'ntb':ntb,'epe':epe,'epe2':epe2}
    elif ntb==1:
        temp=False
        while temp==False:
            epe =  input('List elemental party effect (i.e. pyro, geo...):')
            epe= epe.lower()
            temp=check_epex(epe)
        epe= {'ntb':ntb,'epe':epe,'epe2':'none'}
    else:
        epe= {'ntb':ntb,'epe':'none','epe2':'none'}
        
    forced_sands_choice='no'
    print('If you say no, the optimizer will find the best sands to use')
    forced_sands_choice=input('Would you like to select the sands main stat? (yes or no):')
    forced_sands_choice=forced_sands_choice.lower()
    while True:
        if forced_sands_choice=='yes' or forced_sands_choice=='no':
            break
        else:
            print("Enter Yes or No")
            forced_sands_choice = input('Yes or No?:')
            forced_sands_choice = forced_sands_choice.lower()
    if forced_sands_choice == 'yes':
        print('Available Choices are (attack, defense, hp, energy recharge, elemental mastery)')
        forced_sands=input('Enter the sand type you would like to use:')
        forced_sands=forced_sands.lower()
        while True:
            if forced_sands=='attack' or forced_sands=='defense' or forced_sands=='hp' or forced_sands=='energy recharge' or forced_sands=='elemental mastery':
                break
            else:
                print('Available Choices are (attack, defense, hp, energy recharge, elemental mastery)')
                forced_sands=input('Enter the sand type you would like to use:')
                forced_sands=forced_sands.lower()
        if forced_sands=='defense':
            forced_sands='df'
        if forced_sands=='energy recharge':
            forced_sands='er'
        if forced_sands=='elemental mastery':
            forced_sands='em'
        character['forced_sands']=forced_sands
    else:
        character['forced_sands']='no'
        
    if character['name']!='bennett':
        bennett_boost=False
        bennett_boost=input('Are you using bennett with this character?:')
        bennett_boost= bennett_boost.lower()
        while True:
            if bennett_boost=='yes' or bennett_boost=='no':
                break
            else:
                print("Enter Yes or No")
                bennett_boost = input('Yes or No?:')
                bennett_boost = bennett_boost.lower()
        if bennett_boost=='yes':
            character['bennett_boost']=True
            bennett_er=input('How much energy recharge does your bennett have? (i.e 150):')
            character['bennett_er']=float(bennett_er)
        else:
            character['bennett_boost']=False
    else:
        character['bennett_boost']=True
    yn=input('Would You like to compare your character stats to the max? (yes or no):')
    yn=yn.lower()
    while True:
        if yn=='yes' or yn=='no':
            break
        else:
            print("Enter Yes or No")
            yn = input('Yes or No?:')
            yn = yn.lower()
    optimal_damage={'artifacts':{},
                    'character':{}}
    artifact = get_optimal_damagex(character, weapon,epe)
    optimal_damage['artifacts']['set']=artifact['set']
    optimal_damage['artifacts']['set2']=artifact['set2']
    optimal_damage['artifacts']['sands_type']=artifact['sands_type']
    optimal_damage['artifacts']['goblet_type']=artifact['goblet_type']
    optimal_damage['artifacts']['circlet_type']=artifact['circlet_type']
    optimal_damage['artifacts']['flower']=convert_artix(artifact['flower'])
    optimal_damage['artifacts']['feather']=convert_artix(artifact['feather'])
    optimal_damage['artifacts']['sands']=convert_artix(artifact['sands'])
    optimal_damage['artifacts']['goblet']=convert_artix(artifact['goblet'])
    optimal_damage['artifacts']['circlet']=convert_artix(artifact['circlet'])
    epe['fc']=1
    y=calc_damagex(character,weapon,artifact,epe)
    optimal_damage['character']['hp']=y['thp']
    optimal_damage['character']['attack']=y['ta']
    optimal_damage['character']['defense']=y['tdf']
    optimal_damage['character']['er']=y['er']*100
    optimal_damage['character']['em']=y['em']
    optimal_damage['character']['damage bonus']=(y['db']-1)*100
    optimal_damage['character']['cr']=y['cr']*100
    optimal_damage['character']['cd']=(1+y['cd'])*100
    cr_bonus2=0
    cd_bonus2=0
    if weapon['Main Stat']=='Cr':
        cr_bonus2+= weapon['Main Stat Bonus']
    if weapon['Main Stat']=='Cd':
        cd_bonus2+= weapon['Main Stat Bonus']
    cr = character['Cr_bonus']+0.05+cr_bonus2
    cd = character['Cd_bonus']+0.5+cd_bonus2
    if artifact['circlet_type']=='crit rate':
        cr+= 0.311 + artifact['cr_rolls']*0.039
        cd+=artifact['cd_rolls']*0.078
    if artifact['circlet_type']=='crit damage':
        cr+= artifact['cr_rolls']*0.039
        cd+= 0.622 + artifact['cd_rolls']*0.078
    optimal_damage['character']['cr']=cr*100
    optimal_damage['character']['cd']=(cd)*100
    optimal_damage['objective value']=artifact['total_damage']
    if yn=='yes':
        print("Input Character Stats After Bonuses are applied, i.e after using Hu Tao's skill")
        hp = input('Input Character Hp:')
        hp=float(hp)
        df = input('Input Character Defense:')
        df=float(df)
        er = input('Input Character Energy Recharge:')
        er=float(er)/100
        em = input('Input Character em:')
        em=float(em)
        attack = input('Input Character Attack:')
        attack=float(attack)
        cr = input('Input Character Crit Rate (i.e 72):')
        cr=float(cr)/100
        cd = input('Input Character Crit Damage:')
        cd=float(cd)/100
        db = input('Input Character Damage Bonus:')
        db=float(db)/100
        character['attackc']=attack
        character['emc']=em
        character['erc']=er
        character['crc']=cr
        character['cdc']=cd
        character['hpc']=hp
        character['dfc']=df
        character['dbc']=db
        cod=calc_damagex2(character,weapon,artifact,epe)
        y=optimal_damage['objective value']
        x=cod/y*100
        x=round(x,2)
        cn=character['name']
        x=str(x)
        pn=character['pronoun']
        xs='Your ' +cn
        xs=xs + ' is at '
        xs=xs+x
        xs=xs+'% of '
        xs=xs+ pn
        xs=xs+' damage potential'
        print(xs)
    return optimal_damage


