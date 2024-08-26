import pandas as pd
import numpy as np


def FlushRiver_4Card(df):
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
    df["FlushRiver_4Card"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_tsum]==3)&(df[R_suit]=="c")|\
                                                   (df[s_tsum]==3)&(df[R_suit]=="s")|\
                                                   (df[h_tsum]==3)&(df[R_suit]=="h")|\
                                                   (df[d_tsum]==3)&(df[R_suit]=="d"))
    df = df.dropna(subset=["FlushRiver_4Card"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "FlushRiver_4Card"
    return df[[FF, RunoutFull, "Matchups"]]

def FlushTurn_4Card(df):
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
    df["FlushTurn_4Card"] = (df[Flop1_num]/df[Flop1_num]).where((df[c_tsum]==4)&(df[R_suit]!="c")|\
                                                   (df[s_tsum]==4)&(df[R_suit]!="s")|\
                                                   (df[h_tsum]==4)&(df[R_suit]!="h")|\
                                                   (df[d_tsum]==4)&(df[R_suit]!="d"))
    df = df.dropna(subset=["FlushTurn_4Card"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "FlushTurn_4Card"
    return df[[FF, RunoutFull, "Matchups"]]

def function_4cs(df):
    Flop1_num = "Flop1_1_conv"
    Flop2_num = "Flop2_1_conv"
    Flop3_num = "Flop3_1_conv"
    Turn_num =  "Turn_1_conv"
    River_num = "River_1_conv"
    # df = df[[Flop1_num, Flop2_num, Flop3_num, Turn_num,River_num]]
    # df = pd.DataFrame()
    [l_1, l_2, l_3, l_4, riv_1, riv_2, riv_3, riv_4, riv_5, hi_outlier, lo_outlier, mid_copy_complete, connect_1, connect_2, connect_3, connect_sum_turn, needriv_for_st,riv_connect_sum, riv_connect_1, riv_connect_2, riv_connect_3, riv_connect_4, hi_outlier_complete, lo_outlier_complete] = \
        ["1st_large", "2nd_large", "3rd_large", "4th_large", "riv_1", "riv_2", "riv_3", "riv_4", "riv_5", "hi_outlier", "lo_outlier", "mid_copy_complete", "connect1", "connect2", "connect3", "connect_sum_turn","needriv_for_st","riv_connect_sum", "riv_connect_1", "riv_connect_2", "riv_connect_3", "riv_connect_4","hi_outlier_complete", "lo_outlier_complete" ]
    df[l_1] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num]],axis=1)[:,-1]
    df[l_2] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num]],axis=1)[:,-2]
    df[l_3] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num]],axis=1)[:,-3]
    df[l_4] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num]],axis=1)[:,-4]
    df[riv_1] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num, River_num]],axis=1)[:,-1]
    df[riv_2] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num, River_num]],axis=1)[:,-2]
    df[riv_3] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num, River_num]],axis=1)[:,-3]
    df[riv_4] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num, River_num]],axis=1)[:,-4]
    df[riv_5] = np.sort(df[[Flop1_num, Flop2_num, Flop3_num, Turn_num, River_num]],axis=1)[:,-5]
    df[connect_1] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]-df[l_2]==1),0)
    df[connect_2] = (df[Flop1_num]/df[Flop1_num]).where((df[l_2]-df[l_3]==1),0)
    df[connect_3] = (df[Flop1_num]/df[Flop1_num]).where((df[l_3]-df[l_4]==1),0)
    df[connect_sum_turn] = df[connect_1] + df[connect_2] + df[connect_3]
    df["open_end_turn"] = (df[Flop1_num]/df[Flop1_num]).where((df[connect_sum_turn]==3))
    df["gutshort_turn"] = (df[Flop1_num]/df[Flop1_num]).where((df[connect_sum_turn]==2)&((df[l_2]-df[l_3]==2)|(df[l_1]-df[l_2]==2)|(df[l_3]-df[l_4]==2)))
    
    #brute force method for straight turn when low card when ace 
    df["ace_1_t"] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]==14)&(df[l_2]==5)&(df[l_3]==4)&(df[l_4]==3))
    df["ace_2_t"] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]==14)&(df[l_2]==5)&(df[l_3]==4)&(df[l_4]==2))
    df["ace_3_t"] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]==14)&(df[l_2]==5)&(df[l_3]==3)&(df[l_4]==2))
    df["ace_4_t"] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]==14)&(df[l_2]==4)&(df[l_3]==3)&(df[l_4]==2))
    df["ace_5_t"] = (df[Flop1_num]/df[Flop1_num]).where((df[l_1]==5)&(df[l_2]==4)&(df[l_3]==3)&(df[l_4]==2))
    df["ace_ST4c"] = (df[Flop1_num]/df[Flop1_num]).where((df["ace_5_t"]==1)|(df["ace_4_t"]==1)|(df["ace_3_t"]==1)|(df["ace_2_t"]==1)|(df["ace_1_t"]==1))
    df["ace_makes_st_riv"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]==14)&(df[riv_2]==5)&(df[riv_3]==4)&(df[riv_4]==3)&(df[riv_5]==2))
    df["ace_1_r"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]==14)&(df[riv_2]==5)&(df[riv_3]==4)&(df[riv_4]==3))
    df["ace_2_r"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]==14)&(df[riv_2]==5)&(df[riv_3]==4)&(df[riv_5]==2))
    df["ace_3_r"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]==14)&(df[riv_2]==5)&(df[riv_4]==3)&(df[riv_5]==2))
    df["ace_4_r"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]==14)&(df[riv_3]==4)&(df[riv_4]==3)&(df[riv_5]==2))
    df["ace_5_r"] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_2]==5)&(df[riv_3]==4)&(df[riv_4]==3)&(df[riv_5]==2))
    df["ace_SR4c"] = (df[Flop1_num]/df[Flop1_num]).where((df["ace_1_r"]==1)|(df["ace_2_r"]==1)|(df["ace_3_r"]==1)|(df["ace_4_r"]==1)|(df["ace_5_r"]==1))

    df[riv_connect_1] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_1]-df[riv_2]==1),0)
    df[riv_connect_2] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_2]-df[riv_3]==1),0)
    df[riv_connect_3] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_3]-df[riv_4]==1),0)
    df[riv_connect_4] = (df[Flop1_num]/df[Flop1_num]).where((df[riv_4]-df[riv_5]==1),0)
    df["riv_count"] = df[riv_connect_1] + df[riv_connect_2] + df[riv_connect_3] + df[riv_connect_4]
    df["River_makes_straight"] = (df[Flop1_num]/df[Flop1_num]).where(df["riv_count"]==4)
    df["Riv_open_ender"] = (df[Flop1_num]/df[Flop1_num]).where((df["riv_count"]==3)&((df[l_2]-df[l_3]==2)|(df[l_1]-df[l_2]==2)|(df[l_3]-df[l_4]==2)))
    df["Riv_gutshot"] = (df[Flop1_num]/df[Flop1_num]).where((df["riv_count"]==2)&((df[riv_1]-df[riv_2]==2)|(df[riv_2]-df[riv_3]==2)|(df[riv_3]-df[riv_4]==2)|(df[riv_4]-df[riv_5]==2)))

    df["StraightTurn_4Card"] = (df[Flop1_num]/df[Flop1_num]).where(((df["open_end_turn"]==1)|(df["gutshort_turn"]==1)|(df["ace_ST4c"]==1))&((df["River_makes_straight"]!=1)&(df["ace_makes_st_riv"]!=1)))
    df["StraightRiver_4Card"] = (df[Flop1_num]/df[Flop1_num]).where(((df["Riv_gutshot"]==1)|(df["Riv_open_ender"]==1)|(df["ace_SR4c"]==1))&((df["River_makes_straight"]!=1)&(df["ace_makes_st_riv"]!=1)))
    return df

def StraightRiver_4Card(df):
    df = function_4cs(df)
    df = df.dropna(subset=["StraightRiver_4Card"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "StraightRiver_4Card"
    return df[[FF, RunoutFull, "Matchups"]]

def StraightTurn_4Card(df):
    df = function_4cs(df)
    df = df.dropna(subset=["StraightTurn_4Card"])
    FF = "FF"
    RunoutFull = "Runout_Full"
    df.name = "StraightTurn_4Card"
    return df[[FF, RunoutFull, "Matchups"]]

