import numpy as np
import pandas as pd
import math
import Group1_Categories as G1C
import Group2_Categories as G2C
import Group3_Categories as G3C
import Group4_Categories as G4C
import Group5_Categories as G5C
import Group6_Categories as G6C
import Organize_Data_Functions as ODF
import PotCapture_Functions as PCF
import Mike_Stats_Functions as MSF
from scipy.stats import shapiro 
from scipy.stats import lognorm
from scipy import stats
import numbers

def WeightedAverage(df, DataSet, DataWeights):
    temp = df.copy()
    temp[DataSet] = (temp[DataSet]*100)
    temp[DataWeights] = (temp[DataWeights]*100)
    temp[DataSet] = temp[DataSet].astype('int64')
    temp[DataWeights] = temp[DataWeights].astype('int64')
    temp["Weighted"] = temp[DataSet]*temp[DataWeights]
    #df["Weighted"] = round(df["Weighted"], 2)
    Average = temp["Weighted"].sum()/temp[DataWeights].sum()
    Average = Average/100
    return Average

def Variance(df, avg, DataSet, DataWeights):
    temp = df.copy()
    temp[DataWeights] = (temp[DataWeights]*100)
    temp[DataWeights] = temp[DataWeights].astype('int64')
    temp[DataSet] = round(temp[DataSet], 2)
    temp["onesum"] = ((temp[DataSet]-avg)**2)*temp[DataWeights]
    temp["onesum"] = round(temp["onesum"], 4)
    variance = temp["onesum"].sum()/(temp[DataWeights].sum()-1)
    return variance

def ConfidenceInterval(z, stddev, samplesize):
    ConfInt = z*stddev/(math.sqrt(samplesize))
    return ConfInt
def statistic(x):
    return stats.shapiro(x).statistic

def stats_gen_complete(betsize, z_factor, All_Categories,df_ID):
    rng = np.random.default_rng()
    matchups_str = "% Total Matchups"
    cat_str = "Category("  + str(df_ID) + ")"
    AVPC_str = "Average Pot Capture("  + str(df_ID) + ")"
    PCC_str = "Pot Capture Uncertainty (2 Std Dev) ("  + str(df_ID) + ")"
    pval_str = "Pot Capture p-Value (" + str(df_ID) + ")"
    pval_str_2 = "Pot Capture p-Value shortened(" + str(df_ID) + ")"
    MC_str = "2 Standard Deviations Meets Criteria? (<10% Pot Capture) (" + str(df_ID) + ")"
    results = pd.DataFrame(columns = [cat_str, AVPC_str, PCC_str,pval_str,matchups_str])
    for i in All_Categories:
        if i.name == "Overall":
            matchups_total = i["Matchups"].sum()
    for i in All_Categories:
        FF_avg = MSF.WeightedAverage(i,"FF","Matchups")
        FF_var = MSF.Variance(i,FF_avg,"FF","Matchups")
        PC_df = PCF.BluffingPotCapture(i,"FF",betsize)
        PC_avg = MSF.WeightedAverage(PC_df,"Pot_Capture","Matchups")
        PC_var = MSF.Variance(PC_df, PC_avg, "Pot_Capture", "Matchups")
        PC_sdev = math.sqrt(PC_var)
        PC_conf_int = MSF.ConfidenceInterval(z_factor, PC_sdev, len(i))
        PC_conf_int_pct = PC_conf_int/PC_avg
        matchups_pct = str(round(i["Matchups"].sum()/matchups_total*100,2))+" %"
        p_value = "NA"
        # matchups_list = i["Matchups"].to_list()
        # PC_list = i["Pot_Capture"].to_list()
        # data_list = []
        # for f in range(0,len(PC_list)-1):
        #     for j in range(0,int(matchups_list[f])):
        #         data_list.append(PC_list[f])
        # np.random.seed(0)
        # data2 = np.random.normal(loc=0.1, scale=1, size=len(data_list))

        # Perform a two-sided t-test
        # t_statistic, p_value = stats.ttest_ind(data_list, data2)
        # res = stats.monte_carlo_test(data_list, rng.normal, statistic, 
        #                      alternative='less', batch=None)

        # data_list_2 = [x for x in PC_list for _ in matchups_list]
        # res_2 = stats.monte_carlo_test(data_list_2, rng.normal, statistic, 
        #                      alternative='less', batch=10)


        newrow = pd.DataFrame(columns = [cat_str, AVPC_str, PCC_str,pval_str,matchups_str], 
                            data = [[i.name, PC_avg, PC_sdev*2,p_value,matchups_pct]])
        
        results = pd.concat([results, newrow])
        temp = results.copy()
        temp["Yes"] = "YES"
        temp["NO"] = "NO"
        results[MC_str] = (temp["Yes"]).where(results[PCC_str]<0.1, temp["NO"])
    return results
    
def emptystatsdf(df_ID):
    cat_str = "Category("  + str(df_ID) + ")"
    AVPC_str = "Average Pot Capture("  + str(df_ID) + ")"
    PCC_str = "Pot Capture Certainty (95% Confidence)("  + str(df_ID) + ")"
    MC_str = "Meets Criteria? (<5%) (" + str(df_ID) + ")"
    newrow = pd.DataFrame(columns = [cat_str, AVPC_str, PCC_str, MC_str], data = [[np.nan,np.nan,np.nan,np.nan]])
    return newrow



