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
data = pd.read_csv("report-Mike.csv")
data = ODF.ConvertCamFile_V1(data)
Group1_1 = G1C.AceHighOverRiver(data)
Group1_1.name = "AceHighOverRiver"
Group1_2 = G1C.AceHighOverTurn(data)
Group1_2.name = "AceHighOverTurn"
Group1_3 = G1C.AceHighFlop(data)
Group1_3.name = "AceHighFlop"
Group2_1 = G2C.BroadwayRiverOvercard(data)
Group2_1.name = "BroadwayRiverOvercard"
Group2_2 = G2C.BroadwayTurnOvercard(data)
Group2_2.name = "BroadwayTurnOvercard"
Group2_3 = G2C.Flop2BLowTurnRiver(data)
Group2_3.name = "Flop2BLowTurnRiver"
Group2_4 = G2C.Flop3BLowTurnRiver(data)
Group2_4.name = "Flop3BLowTurnRiver"
Group3 = G3C.Low_Through_River(data)
Group3.name = "Low_Through_River"
Group4_1 = G4C.Paired_Flop(data)
Group4_1.name = "Paired_Flop"
Group4_2 = G4C.Pairing_River(data)
Group4_2.name = "Pairing_River"
Group4_3 = G4C.Pairing_Turn(data)
Group4_3.name = "Pairing_Turn"
Group5_1 = G5C.FlushClose_River(data)
Group5_1.name = "FlushClose_River"
Group5_2 = G5C.FlushClose_Turn(data)
Group5_2.name = "FlushClose_Turn"
Group5_3 = G5C.Monotone_Flop(data)
Group5_3.name = "Monotone_Flop"
Group5_4 = G5C.Non_FlushClose_River(data)
Group5_4.name = "Non_FlushClose_River"
Group5_5 = G5C.Rainbow_Turn(data)
Group5_5.name = "Rainbow_Turn"
Group6_1 = G6C.FlushRiver_4Card(data)
Group6_1.name = "FlushRiver_4Card"
Group6_2 = G6C.FlushTurn_4Card(data)
Group6_2.name = "FlushTurn_4Card"
Group6_3 = G6C.FlushTurn_4Card(data)
Group6_3.name = "FlushTurn_4Card"
Group6_4 = G6C.FlushRiver_4Card(data)
Group6_4.name = "FlushRiver_4Card"

def overlap_arr_gen(category_1, category_2, colname, return_df):
    arr_1 = category_1[colname].to_numpy()
    arr_2 = category_2[colname].to_numpy()

    same_hands = np.intersect1d(arr_1, arr_2)
    overlap_df = category_1[category_1[colname].isin(same_hands)]

    small_overlap = same_hands.size/arr_2.size*100
    large_overlap = same_hands.size/arr_1.size*100

    overlap_results_new = pd.DataFrame(columns = ["Category 1", "Category 2", "% Duplicates (Category 1)", "% Duplicates (Category 2)"], data = [[category_1.name, category_2.name, large_overlap, small_overlap]])
    if return_df == True:
        return overlap_df
    else:
        return [small_overlap, large_overlap]


All_Categories = [Group1_1, Group1_2, Group1_3, Group2_1, Group2_2, Group2_3, Group2_4, Group3, Group4_1, Group4_2, Group4_3, Group5_1, Group5_2, Group5_3, Group5_4, Group5_5, Group6_1, Group6_2, Group6_3, Group6_4]
def data_gen_v2(category_list):
    overlap_results = pd.DataFrame(columns = ["Category(1)", "Average Pot Capture(1)", "Pot Capture Certainty (95% Confidence)(1)", "Meets Criteria? (<5%) (1)",\
                                               "Category(2)", "Average Pot Capture(2)", "Pot Capture Certainty (95% Confidence)(2)", "Meets Criteria? (<5%) (2)",\
                                                  "Category(Overlap)", "Average Pot Capture(Overlap)", "Pot Capture Certainty (95% Confidence)(Overlap)", "Meets Criteria? (<5%) (Overlap)",\
                                                "Category 1 Overlap", "Category 2 Overlap"])
    for i in range(0,len(category_list)-1):
        i_=category_list[i]
        i_res = MSF.stats_gen_complete(0.5, 1.96, [i_],1)
        for j in range(0,len(category_list)-1):
            j_ = category_list[j]
            j_res = MSF.stats_gen_complete(0.5, 1.96, [j_],2)
            if (i!=j)&(i<j) :
                samehands_df = overlap_arr_gen(i_, j_, "Runout_Full", True)
                samehands_df.name = "Overlap"
                if len(samehands_df)>0:
                    overlap_res = MSF.stats_gen_complete(0.5,1.96,[samehands_df],"Overlap")
                if len(samehands_df)==0:
                    overlap_res = MSF.emptystatsdf("Overlap")
                pcts = overlap_arr_gen(i_, j_, "Runout_Full", False)
                new_res = pd.concat([i_res, j_res, overlap_res], axis=1, join='outer')
                new_res["Category 1 Overlap"] = pcts[0]
                new_res["Category 2 Overlap"] = pcts[1]
                overlap_results = pd.concat([overlap_results, new_res])
    overlap_results = overlap_results.drop_duplicates()
    overlap_results = overlap_results[overlap_results['Category(1)'] != overlap_results['Category(2)']]
    return overlap_results            

# overlap_results = data_gen_v2(All_Categories)

# overlap_results.to_csv("overlapping_categories_estimate.csv")
# print(overlap_results)
# print(len(overlap_results))