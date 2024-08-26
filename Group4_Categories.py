import pandas as pd
import numpy as np

def Pairing_River(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Pair_B4_Riv"] = (df[Flop1_num]/df[Flop1_num]).where((df[Flop1_num]==df[Flop2_num])|(df[Flop1_num]==df[Flop3_num])|(df[Flop2_num]==df[Flop3_num])|(df[Flop1_num]==df[Turn_num])|(df[Flop2_num]==df[Turn_num])|(df[Flop3_num]==df[Turn_num]))
    df["Pairing_River"] = (df[Flop1_num]/df[Flop1_num]).where((((df[Turn_num]==df[River_num])&(df[Flop1_num]!=df[River_num])&(df[Flop2_num]!=df[River_num])&(df[Flop3_num]!=df[River_num]))|\
                                          ((df[Flop1_num]==df[River_num])&(df[Turn_num]!=df[River_num])&(df[Flop2_num]!=df[River_num])&(df[Flop3_num]!=df[River_num]))|\
                                         ((df[Flop2_num]==df[River_num])&(df[Turn_num]!=df[River_num])&(df[Flop1_num]!=df[River_num])&(df[Flop3_num]!=df[River_num]))|\
                                          ((df[Flop3_num]==df[River_num])&(df[Turn_num]!=df[River_num])&(df[Flop1_num]!=df[River_num])&(df[Flop2_num]!=df[River_num])))&(df["Pair_B4_Riv"]!=1))
    # df["Pairing_River"] = (df[Flop1_num]/df[Flop1_num]).where((df[Turn_num]==df[River_num])|(df[Flop1_num]==df[River_num])|(df[Flop2_num]==df[River_num])|(df[Flop3_num]==df[River_num]))
    df = df.dropna(subset=["Pairing_River"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Pairing_River"
    return df[[FF, RunoutFull, "Matchups"]]

def Pairing_Turn(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    # df["Pairing_Turn"] = (df[Flop1_num]/df[Flop1_num]).where(((df[Flop1_num]==df[Turn_num])&(df[Flop2_num]!=df[Turn_num])&(df[Flop3_num]!=df[Turn_num]))|\
    #                                      ((df[Flop2_num]==df[Turn_num])&(df[Flop1_num]!=df[Turn_num])&(df[Flop3_num]!=df[Turn_num]))|\
    #                                      ((df[Flop3_num]==df[Turn_num])&(df[Flop1_num]!=df[Turn_num])&(df[Flop2_num]!=df[Turn_num])))
    df["Pair_B4_Turn"] = (df[Flop1_num]/df[Flop1_num]).where((df[Flop1_num]==df[Flop2_num])|(df[Flop1_num]==df[Flop3_num])|(df[Flop2_num]==df[Flop3_num]))
    df["Pairing_Turn"] = (df[Flop1_num]/df[Flop1_num]).where((((df[Flop1_num]==df[Turn_num])&(df[Flop2_num]!=df[Turn_num])&(df[Flop3_num]!=df[Turn_num]))|\
                                                             ((df[Flop2_num]==df[Turn_num])&(df[Flop1_num]!=df[Turn_num])&(df[Flop3_num]!=df[Turn_num]))|\
                                                                ((df[Flop3_num]==df[Turn_num])&(df[Flop2_num]!=df[Turn_num])&(df[Flop1_num]!=df[Turn_num])))&\
                                                                    (df["Pair_B4_Turn"]!=1))
    df = df.dropna(subset=["Pairing_Turn"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Pairing_Turn"
    return df[[FF, RunoutFull, "Matchups"]]

def Paired_Flop(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Paired_Flop"] = (df[Flop1_num]/df[Flop1_num]).where(((df[Flop1_num]==df[Flop2_num])&(df[Flop2_num]!=df[Flop3_num]))|\
                                                            ((df[Flop1_num]==df[Flop3_num])&(df[Flop3_num]!=df[Flop2_num]))|\
                                                                ((df[Flop2_num]==df[Flop3_num])&(df[Flop1_num]!=df[Flop2_num])))
    df = df.dropna(subset=["Paired_Flop"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Paired_Flop"
    return df[[FF, RunoutFull, "Matchups"]]

def Set_Flop(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Set_Flop"] = (df[Flop1_num]/df[Flop1_num]).where((df[Flop1_num]==df[Flop2_num])&(df[Flop2_num]==df[Flop3_num]))
    df = df.dropna(subset=["Set_Flop"])
    df.name="Set_Flop"
    return df[["FF","Runout_Full","Matchups"]]