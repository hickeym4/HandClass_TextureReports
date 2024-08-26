import pandas as pd
import numpy as np



def AllData(df):
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Overall"
    return df[[FF, RunoutFull, "Matchups"]]


def AceHighOverRiver(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["AceHighOverRiver"] = (df[Flop1_num]/df[Flop1_num]).where((df[River_num]==14)&(df[Flop1_num]<14)&(df[Flop2_num]<14)&(df[Flop3_num]<14)&(df[Turn_num]<14))
    df = df.dropna(subset=["AceHighOverRiver"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "AceHighOverRiver"
    return df[[FF, RunoutFull, "Matchups"]]

def AceHighOverTurn(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["AceHighOverTurn"] = (df[Flop1_num]/df[Flop1_num]).where((df[Turn_num]==14)&(df[Flop3_num]<14)&(df[Flop2_num]<14)&(df[Flop1_num]<14))
    df = df.dropna(subset=["AceHighOverTurn"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "AceHighOverTurn"
    return df[[FF, RunoutFull, "Matchups"]]

def AceHighFlop(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["AH_F_c1"] = (df[Flop1_num]/df[Flop1_num]).where(df[Flop1_num]==14,0)
    df["AH_F_c2"] = (df[Flop1_num]/df[Flop1_num]).where(df[Flop2_num]==14,0)
    df["AH_F_c3"] = (df[Flop1_num]/df[Flop1_num]).where(df[Flop3_num]==14,0)
    df["AceFlop_Count"] = df["AH_F_c1"]+df["AH_F_c2"]+df["AH_F_c3"]
    df["AceHighFlop"] = (df[Flop1_num]/df[Flop1_num]).where(df["AceFlop_Count"]>=1)
    df = df.dropna(subset=["AceHighFlop"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "AceHighOverTurn"
    return df[[FF, RunoutFull, "Matchups"]]


