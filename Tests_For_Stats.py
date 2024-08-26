import pandas as pd
import numpy as np
import Mike_Stats_Functions as MSF 
import math
data = pd.read_csv("Stats_Test_File.csv")

def Test_Stats():
    WeightedAverage = round(data["Weighted Average"].iloc[0],2)
    WeightedStdDev = round(data["Weight Std Dev"].iloc[0],2)
    ConfidenceInterval = round(data["Confidence Interval"].iloc[0],2)
    StdDev = round(data["StdDev"].iloc[0],2)
    Variance = round(WeightedStdDev*WeightedStdDev,2)
    weightavgpy = MSF.WeightedAverage(data,"Num","Weights")
    varpy = MSF.Variance(data,weightavgpy,"Num","Weights")
    confpy = MSF.ConfidenceInterval(1.96,math.sqrt(varpy),len(data["Num"]))

    avg = (WeightedAverage-weightavgpy)/weightavgpy*100
    var = (Variance-varpy)/varpy*100
    conf = (ConfidenceInterval-confpy)/confpy*100
    if (avg<.05)&(var<.05)&(conf<.05):
        return True
    
