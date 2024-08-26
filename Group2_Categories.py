import pandas as pd
import numpy as np

def BroadwayRiverOvercard(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["BroadwayRiverOvercard"] = (df[Flop1_num]/df[Flop1_num]).where((df[River_num]>=11)&(df[Turn_num]<df[River_num])&(df[Flop3_num]<df[River_num])&(df[Flop2_num]<df[River_num])\
                                          &(df[Flop1_num]<df[River_num])&(df[River_num]!=14))
    df = df.dropna(subset=["BroadwayRiverOvercard"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "BroadwayRiverOvercard"
    return df[[FF, RunoutFull, "Matchups"]]
def BroadwayTurnOvercard(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["BroadwayTurnOvercard"] = (df[Flop1_num]/df[Flop1_num]).where((df[Turn_num]>=11)&(df[Flop3_num]<df[Turn_num])&(df[Flop2_num]<df[Turn_num])\
                                          &(df[Flop1_num]<df[Turn_num])&(df[Turn_num]!=14))
    df = df.dropna(subset=["BroadwayTurnOvercard"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "BroadwayTurnOvercard"
    return df[[FF, RunoutFull, "Matchups"]]

def Flop2BLowTurnRiver(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Flop2BLowTurnRiver"] = (df[Flop1_num]/df[Flop1_num]).where(((df[Flop1_num]>=10)&(df[Flop1_num]!=14)&(df[Flop2_num]>=10)&(df[Flop2_num]!=14)&(df[Flop3_num]<10)&(df[Flop3_num]!=14)&(df[Flop1_num]!=df[Flop2_num])&(df[Turn_num]<10)&(df[River_num]<10))|\
                                                                   ((df[Flop2_num]>=10)&(df[Flop2_num]!=14)&(df[Flop3_num]>=10)&(df[Flop3_num]!=14)&(df[Flop1_num]<10)&(df[Flop1_num]!=10)&(df[Flop2_num]!=df[Flop3_num])&(df[Turn_num]<10)&(df[River_num]<10))|\
                                                                    ((df[Flop1_num]>=10)&(df[Flop1_num]!=14)&(df[Flop3_num]>=10)&(df[Flop3_num]!=14)&(df[Flop2_num]<10)&(df[Flop2_num]!=10)&(df[Flop1_num]!=df[Flop3_num])&(df[Turn_num]<10)&(df[River_num]<10)))
    df = df.dropna(subset=["Flop2BLowTurnRiver"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Flop2BLowTurnRiver"
    return df[[FF, RunoutFull, "Matchups"]]

def Flop3BLowTurnRiver(df,):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Flop2BLowTurnRiver"] = (df[Flop1_num]/df[Flop1_num]).where((df[Flop1_num]>=10)&(df[Flop2_num]>=10)&(df[Flop3_num]>=10)&\
                                                                   (df[Flop1_num]!=df[Flop2_num])&(df[Flop2_num]!=df[Flop3_num])&(df[Flop3_num]!=df[Flop1_num])&\
                                                                   (df[Turn_num]<10)&(df[River_num]<10))
    df = df.dropna(subset=["Flop2BLowTurnRiver"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Flop3BLowTurnRiver"
    return df[[FF, RunoutFull, "Matchups"]]

