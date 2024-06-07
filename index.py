import requests
import json
import pandas as pd
from requests import get
import random
from itertools import product
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import random
import ast
import asyncio

pos1_list = ['medusa', 'tb', 'bs', 'morph', 'mk'  ]
pos2_list = ['ember', 'bat', 'storm', 'void', 'pango']
pos3_list = ['doom', 'beast', 'sb', 'timber', 'underlord']
pos4_list = ['techies', 'ench', 'undying', 'sky', 'mirana']
pos5_list = ['rubick', 'pugna', 'silencer', 'cm', 'disruptor']

pos1 = ['medusa', 'terrorblade', 'bloodseeker', 'morphling', 'monkey_king']
pos2 = ['ember_spirit', 'batrider', 'storm_spirit', 'void', 'void_spirit']
pos3 = ['doom_bringer', 'beastmaster', 'spirit_breaker', 'shredder', 'underlord']
pos4 = ['techies', 'enchantress', 'undying', 'skywrath_mage', 'mirana']
pos5 = ['rubick', 'pugna', 'silencer', 'crystal_maiden', 'disruptor']

heroes= [
    {
        "name": "npc_dota_hero_dummy",
        "id": 0
    },
    {
        "name": "npc_dota_hero_antimage",
        "id": 1
    },
    {
        "name": "npc_dota_hero_axe",
        "id": 2
    },
    {
        "name": "npc_dota_hero_bane",
        "id": 3
    },
    {
        "name": "npc_dota_hero_bloodseeker",
        "id": 4
    },
    {
        "name": "npc_dota_hero_crystal_maiden",
        "id": 5
    },
    {
        "name": "npc_dota_hero_drow_ranger",
        "id": 6
    },
    {
        "name": "npc_dota_hero_earthshaker",
        "id": 7
    },
    {
        "name": "npc_dota_hero_juggernaut",
        "id": 8
    },
    {
        "name": "npc_dota_hero_mirana",
        "id": 9
    },
    {
        "name": "npc_dota_hero_nevermore",
        "id": 11
    },
    {
        "name": "npc_dota_hero_morphling",
        "id": 10
    },
    {
        "name": "npc_dota_hero_phantom_lancer",
        "id": 12
    },
    {
        "name": "npc_dota_hero_puck",
        "id": 13
    },
    {
        "name": "npc_dota_hero_pudge",
        "id": 14
    },
    {
        "name": "npc_dota_hero_razor",
        "id": 15
    },
    {
        "name": "npc_dota_hero_sand_king",
        "id": 16
    },
    {
        "name": "npc_dota_hero_storm_spirit",
        "id": 17
    },
    {
        "name": "npc_dota_hero_sven",
        "id": 18
    },
    {
        "name": "npc_dota_hero_tiny",
        "id": 19
    },
    {
        "name": "npc_dota_hero_vengefulspirit",
        "id": 20
    },
    {
        "name": "npc_dota_hero_windrunner",
        "id": 21
    },
    {
        "name": "npc_dota_hero_zuus",
        "id": 22
    },
    {
        "name": "npc_dota_hero_kunkka",
        "id": 23
    },
    {
        "name": "npc_dota_hero_lina",
        "id": 25
    },
    {
        "name": "npc_dota_hero_lich",
        "id": 31
    },
    {
        "name": "npc_dota_hero_lion",
        "id": 26
    },
    {
        "name": "npc_dota_hero_shadow_shaman",
        "id": 27
    },
    {
        "name": "npc_dota_hero_slardar",
        "id": 28
    },
    {
        "name": "npc_dota_hero_tidehunter",
        "id": 29
    },
    {
        "name": "npc_dota_hero_witch_doctor",
        "id": 30
    },
    {
        "name": "npc_dota_hero_riki",
        "id": 32
    },
    {
        "name": "npc_dota_hero_enigma",
        "id": 33
    },
    {
        "name": "npc_dota_hero_tinker",
        "id": 34
    },
    {
        "name": "npc_dota_hero_sniper",
        "id": 35
    },
    {
        "name": "npc_dota_hero_necrolyte",
        "id": 36
    },
    {
        "name": "npc_dota_hero_warlock",
        "id": 37
    },
    {
        "name": "npc_dota_hero_beastmaster",
        "id": 38
    },
    {
        "name": "npc_dota_hero_queenofpain",
        "id": 39
    },
    {
        "name": "npc_dota_hero_venomancer",
        "id": 40
    },
    {
        "name": "npc_dota_hero_faceless_void",
        "id": 41
    },
    {
        "name": "npc_dota_hero_skeleton_king",
        "id": 42
    },
    {
        "name": "npc_dota_hero_death_prophet",
        "id": 43
    },
    {
        "name": "npc_dota_hero_phantom_assassin",
        "id": 44
    },
    {
        "name": "npc_dota_hero_pugna",
        "id": 45
    },
    {
        "name": "npc_dota_hero_templar_assassin",
        "id": 46
    },
    {
        "name": "npc_dota_hero_viper",
        "id": 47
    },
    {
        "name": "npc_dota_hero_luna",
        "id": 48
    },
    {
        "name": "npc_dota_hero_dragon_knight",
        "id": 49
    },
    {
        "name": "npc_dota_hero_dazzle",
        "id": 50
    },
    {
        "name": "npc_dota_hero_rattletrap",
        "id": 51
    },
    {
        "name": "npc_dota_hero_leshrac",
        "id": 52
    },
    {
        "name": "npc_dota_hero_furion",
        "id": 53
    },
    {
        "name": "npc_dota_hero_life_stealer",
        "id": 54
    },
    {
        "name": "npc_dota_hero_dark_seer",
        "id": 55
    },
    {
        "name": "npc_dota_hero_clinkz",
        "id": 56
    },
    {
        "name": "npc_dota_hero_omniknight",
        "id": 57
    },
    {
        "name": "npc_dota_hero_enchantress",
        "id": 58
    },
    {
        "name": "npc_dota_hero_huskar",
        "id": 59
    },
    {
        "name": "npc_dota_hero_night_stalker",
        "id": 60
    },
    {
        "name": "npc_dota_hero_broodmother",
        "id": 61
    },
    {
        "name": "npc_dota_hero_bounty_hunter",
        "id": 62
    },
    {
        "name": "npc_dota_hero_weaver",
        "id": 63
    },
    {
        "name": "npc_dota_hero_jakiro",
        "id": 64
    },
    {
        "name": "npc_dota_hero_batrider",
        "id": 65
    },
    {
        "name": "npc_dota_hero_chen",
        "id": 66
    },
    {
        "name": "npc_dota_hero_spectre",
        "id": 67
    },
    {
        "name": "npc_dota_hero_doom_bringer",
        "id": 69
    },
    {
        "name": "npc_dota_hero_ancient_apparition",
        "id": 68
    },
    {
        "name": "npc_dota_hero_ursa",
        "id": 70
    },
    {
        "name": "npc_dota_hero_spirit_breaker",
        "id": 71
    },
    {
        "name": "npc_dota_hero_gyrocopter",
        "id": 72
    },
    {
        "name": "npc_dota_hero_alchemist",
        "id": 73
    },
    {
        "name": "npc_dota_hero_invoker",
        "id": 74
    },
    {
        "name": "npc_dota_hero_silencer",
        "id": 75
    },
    {
        "name": "npc_dota_hero_obsidian_destroyer",
        "id": 76
    },
    {
        "name": "npc_dota_hero_lycan",
        "id": 77
    },
    {
        "name": "npc_dota_hero_brewmaster",
        "id": 78
    },
    {
        "name": "npc_dota_hero_shadow_demon",
        "id": 79
    },
    {
        "name": "npc_dota_hero_lone_druid",
        "id": 80
    },
    {
        "name": "npc_dota_hero_chaos_knight",
        "id": 81
    },
    {
        "name": "npc_dota_hero_meepo",
        "id": 82
    },
    {
        "name": "npc_dota_hero_treant",
        "id": 83
    },
    {
        "name": "npc_dota_hero_ogre_magi",
        "id": 84
    },
    {
        "name": "npc_dota_hero_undying",
        "id": 85
    },
    {
        "name": "npc_dota_hero_rubick",
        "id": 86
    },
    {
        "name": "npc_dota_hero_disruptor",
        "id": 87
    },
    {
        "name": "npc_dota_hero_nyx_assassin",
        "id": 88
    },
    {
        "name": "npc_dota_hero_naga_siren",
        "id": 89
    },
    {
        "name": "npc_dota_hero_keeper_of_the_light",
        "id": 90
    },
    {
        "name": "npc_dota_hero_wisp",
        "id": 91
    },
    {
        "name": "npc_dota_hero_visage",
        "id": 92
    },
    {
        "name": "npc_dota_hero_slark",
        "id": 93
    },
    {
        "name": "npc_dota_hero_medusa",
        "id": 94
    },
    {
        "name": "npc_dota_hero_troll_warlord",
        "id": 95
    },
    {
        "name": "npc_dota_hero_centaur",
        "id": 96
    },
    {
        "name": "npc_dota_hero_magnataur",
        "id": 97
    },
    {
        "name": "npc_dota_hero_shredder",
        "id": 98
    },
    {
        "name": "npc_dota_hero_bristleback",
        "id": 99
    },
    {
        "name": "npc_dota_hero_tusk",
        "id": 100
    },
    {
        "name": "npc_dota_hero_skywrath_mage",
        "id": 101
    },
    {
        "name": "npc_dota_hero_abaddon",
        "id": 102
    },
    {
        "name": "npc_dota_hero_elder_titan",
        "id": 103
    },
    {
        "name": "npc_dota_hero_legion_commander",
        "id": 104
    },
    {
        "name": "npc_dota_hero_techies",
        "id": 105
    },
    {
        "name": "npc_dota_hero_ember_spirit",
        "id": 106
    },
    {
        "name": "npc_dota_hero_earth_spirit",
        "id": 107
    },
    {
        "name": "npc_dota_hero_underlord",
        "id": 108
    },
    {
        "name": "npc_dota_hero_terrorblade",
        "id": 109
    },
    {
        "name": "npc_dota_hero_phoenix",
        "id": 110
    },
    {
        "name": "npc_dota_hero_oracle",
        "id": 111
    },
    {
        "name": "npc_dota_hero_winter_wyvern",
        "id": 112
    },
    {
        "name": "npc_dota_hero_arc_warden",
        "id": 113
    },
    {
        "name": "npc_dota_hero_monkey_king",
        "id": 114
    },
    {
        "name": "npc_dota_hero_dark_willow",
        "id": 119
    },
    {
        "name": "npc_dota_hero_pangolier",
        "id": 120
    },
    {
        "name": "npc_dota_hero_grimstroke",
        "id": 121
    },
    {
        "name": "npc_dota_hero_hoodwink",
        "id": 123
    },
    {
        "name": "npc_dota_hero_void_spirit",
        "id": 126
    },
    {
        "name": "npc_dota_hero_snapfire",
        "id": 128
    },
    {
        "name": "npc_dota_hero_mars",
        "id": 129
    },
    {
        "name": "npc_dota_hero_dawnbreaker",
        "id": 135
    },
    {
        "name": "npc_dota_hero_marci",
        "id": 136
    },
    {
        "name": "npc_dota_hero_primal_beast",
        "id": 137
    },
    {
        "name": "npc_dota_hero_muerta",
        "id": 138
    },   
]

def matchDetailProcessing(matches, heronames):
    matches.dropna(inplace=True)
    # for hero in heronames:
    matches = (matches[matches['heroId'].isin(heronames)])

    # reset index
    matches.reset_index(inplace=True, drop=True)

    # loop over columns
    data = []

    for i in range(1, len(matches.columns)):
        # create buffer list
        temp = []

        # get column name
        name = matches.columns[i]

        # find quartile
        q1 = round(matches.iloc[:, i].quantile(0.25), 2)
        q2 = round(matches.iloc[:, i].quantile(0.50), 2)
        q3 = round(matches.iloc[:, i].quantile(0.75), 2)

        # append to temp list
        temp.append(name)
        temp.append(q1)
        temp.append(q2)
        temp.append(q3)
        data.append(temp)

    data = pd.DataFrame(data, columns=['variable', 'q1', 'q2', 'q3'])

    return data

def getAllFuzzyLimits():
    pos1_limits = matchDetailProcessing(all_matches,pos1)

    # add new column at the front of dataframe
    pos1_limits.insert(0, 'pos', 'pos1')

    # insert the rest of the label
    pos2_limits = matchDetailProcessing(all_matches,pos2)
    pos2_limits['pos'] = 'pos2'
    pos3_limits = matchDetailProcessing(all_matches,pos3)
    pos3_limits['pos'] = 'pos3'
    pos4_limits = matchDetailProcessing(all_matches,pos4)
    pos4_limits['pos'] = 'pos4'
    pos5_limits = matchDetailProcessing(all_matches,pos5)
    pos5_limits['pos'] = 'pos5'

    #combine all dataframe
    all_limits = pd.concat([pos1_limits, pos2_limits, pos3_limits, pos4_limits, pos5_limits])

    # reset index
    all_limits.reset_index(inplace=True, drop=True)

    return all_limits


def boxGraph(matches):
    fig = make_subplots(rows=9, cols=1, shared_yaxes=True, subplot_titles=('KDA Distribution', 'GPM Distribution', 'XPM Distribution', 'Damage Dealt Distribution', 'Damage Taken Distribution', 'Tower Damage Distribution', 'Control Duration Distribution', 'Ward Planted Distribution', 'Ward Destroyed Distribution'))
    fig.add_trace(go.Box(x=all_matches['kda'], name='KDA'), row=1, col=1)
    fig.add_trace(go.Box(x=all_matches['gpm'], name='gpm'), row=2, col=1)
    fig.add_trace(go.Box(x=all_matches['xpm'], name='xpm'), row=3, col=1)
    fig.add_trace(go.Box(x=all_matches['damageDealt'], name='damageDealt'), row=4, col=1)
    fig.add_trace(go.Box(x=all_matches['damageTaken'], name='damageTaken'), row=5, col=1)
    fig.add_trace(go.Box(x=all_matches['towerDamage'], name='towerDamage'), row=6, col=1)
    fig.add_trace(go.Box(x=all_matches['controlDuration'], name='controlDuration'), row=7, col=1)
    fig.add_trace(go.Box(x=all_matches['wardPlanted'], name='wardPlanted'), row=8, col=1)
    fig.add_trace(go.Box(x=all_matches['wardDestroyed'], name='wardDestroyed'), row=9, col=1)
    fig.update_layout(height=1200, width=800)
    st.plotly_chart(fig)
    
    
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNDdkZGU5YzYtZmVlZi00ZGM4LWI5ZTMtZTIxNDNhODIwOWNjIiwiU3RlYW1JZCI6IjMwMTQ5ODE3NSIsIm5iZiI6MTY5MTgzNTcyNSwiZXhwIjoxNzIzMzcxNzI1LCJpYXQiOjE2OTE4MzU3MjUsImlzcyI6Imh0dHBzOi8vYXBpLnN0cmF0ei5jb20ifQ.so3b8DWeUWMIKGEug2V49YvizzUK8VGsFSRkZMJmdgM'

def getAuthHeader(token):
    return {'Authorization': 'Bearer ' + token}

def getItem(token, itemID):
    url = f'https://api.stratz.com/api/v1/Item/{itemID}'
    headers = getAuthHeader(token)
    result = get(url, headers=headers)  
    json_result = json.loads(result.content)  
    return json_result
    
def getMatch(token, matchID):
    url = f'https://api.stratz.com/api/v1/match/{matchID}/breakdown'
    headers = getAuthHeader(token)
    result = get(url, headers=headers)  
    json_result = json.loads(result.content)
    return json_result

def getHeroName(heroId):
    for hero in heroes:
        if hero['id'] == heroId:
            return hero['name'][14:]
    return heroId

def TotalWardPlanted(x):
    count = 0
    for i in x :
        if i['type'] == 0:
            count += 1
    return count

def TotalWardDestroyed(x):
    count = 0
    for i in x :
        if i['isWard'] == False:
            count += 1
    return count

def matchDetailAggregator (matchid):
    result = pd.DataFrame(columns=['heroId','kda','gpm','xpm','damageDealt','damageTaken','towerDamage','controlDuration','wardPlanted','wardDestroyed'])
    for id in matchid:
        scraped = getMatch(token, id)
        # check.append(len(scraped['players'][0]))
        # print(check)
        if (len(scraped['players'][0]) > 37):
            for i in range(10):
                data = []
                data.append(getHeroName(scraped['players'][i]['heroId']))
                if scraped['players'][i]['numDeaths'] == 0:
                    death = 1
                else:
                    death = scraped['players'][i]['numDeaths']
                data.append(round(((scraped['players'][i]['numKills']+scraped['players'][i]['numAssists'])/death),2))
                data.append(scraped['players'][i]['goldPerMinute'])
                data.append(scraped['players'][i]['experiencePerMinute'])
                data.append(scraped['players'][i]['heroDamage'])
                data.append(scraped['players'][i]['stats']['heroDamageReport']['receivedTotal']['physicalDamage']+scraped['players'][i]['stats']['heroDamageReport']['receivedTotal']['magicalDamage']+scraped['players'][i]['stats']['heroDamageReport']['receivedTotal']['pureDamage'])
                data.append(scraped['players'][i]['towerDamage'])
                data.append(int(scraped['players'][i]['stats']['heroDamageReport']['receivedTotal']['disableDuration'] + (scraped['players'][i]['stats']['heroDamageReport']['receivedTotal']['slowDuration']/2)))
                data.append(TotalWardPlanted(scraped['players'][i]['stats']['wardPlaced']))
                data.append(TotalWardDestroyed(scraped['players'][i]['stats']['wardDestruction']))
                #insert data into result dataframe
                result.loc[len(result)] = data

    return result


def fuzzify (bot,mid,top,x):
    if x <= bot:
        return [1,0,0]

    if x >= top:
        return [0,0,1]

    if x == mid:
        return [0,1,0]

    if x > mid :
        mu_mid = (top - x) / (top - mid)
        mu_top = (x - mid) / (top - mid)
        if round(mu_mid,2) + round(mu_top,2) == 1:
            return [0, round(mu_mid,2), round(mu_top,2)]
        else:
            return "calculation error"
    
    if x < mid :
        mu_bot = (mid - x) / (mid - bot)
        mu_mid = (x - bot) / (mid - bot)
        if round(mu_bot,2) + round(mu_mid,2) == 1:
            return [round(mu_bot,2), round(mu_mid,2), 0]
        else:
            return "calculation error"
        
def calculateMuValues(matchid, limits):
    match0 = matchDetailAggregator([matchid])
    total = []
    for j in range (0,10):
        for i in range (0,44,9):
            if i == 0:
                pos = 'pos1'
            elif i == 9:
                pos = 'pos2'
            elif i == 18:
                pos = 'pos3'
            elif i == 27:
                pos = 'pos4'
            elif i == 36:
                pos = 'pos5'

            mu ={
                'hero' : match0.iloc[j,0],
                'pos' : pos,
                'kda' : fuzzify(limits.loc[i,'q1'], limits.loc[i,'q2'], limits.loc[i,'q3'], match0.iloc[j,1]),
                'gpm' : fuzzify(limits.loc[i+1,'q1'], limits.loc[i+1,'q2'], limits.loc[1,'q3'], match0.iloc[j,2]),
                'xpm' : fuzzify(limits.loc[i+2,'q3'], limits.loc[i+2,'q2'], limits.loc[2,'q3'], match0.iloc[j,3]),
                'damageDealt' : fuzzify(limits.loc[i+3,'q3'], limits.loc[i+3,'q2'], limits.loc[3,'q3'], match0.iloc[j,4]),
                'damageTaken' : fuzzify(limits.loc[i+4,'q3'], limits.loc[i+4,'q2'], limits.loc[4,'q3'], match0.iloc[j,5]),
                'towerDamage' : fuzzify(limits.loc[i+5,'q3'], limits.loc[i+5,'q2'], limits.loc[5,'q3'], match0.iloc[j,6]),
                'controlDuration' : fuzzify(limits.loc[i+6,'q3'], limits.loc[i+6,'q2'], limits.loc[6,'q3'], match0.iloc[j,7]),
                'wardPlanted' : fuzzify(limits.loc[i+7,'q3'], limits.loc[i+7,'q2'], limits.loc[7,'q3'], match0.iloc[j,8]),
                'wardDestroyed' : fuzzify(limits.loc[i+8,'q3'], limits.loc[i+8,'q2'], limits.loc[8,'q3'], match0.iloc[j,9]),
            }
            total.append(mu)

    print(total)
    return total

def check_conditions_4vars(x):
    if x == 1:
        return 'low'
    elif x == 2:
        return 'medium'
    elif x == 3:
        return 'high'
    elif 3 < x < 7:
        return 'bad'
    elif 6 < x < 9:
        return 'decent'
    else:
        return 'good'

def check_conditions_3vars(x):
    if x <= 1:
        return 'low'
    elif x == 2:
        return 'medium'
    elif x == 3:
        return 'high'
    elif 3 < x < 6:
        return 'bad'
    elif 5 < x < 8:
        return 'decent'
    else:
        return 'good'

def createInferenceTableValues (variables):
    # create buffer dictionary
    var_dict = {}

    # construct initial weight of the variables
    for variable in variables:
        var_dict[variable] = (1,2,3)

    # calculate dot product
    inference_table = pd.DataFrame(list(product(*var_dict.values())), columns=var_dict.keys())

    # calculate total points on entire row, put in a new 'total' column
    inference_table['total'] = inference_table.sum(axis=1)

    return inference_table

def createInferenceTable (variables):
    # create buffer dictionary
    var_dict = {}

    # construct initial weight of the variables
    for variable in variables:
        var_dict[variable] = (1,2,3)

    # calculate dot product
    inference_table = pd.DataFrame(list(product(*var_dict.values())), columns=var_dict.keys())

    # calculate total points on entire row, put in a new 'total' column
    inference_table['total'] = inference_table.sum(axis=1)

    # for 4 variables (core position)
    if len(variables) == 4:
        for i in range(len(inference_table.columns)):
            inference_table.iloc[:,i] = inference_table.iloc[:,i].apply(check_conditions_4vars)
    
    # this one is for 3 variables (support position)
    else:
        for i in range(len(inference_table.columns)):
            inference_table.iloc[:,i] = inference_table.iloc[:,i].apply(check_conditions_3vars)
        inference_table.iloc[0,3] = 'bad' # lowest score value is 3, result in "high" instead of "low, decent, high"

    return inference_table

def getAllRulesValues():
    pos1_rules = createInferenceTableValues(['kda','gpm','damageDealt','towerDamage'])
    pos1_rules.insert(0, 'pos', 'pos1')
    
    pos2_rules = createInferenceTableValues(['kda','gpm','xpm','damageDealt'])
    pos2_rules['pos'] = 'pos2'
    pos3_rules = createInferenceTableValues(['kda','gpm','damageTaken','controlDuration'])
    pos3_rules['pos'] = 'pos3'
    pos4_rules = createInferenceTableValues(['kda','controlDuration','wardPlanted'])
    pos4_rules['pos'] = 'pos4'
    pos5_rules = createInferenceTableValues(['controlDuration', 'wardPlanted', 'wardDestroyed'])
    pos5_rules['pos'] = 'pos5'

    all_rules = pd.concat([pos1_rules, pos2_rules, pos3_rules, pos4_rules, pos5_rules])

    # reset index
    all_rules.reset_index(inplace=True, drop=True)

    # move total column to end of dataframe
    all_rules = all_rules[['pos','kda','gpm','xpm','damageDealt','damageTaken','towerDamage','controlDuration','wardPlanted','wardDestroyed', 'total']]
    
    # replace nan values with "none"
    all_rules = all_rules.fillna('none')

    return all_rules

def getAllRules():
    pos1_rules = createInferenceTable(['kda','gpm','damageDealt','towerDamage'])
    pos1_rules.insert(0, 'pos', 'pos1')
    
    pos2_rules = createInferenceTable(['kda','gpm','xpm','damageDealt'])
    pos2_rules['pos'] = 'pos2'
    pos3_rules = createInferenceTable(['kda','gpm','damageTaken','controlDuration'])
    pos3_rules['pos'] = 'pos3'
    pos4_rules = createInferenceTable(['kda','controlDuration','wardPlanted'])
    pos4_rules['pos'] = 'pos4'
    pos5_rules = createInferenceTable(['controlDuration', 'wardPlanted', 'wardDestroyed'])
    pos5_rules['pos'] = 'pos5'

    all_rules = pd.concat([pos1_rules, pos2_rules, pos3_rules, pos4_rules, pos5_rules])

    # reset index
    all_rules.reset_index(inplace=True, drop=True)

    # move total column to end of dataframe
    all_rules = all_rules[['pos','kda','gpm','xpm','damageDealt','damageTaken','towerDamage','controlDuration','wardPlanted','wardDestroyed', 'total']]
    
    # replace nan values with "none"
    all_rules = all_rules.fillna('none')

    return all_rules

def getRandomizedSample():
    # generate 3 random numbers
    random.seed(time.time_ns())
    sample_low = []
    sample_med = []
    sample_high = []

    for i in range(3):
        sample_low.append(random.randint(0,25))
        sample_med.append(random.randint(26,74))
        sample_high.append(random.randint(75,100))

    return [sample_low, sample_med, sample_high]

def defuzzification(inferenced_table):
    # Defuzzification
    bad = []
    decent = []
    good = []

    for cols in inferenced_table:
        # drop columns
        if inferenced_table.loc[0,cols] == 'none':
            inferenced_table.drop(columns=[cols], inplace=True)
            
    for i in range(len(inferenced_table)):
        if inferenced_table.loc[i,'total'] == 'bad':
            temp = min(inferenced_table.iloc[i,1:-1])
            # print(temp)
            bad.append(temp)

        if inferenced_table.loc[i,'total'] == 'decent':
            temp = min(inferenced_table.iloc[i,1:-1])
            # print(temp)
            decent.append(temp)

        if inferenced_table.loc[i,'total'] == 'good':
            temp = min(inferenced_table.iloc[i,1:-1])
            # print(temp)
            good.append(temp)

    max_bad = max(bad)
    max_decent = max(decent)
    max_good = max(good)

    return [max_bad, max_decent, max_good]

def getMatchByID(matchid,fuzzy_limits):
    fuzzified_match = calculateMuValues(matchid, fuzzy_limits)
    fuzzified_match = pd.DataFrame(fuzzified_match)
    fuzzified_match.to_csv(f'{matchid}.csv', index=False)
    fuzzified_match = pd.read_csv(f'{matchid}.csv')
    return fuzzified_match

def get_inference_data(inference_rules):
    return {f'pos{i}_inference': pd.DataFrame(inference_rules[inference_rules['pos'] == f'pos{i}']).reset_index(drop=True) for i in range(1, 6)}

def display_match_details(selectedMatch, fuzzified_match):
    st.write('## Statistik Match')
    st.write(selectedMatch)
    st.write('## Nilai Fuzzy')
    st.write(fuzzified_match)

def display_hero_positions(selectedMatch):
    st.write('## Pilih Posisi Hero')

    pos_ref=['pos1-carry', 'pos2-midlaner', 'pos3-offlane', 'pos4-roamer', 'pos5-support']
    
    st.write('Masing-masing team harus mempunyai posisi 1-5')

    col1, col2 = st.columns(2)

    with col1:
        st.write('### Radiant')
        pos1r = st.selectbox(selectedMatch.iloc[0,0], pos_ref, index=0)
        pos2r = st.selectbox(selectedMatch.iloc[1,0], pos_ref, index=1)
        pos3r = st.selectbox(selectedMatch.iloc[2,0], pos_ref, index=2)
        pos4r = st.selectbox(selectedMatch.iloc[3,0], pos_ref, index=3)
        pos5r = st.selectbox(selectedMatch.iloc[4,0], pos_ref, index=4)
        pos_radiant = [pos1r, pos2r, pos3r, pos4r, pos5r]
        if len(set(pos_radiant)) == len(pos_radiant):
            radiant=True
            st.markdown(''':green[VALID]''')
        else:
            radiant=False
            st.markdown(''':red[INVALID, pilih satu posisi di setiap hero]''')

    with col2:
        st.write('### Dire')
        pos1d=st.selectbox(selectedMatch.iloc[5,0], pos_ref, index=0)
        pos2d=st.selectbox(selectedMatch.iloc[6,0], pos_ref, index=1)
        pos3d=st.selectbox(selectedMatch.iloc[7,0], pos_ref, index=2)
        pos4d=st.selectbox(selectedMatch.iloc[8,0], pos_ref, index=3)
        pos5d=st.selectbox(selectedMatch.iloc[9,0], pos_ref, index=4)
        pos_dire = [pos1d, pos2d, pos3d, pos4d, pos5d]
        if len(set(pos_dire)) == len(pos_dire):
            dire=True
            st.markdown(''':green[VALID]''')
        else:
            dire=False
            st.markdown(''':red[INVALID, pilih satu posisi di setiap hero]''')
    
    if radiant and dire:
        return pos_radiant + pos_dire
    else:
        return False
    
def position_checking(pos_selection):
    poscol1=['pos1-carry', 'pos2-midlaner', 'pos3-offlane', 'pos4-roamer', 'pos5-support']
    
    # check if there is only two occurences of each position
    for pos in poscol1:
        if pos_selection.count(pos) != 2:
            return False
    return True

def final_calculation(fuzzified_match, pos1_inference, pos2_inference, pos3_inference, pos4_inference, pos5_inference):
    heroes = fuzzified_match['hero'].unique()
    finaltable = pd.DataFrame(columns=['hero','pos1','pos2','pos3','pos4','pos5'])
    randomsample = getRandomizedSample()

    for hero in heroes:
        # separate the full hero list to one heroes each
        selectedhero = fuzzified_match[fuzzified_match['hero'] == hero]
        # print(selectedhero)
    
        entry = []
        entry.append(hero)
        # loop over all heroes
        for i in range (len(selectedhero)):        
            # perform calculation for pos1 on current hero
            if selectedhero.iloc[i,1] == 'pos1':
                pos1_inferenced = pos1_inference.copy()
                for cols in pos1_inferenced.columns[1:-1]:
                    # drop unnecessary column so we have the same column as inference table
                    pos1_fuzzy = selectedhero.drop(columns=['hero','pos'])

                    # turn list of strings to list of float numbers
                    fuzzyvalues = [[float(num) for num in item.strip('[]').split(',')] for item in pos1_fuzzy[cols]]

                    # replace categorical values in inference table with numerical fuzzy values in fuzzyvalues list
                    pos1_inferenced[cols] = pos1_inferenced[cols].replace('low',fuzzyvalues[i][0])
                    pos1_inferenced[cols] = pos1_inferenced[cols].replace('medium',fuzzyvalues[i][1])
                    pos1_inferenced[cols] = pos1_inferenced[cols].replace('high',fuzzyvalues[i][2])

                # put inferenced table into defuzzification function
                pos1_fuzzified = defuzzification(pos1_inferenced)
                
                # final calculation based on randomized sample and defuzzified values
                pos1_final = ((pos1_fuzzified[0] * sum(randomsample[0])) + (pos1_fuzzified[1] * sum(randomsample[1])) + (pos1_fuzzified[2] * sum(randomsample[2])) / ((pos1_fuzzified[0] * len(randomsample[0])) + (pos1_fuzzified[1] * len(randomsample[1])) + (pos1_fuzzified[2] * len(randomsample[2])))) 
                entry.append(round((pos1_final),2))

            if selectedhero.iloc[i,1] == 'pos2':
                pos2_inferenced = pos2_inference.copy()
                for cols in pos2_inferenced.columns[1:-1]:
                    pos2_fuzzy = selectedhero.drop(columns=['hero','pos'])
                    fuzzyvalues = [[float(num) for num in item.strip('[]').split(',')] for item in pos2_fuzzy[cols]]
                    pos2_inferenced[cols] = pos2_inferenced[cols].replace('low',fuzzyvalues[i][0])
                    pos2_inferenced[cols] = pos2_inferenced[cols].replace('medium',fuzzyvalues[i][1])
                    pos2_inferenced[cols] = pos2_inferenced[cols].replace('high',fuzzyvalues[i][2])
                pos2_fuzzified = defuzzification(pos2_inferenced)
                pos2_final = ((pos2_fuzzified[0] * sum(randomsample[0])) + (pos2_fuzzified[1] * sum(randomsample[1])) + (pos2_fuzzified[2] * sum(randomsample[2])) / ((pos2_fuzzified[0] * len(randomsample[0])) + (pos2_fuzzified[1] * len(randomsample[1])) + (pos2_fuzzified[2] * len(randomsample[2])))) 
                entry.append(round((pos2_final),2))

            if selectedhero.iloc[i,1] == 'pos3':
                pos3_inferenced = pos3_inference.copy()
                for cols in pos3_inferenced.columns[1:-1]:
                    pos3_fuzzy = selectedhero.drop(columns=['hero','pos'])
                    fuzzyvalues = [[float(num) for num in item.strip('[]').split(',')] for item in pos3_fuzzy[cols]]
                    pos3_inferenced[cols] = pos3_inferenced[cols].replace('low',fuzzyvalues[i][0])
                    pos3_inferenced[cols] = pos3_inferenced[cols].replace('medium',fuzzyvalues[i][1])
                    pos3_inferenced[cols] = pos3_inferenced[cols].replace('high',fuzzyvalues[i][2])
                pos3_fuzzified = defuzzification(pos3_inferenced)
                pos3_final = ((pos3_fuzzified[0] * sum(randomsample[0])) + (pos3_fuzzified[1] * sum(randomsample[1])) + (pos3_fuzzified[2] * sum(randomsample[2])) / ((pos3_fuzzified[0] * len(randomsample[0])) + (pos3_fuzzified[1] * len(randomsample[1])) + (pos3_fuzzified[2] * len(randomsample[2])))) 
                entry.append(round((pos3_final),2))

            if selectedhero.iloc[i,1] == 'pos4':
                pos4_inferenced = pos4_inference.copy()
                for cols in pos4_inferenced.columns[1:-1]:
                    pos4_fuzzy = selectedhero.drop(columns=['hero','pos'])
                    fuzzyvalues = [[float(num) for num in item.strip('[]').split(',')] for item in pos4_fuzzy[cols]]
                    pos4_inferenced[cols] = pos4_inferenced[cols].replace('low',fuzzyvalues[i][0])
                    pos4_inferenced[cols] = pos4_inferenced[cols].replace('medium',fuzzyvalues[i][1])
                    pos4_inferenced[cols] = pos4_inferenced[cols].replace('high',fuzzyvalues[i][2])
                pos4_fuzzified = defuzzification(pos4_inferenced)
                pos4_final = ((pos4_fuzzified[0] * sum(randomsample[0])) + (pos4_fuzzified[1] * sum(randomsample[1])) + (pos4_fuzzified[2] * sum(randomsample[2])) / ((pos4_fuzzified[0] * len(randomsample[0])) + (pos4_fuzzified[1] * len(randomsample[1])) + (pos4_fuzzified[2] * len(randomsample[2])))) 
                entry.append(round((pos4_final),2))

            if selectedhero.iloc[i,1] == 'pos5':
                pos5_inferenced = pos5_inference.copy()
                for cols in pos5_inferenced.columns[1:-1]:
                    pos5_fuzzy = selectedhero.drop(columns=['hero','pos'])
                    fuzzyvalues = [[float(num) for num in item.strip('[]').split(',')] for item in pos5_fuzzy[cols]]
                    pos5_inferenced[cols] = pos5_inferenced[cols].replace('low',fuzzyvalues[i][0])
                    pos5_inferenced[cols] = pos5_inferenced[cols].replace('medium',fuzzyvalues[i][1])
                    pos5_inferenced[cols] = pos5_inferenced[cols].replace('high',fuzzyvalues[i][2])
                pos5_fuzzified = defuzzification(pos5_inferenced)
                pos5_final = ((pos5_fuzzified[0] * sum(randomsample[0])) + (pos5_fuzzified[1] * sum(randomsample[1])) + (pos5_fuzzified[2] * sum(randomsample[2])) / ((pos5_fuzzified[0] * len(randomsample[0])) + (pos5_fuzzified[1] * len(randomsample[1])) + (pos5_fuzzified[2] * len(randomsample[2])))) 
                entry.append(round((pos5_final),2))
        # append entry to finaltable    
        finaltable.loc[len(finaltable)] = entry

    return finaltable
    
def strip_to_pos(finaltable, pos_selection):
    newpos = []
    for pos in pos_selection:
        newpos.append(pos[0:4])
    
    for i in range(len(finaltable)):
        finaltable.loc[i,'pos1'] = finaltable.loc[i,newpos[i]]
        
    finaltable.drop(columns=['pos2','pos3','pos4','pos5'], inplace=True)
    
    #rename column
    finaltable.rename(columns={'pos1':'score'}, inplace=True)
    
    #add pos_selection to finaltable
    finaltable['pos'] = pos_selection
    
    return finaltable

def convert_to_categorical(dataframe):
  for cols in dataframe.columns:
    if cols == 'score':
      min = dataframe[cols].min()
      q1 = dataframe[cols].quantile(0.25)
      q3 = dataframe[cols].quantile(0.75)
      max = dataframe[cols].max()
      print(min,q1,q3,max)
      dataframe[cols] = pd.cut(dataframe[cols], bins=[min-1, q1, q3, max+1], labels=['jelek', 'sedang', 'bagus'])
  return dataframe

st.write('# Dota 2 Player Performance Prediction')
st.write('Program ini berfungsi untuk memprediksi performa seorang pemain Dota 2 berdasarkan hero yang dipilihnya dan posisi yang dimainkan')
st.write('Sistem prediksi ini menggunakan dataset yang diambil dari pertandingan semi-professional dan professional Dota2 yang terjadi di patch 7.33')
st.write('Menggunakan Fuzzy Logic, dataset diubah menjadi batasan-batasan fuzzy yang kemudian digunakan untuk memprediksi performa pemain')

st.write('\n\n')

st.write('## Batasan Dataset')
st.write('Berikut adalah batasan dataset yang digunakan')
all_matches = pd.read_csv('all_matches.csv')
boxGraph(all_matches)
fuzzy_limits = getAllFuzzyLimits() 
st.write(fuzzy_limits)

st.write('## Masukkan MatchID')
st.write('MatchID digunakan untuk mencari detail match yang dimainkan oleh player')
chosen = st.text_input('MatchID')

if chosen:
    try:
        fuzzified_match = getMatchByID(chosen, fuzzy_limits)
        if(fuzzified_match.empty):
            raise Exception('MatchID tidak ditemukanaaa')
        selectedMatch = matchDetailAggregator([chosen])
        inference_rules = getAllRules()
        pos_inference = get_inference_data(inference_rules)
        display_match_details(selectedMatch, fuzzified_match)
        pos_selection = display_hero_positions(selectedMatch)
        if (pos_selection != False):
            predict = st.button('Prediksi Performa')
            if predict:
                finalfinal = final_calculation(fuzzified_match, pos_inference['pos1_inference'], pos_inference['pos2_inference'], pos_inference['pos3_inference'], pos_inference['pos4_inference'], pos_inference['pos5_inference'])
                finalscore = strip_to_pos(finalfinal, pos_selection)
                finalscore = convert_to_categorical(finalscore)
                st.write(finalscore)        
    except Exception as e: 
        st.write(f"Mohon Parse match terlebih dahulu di https://stratz.com/matches/{chosen}")  