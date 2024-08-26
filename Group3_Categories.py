import pandas as pd
import numpy as np

def Low_Through_River(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    df["Low_Through_River"] = (df[Flop1_num]/df[Flop1_num]).where((df[Flop1_num]<=10)&(df[Flop2_num]<=10)&(df[Flop3_num]<=10)&(df[Turn_num]<=10)&(df[River_num]<=10))
    df = df.dropna(subset=["Low_Through_River"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Low_Through_River"
    return df[[FF, RunoutFull, "Matchups"]]


