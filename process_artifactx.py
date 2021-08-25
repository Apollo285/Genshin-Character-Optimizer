# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:18:58 2021

@author: aeapo
"""

def process_artifact(as1, as2):
    artifact=False
    if not as2:#as2=='false':
        if as1.lower()=="gladiator's finale" or as1.lower()=="gladiators finale" :
            artifact={'ns':1,'set':'4GF','set2':'none'}
        elif as1.lower()=="wanderer's troupe" or as1.lower()=="wanderers troupe":
            artifact={'ns':1,'set':'4WT','set2':'none'}
        elif as1.lower()=="thundersoother":
            artifact={'ns':1,'set':'4TS','set2':'none'}
        elif as1.lower()=="thundering fury":
            artifact={'ns':1,'set':'4TF','set2':'none'}
        elif as1.lower()=="viridescent venerer":
            artifact={'ns':1,'set':'4VV','set2':'none'}
        elif as1.lower()=="crimson witch" or as1.lower()=='crimson witch of flames':
            artifact={'ns':1,'set':'4CW','set2':'none'}
        elif as1.lower()=="lavawalker":
            artifact={'ns':1,'set':'4LW','set2':'none'}
        elif as1.lower()=="noblesse oblige":
            artifact={'ns':1,'set':'4NO','set2':'none'}
        elif as1.lower()=="bloodstained chivalry":
            artifact={'ns':1,'set':'4BC','set2':'none'}
        elif as1.lower()=="archaic petra":
            artifact={'ns':1,'set':'4AP','set2':'none'}
        elif as1.lower()=="retracing bolide":
            artifact={'ns':1,'set':'4RB','set2':'none'}
        elif as1.lower()=="blizzard strayer":
            artifact={'ns':1,'set':'4BS','set2':'none'}
        elif as1.lower()=="heart of depth":
            artifact={'ns':1,'set':'4HD','set2':'none'}
        elif as1.lower()=="tenacity of the millelith":
            artifact={'ns':1,'set':'4TM','set2':'none'}
        elif as1.lower()=="pale flame":
            artifact={'ns':1,'set':'4PF','set2':'none'}
        elif as1.lower()=="emblem of severed fate":
            artifact={'ns':1,'set':'4EF','set2':'none'}
        elif as1.lower()=="shimenawa's reminiscence" or as1.lower()=="shimenawas reminiscence":
            artifact={'ns':1,'set':'4SR','set2':'none'}
    else:
        if as1.lower()=="gladiator's finale" or as1.lower()=="gladiators finale":
            artifact={'ns':2,'set':'2GF'}
        elif as1.lower()=="wanderer's troupe" or as1.lower()=="wanderers troupe":
            artifact={'ns':2,'set':'2WT'}
        elif as1.lower()=="thundersoother":
            artifact={'ns':2,'set':'2TS'}
        elif as1.lower()=="thundering fury":
            artifact={'ns':2,'set':'2TF'}
        elif as1.lower()=="viridescent venerer":
            artifact={'ns':2,'set':'2VV'}
        elif as1.lower()=="crimson witch" or as1.lower()=='crimson witch of flames':
            artifact={'ns':2,'set':'2CW'}
        elif as1.lower()=="lavawalker":
            artifact={'ns':2,'set':'2LW'}
        elif as1.lower()=="noblesse oblige":
            artifact={'ns':2,'set':'2NO'}
        elif as1.lower()=="bloodstained chivalry":
            artifact={'ns':2,'set':'2BC'}
        elif as1.lower()=="archaic petra":
            artifact={'ns':2,'set':'2AP'}
        elif as1.lower()=="retracing bolide":
            artifact={'ns':2,'set':'2RB'}
        elif as1.lower()=="blizzard strayer":
            artifact={'ns':2,'set':'2BS'}
        elif as1.lower()=="heart of depth":
            artifact={'ns':2,'set':'2HD'}
        elif as1.lower()=="tenacity of the millelith":
            artifact={'ns':2,'set':'2TM'}
        elif as1.lower()=="pale flame":
            artifact={'ns':2,'set':'2PF'}
        elif as1.lower()=="emblem of severed fate":
            artifact={'ns':2,'set':'2EF'}
        elif as1.lower()=="shimenawa's reminiscence" or as1.lower()=="shimenawas reminiscence":
            artifact={'ns':2,'set':'2SR'}
            
        if as2.lower()=="gladiator's finale" or as2.lower()=="gladiators finale":
            artifact['set2']='2GF'
        elif as2.lower()=="wanderer's troupe" or as2.lower()=="wanderers troupe":
            artifact['set2']='2WT'
        elif as2.lower()=="thundersoother":
            artifact['set2']='2TS'
        elif as2.lower()=="thundering fury":
            artifact['set2']='2TF'
        elif as2.lower()=="viridescent venerer":
            artifact['set2']='2VV'
        elif as2.lower()=="crimson witch" or as1.lower()=='crimson witch of flames':
            artifact['set2']='2CW'
        elif as2.lower()=="lavawalker":
            artifact['set2']='2LW'
        elif as2.lower()=="noblesse oblige":
            artifact['set2']='2NO'
        elif as2.lower()=="bloodstained chivalry":
            artifact['set2']='2BC'
        elif as2.lower()=="archaic petra":
            artifact['set2']='2AP'
        elif as2.lower()=="retracing bolide":
            artifact['set2']='2RB'
        elif as2.lower()=="blizzard strayer":
            artifact['set2']='2BS'
        elif as2.lower()=="heart of depth":
            artifact['set2']='2HD'
        elif as2.lower()=="tenacity of the millelith":
            artifact['set2']='2TM'
        elif as2.lower()=="pale flame":
            artifact['set2']='2PF'
        elif as2.lower()=="emblem of severed fate":
            artifact['set2']='2EF'
        elif as2.lower()=="shimenawa's reminiscence" or as2.lower()=="shimenawas reminiscence":
            artifact['set2']='2SR'
    if artifact==False:
        print('Invalid Artifact Selection')
    if as2 !=False:
        if not 'set2' in artifact:
           artifact=False
           print('Invalid Artifact Selection')
    return artifact