import pandas as pd
import numpy as np

def Non_FlushClose_River(df):
    Flop1_num = "Flop1_1_conv"
    c_fsum = "c_fsum"
    s_fsum = "s_fsum"
    h_fsum = "h_fsum"
    d_fsum = "d_fsum"
    c_tsum = "c_tsum"
    s_tsum = "s_tsum"
    h_tsum = "h_tsum"
    d_tsum = "d_tsum"
    F1_suit = "Flop1_2"
    F2_suit = "Flop2_2"
    F3_suit = "Flop3_2"
    T_suit = "Turn_2"
    R_suit = "River_2"
    df["Non_FlushClose_River"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_tsum]==2)&(df[R_suit]!="c")|\
                                                   (df[s_tsum]==2)&(df[R_suit]!="s")|\
                                                   (df[h_tsum]==2)&(df[R_suit]!="h")|\
                                                   (df[d_tsum]==2)&(df[R_suit]!="d"))
    df = df.dropna(subset=["Non_FlushClose_River"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Non_FlushClose_River"
    return df[[FF, RunoutFull, "Matchups"]]

def FlushClose_River(df):
    Flop1_num = "Flop1_1_conv"
    c_fsum = "c_fsum"
    s_fsum = "s_fsum"
    h_fsum = "h_fsum"
    d_fsum = "d_fsum"
    c_tsum = "c_tsum"
    s_tsum = "s_tsum"
    h_tsum = "h_tsum"
    d_tsum = "d_tsum"
    F1_suit = "Flop1_2"
    F2_suit = "Flop2_2"
    F3_suit = "Flop3_2"
    T_suit = "Turn_2"
    R_suit = "River_2"
    df["FlushClose_River"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_tsum]==2)&(df[R_suit]=="c")|(df[s_tsum]==2)&(df[R_suit]=="s")|\
                                                                 (df[h_tsum]==2)&(df[R_suit]=="h")|(df[d_tsum]==2)&(df[R_suit]=="d"))
    df = df.dropna(subset=["FlushClose_River"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "FlushClose_River"
    return df[[FF, RunoutFull, "Matchups"]]

def Rainbow_Turn(df):
    Flop1_num = "Flop1_1_conv"
    c_fsum = "c_fsum"
    s_fsum = "s_fsum"
    h_fsum = "h_fsum"
    d_fsum = "d_fsum"
    c_tsum = "c_tsum"
    s_tsum = "s_tsum"
    h_tsum = "h_tsum"
    d_tsum = "d_tsum"
    F1_suit = "Flop1_2"
    F2_suit = "Flop2_2"
    F3_suit = "Flop3_2"
    T_suit = "Turn_2"
    R_suit = "River_2"
    df["Rainbow_Turn"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_tsum]==1)&(df[s_tsum]==1)&(df[h_tsum]==1)&(df[d_tsum]==1))
    df = df.dropna(subset=["Rainbow_Turn"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Rainbow_Turn"
    return df[[FF, RunoutFull, "Matchups"]]

def FlushClose_Turn(df):
    Flop1_num = "Flop1_1_conv"
    c_fsum = "c_fsum"
    s_fsum = "s_fsum"
    h_fsum = "h_fsum"
    d_fsum = "d_fsum"
    c_tsum = "c_tsum"
    s_tsum = "s_tsum"
    h_tsum = "h_tsum"
    d_tsum = "d_tsum"
    F1_suit = "Flop1_2"
    F2_suit = "Flop2_2"
    F3_suit = "Flop3_2"
    T_suit = "Turn_2"
    R_suit = "River_2"
    df["FlushClose_Turn"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_fsum]==2)&(df[T_suit]=="c")|\
                                                   (df[s_fsum]==2)&(df[T_suit]=="s")|\
                                                   (df[h_fsum]==2)&(df[T_suit]=="h")|\
                                                   (df[d_fsum]==2)&(df[T_suit]=="d"))
    df = df.dropna(subset=["FlushClose_Turn"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "FlushClose_Turn"
    return df[[FF, RunoutFull, "Matchups"]]

def Monotone_Flop(df):
    Flop1_num = "Flop1_1_conv"
    c_fsum = "c_fsum"
    s_fsum = "s_fsum"
    h_fsum = "h_fsum"
    d_fsum = "d_fsum"
    c_tsum = "c_tsum"
    s_tsum = "s_tsum"
    h_tsum = "h_tsum"
    d_tsum = "d_tsum"
    F1_suit = "Flop1_2"
    F2_suit = "Flop2_2"
    F3_suit = "Flop3_2"
    T_suit = "Turn_2"
    R_suit = "River_2"
    df["Monotone_Flop"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_fsum]==3)|(df[s_fsum]==3)|(df[h_fsum]==3)|(df[d_fsum]==3))
    df = df.dropna(subset=["Monotone_Flop"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "Monotone_Flop"
    return df[[FF, RunoutFull, "Matchups"]]

    