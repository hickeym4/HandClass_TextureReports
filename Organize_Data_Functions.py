import pandas as pd
import numpy as np

def ConvertCamFile_V1(df):
    df = df.rename(columns={"FOLD freq":"FF"})
    df = df.dropna(subset=["Flop"])
    df = df.dropna(subset=["Turn"])
    df = df.dropna(subset=["River"])
    df[['Flop1', 'Flop2','Flop3']] = df['Flop'].str.split(' ', expand=True).where(df["Flop"].notna())
    df["Flop1_1"] = df["Flop1"].str[:1]
    df["Flop1_2"] = df["Flop1"].str[1:2]
    df["Flop2_1"] = df["Flop2"].str[:1]
    df["Flop2_2"] = df["Flop2"].str[1:2]
    df["Flop3_1"] = df["Flop3"].str[:1]
    df["Flop3_2"] = df["Flop3"].str[1:2]
    df["Turn_1"] = df["Turn"].str[:1]
    df["Turn_2"] = df["Turn"].str[1:2]
    df["River_1"] = df["River"].str[:1]
    df["River_2"] = df["River"].str[1:2]
    for i in range(1,4):
        for j in range(1,3):
            str_orig = "Flop"+str(i)+"_"+str(j)
            str_conv = str_orig + "_conv"
            df[str_conv] = (df["FF"]/df["FF"]*10).where(df[str_orig]=="T",(df["FF"]/df["FF"]*11).where(df[str_orig]=="J",\
                                            (df["FF"]/df["FF"]*12).where(df[str_orig]=="Q",(df["FF"]/df["FF"]*13).where(df[str_orig]=="K",\
                                            (df["FF"]/df["FF"]*14).where(df[str_orig]=="A",df[str_orig])))))
    for z in range(1,3):
            str_orig = "Turn_"+str(z)
            str_conv = str_orig + "_conv"
            df[str_conv] = (df["FF"]/df["FF"]*10).where(df[str_orig]=="T",(df["FF"]/df["FF"]*11).where(df[str_orig]=="J",\
                                            (df["FF"]/df["FF"]*12).where(df[str_orig]=="Q",(df["FF"]/df["FF"]*13).where(df[str_orig]=="K",\
                                            (df["FF"]/df["FF"]*14).where(df[str_orig]=="A",df[str_orig])))))
    for f in range(1,3):
            str_orig = "River_"+str(f)
            str_conv = str_orig + "_conv"
            df[str_conv] = (df["FF"]/df["FF"]*10).where(df[str_orig]=="T",(df["FF"]/df["FF"]*11).where(df[str_orig]=="J",\
                                            (df["FF"]/df["FF"]*12).where(df[str_orig]=="Q",(df["FF"]/df["FF"]*13).where(df[str_orig]=="K",\
                                            (df["FF"]/df["FF"]*14).where(df[str_orig]=="A",df[str_orig])))))
    df["Flop1_1_conv"]=df["Flop1_1_conv"].astype(int)
    df["Flop2_1_conv"]=df["Flop2_1_conv"].astype(int)
    df["Flop3_1_conv"]=df["Flop3_1_conv"].astype(int)
    df["Turn_1_conv"]=df["Turn_1_conv"].astype(int)
    df["River_1_conv"]=df["River_1_conv"].astype(int)

    suits = ["c","s","h","d"]

    for s in suits:
        f1 = str(s)+"_f1"
        f2 = str(s)+"_f2"
        f3 = str(s)+"_f3"
        fsum = str(s)+"_fsum"
        turn = str(s)+"_turn"
        tsum = str(s)+"_tsum"
        river = str(s)+"_river"
        
        df[f1]=(df["FF"]/df["FF"]).where(df["Flop1_2"]==s,0)
        df[f2]=(df["FF"]/df["FF"]).where(df["Flop2_2"]==s,0)
        df[f3]=(df["FF"]/df["FF"]).where(df["Flop3_2"]==s,0)
        df[fsum] = df[f1]+df[f2]+df[f3]
        df[turn]=(df["FF"]/df["FF"]).where(df["Turn_2"]==s,0)
        df[tsum] = df[fsum]+df[turn]
        df[river]=(df["FF"]/df["FF"]).where(df["River_2"]==s,0)
    df["Runout_Full"] = df["Flop"].astype(str) +" "+ df["Turn"].astype(str)+" " + df["River"].astype(str) 
    return df
def can_be_converted_to_number(s):
    try:
        float(s)  # Try to convert the string to a float
        return True
    except ValueError:
        return False

def check_report_naming_format_betsize(csvpath):
    name = str(csvpath)
    # str1 = str(name).rsplit('-', 1)
    # str1_num = str1[-1]
    # if 'r' in str1_num:
    #     str1_num= str1_num.rsplit('r',1) 
    #     str1_num = str1_num[0]
    # if can_be_converted_to_number(str1_num):
    #     return True
    # else:
    #     return False
    if name[-1]=="F":
        return False
    else:
        return True
def check_report_columns(df):
    if "FOLD freq" in df.columns:
        return True
    else:
        return False

# teststr = r"C:\Users\cam\Downloads\Robby-HandClasses-main\Robby-HandClasses-main\Reports_Round_1\BB_vs_BU_3BP\IP\B-BC-F\3BP_BU_vs_BB_B-BC-F"

# print(check_report_naming_format_betsize(teststr))