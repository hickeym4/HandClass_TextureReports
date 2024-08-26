import pandas as pd
import numpy as np

def BluffingPotCapture(df, FoldFrequency, BetSize):
    PC = "Pot_Capture"
    # temp = df.copy()
    df[FoldFrequency]=round(df[FoldFrequency], 4)
    df[PC] = df[FoldFrequency]/100-(1-df[FoldFrequency]/100)*(BetSize)
    return df

