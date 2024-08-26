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
# import Category_Tests as CT
# import Tests_For_Stats as StatTest
pd.set_option("display.max_columns", None)
# This is the old (original) file- since it contains a different header, no modification is needed on import
# data = pd.read_csv("report-Mike.csv")

#Most recent report- the one cam wants. Since the header is different and some of the values had issues, modification is needed to handle the file.
#If this report style stays consistent, I'll just put this into a function instead of leaving it here.
# data = pd.read_csv("report_9_Jun.csv",skiprows=3,header=None)

def ReportGenerator2000(betsize,data):
    # new_header = data.iloc[0]
    # data = data[1:]
    # data.columns = new_header
    data["FOLD freq"] = data["FOLD freq"].astype(float)
    data = data[data["FOLD freq"].notna()]
    data = data[(data["FOLD freq"]>0)&(data["FOLD freq"]<=100)]
    data["Matchups"] = data["Matchups"].astype(float)
    data = data[data["Matchups"].notna()]

    # tests = pd.read_csv("Category_Tests_Updated_24April2024.csv")
    data = ODF.ConvertCamFile_V1(data)
    all_runouts = data["Runout_Full"].to_list()

    #Categorize each output, and test outputs
    #Group 1 
    Group1_0 = G1C.AllData(data)
    Group1_0.name = "Overall"
    # Group1_0.to_csv("Overall_Matchups_test.csv")
    Group1_1 = G1C.AceHighOverRiver(data)
    Group1_1.name = "AceHighOverRiver"
    # group1_1_test = pd.DataFrame()
    # group1_1_tests = CT.test_category(tests,Group1_1,"Group1_1",all_runouts,group1_1_test)

    Group1_2 = G1C.AceHighOverTurn(data)
    Group1_2.name = "AceHighOverTurn"
    # group1_2_test = pd.DataFrame()
    # group1_2_tests = CT.test_category(tests,Group1_2,"Group1_2",all_runouts,group1_2_test)

    Group1_3 = G1C.AceHighFlop(data)
    Group1_3.name = "AceHighFlop"
    # group1_3_test = pd.DataFrame()
    # group1_3_tests = CT.test_category(tests,Group1_3,"Group1_3",all_runouts,group1_3_test)

    #Group 2 
    Group2_1 = G2C.BroadwayRiverOvercard(data)
    Group2_1.name = "BroadwayRiverOvercard"
    # group2_1_test = pd.DataFrame()
    # group2_1_tests = CT.test_category(tests,Group2_1,"Group2_1",all_runouts,group2_1_test)

    Group2_2 = G2C.BroadwayTurnOvercard(data)
    Group2_2.name = "BroadwayTurnOvercard"
    # group2_2_test = pd.DataFrame()
    # group2_2_tests = CT.test_category(tests,Group2_2,"Group2_2",all_runouts,group2_2_test)

    Group2_3 = G2C.Flop2BLowTurnRiver(data)
    Group2_3.name = "Flop2BLowTurnRiver"
    # group2_3_test = pd.DataFrame()
    # group2_3_tests = CT.test_category(tests,Group2_3,"Group2_3",all_runouts,group2_3_test)

    Group2_4 = G2C.Flop3BLowTurnRiver(data)
    Group2_4.name = "Flop3BLowTurnRiver"
    # group2_4_test = pd.DataFrame()
    # group2_4_tests = CT.test_category(tests,Group2_4,"Group2_4",all_runouts,group2_4_test)

    #Group 3
    Group3 = G3C.Low_Through_River(data)
    Group3.name = "Low_Through_River"
    # group3_1_test = pd.DataFrame()
    # group3_1_tests = CT.test_category(tests,Group3,"Group3_1",all_runouts,group3_1_test)

    #Group 4
    Group4_1 = G4C.Pairing_River(data)
    Group4_1.name = "Pairing_River"
    # group4_1_test = pd.DataFrame()
    # group4_1_tests = CT.test_category(tests,Group4_1,"Group4_1",all_runouts,group4_1_test)

    Group4_2 = G4C.Pairing_Turn(data)
    Group4_2.name = "Pairing_Turn"
    # group4_2_test = pd.DataFrame()
    # group4_2_tests = CT.test_category(tests,Group4_2,"Group4_2",all_runouts,group4_2_test)

    Group4_3 = G4C.Paired_Flop(data)
    Group4_3.name = "Paired_Flop"
    # group4_3_test = pd.DataFrame()
    # group4_3_tests = CT.test_category(tests,Group4_3,"Group4_3",all_runouts,group4_3_test)

    Group4_4 = G4C.Set_Flop(data)
    Group4_4.name = "Set_Flop"
    # Group4_4.to_csv("Set_Flop_Matchups_test.csv")

    #Group 5
    Group5_1 = G5C.Non_FlushClose_River(data)
    Group5_1.name = "Non_FlushClose_River"
    # group5_1_test = pd.DataFrame()
    # group5_1_tests = CT.test_category(tests,Group5_1,"Group5_1",all_runouts,group5_1_test)

    Group5_2 = G5C.FlushClose_River(data)
    Group5_2.name = "FlushClose_River"
    # group5_2_test = pd.DataFrame()
    # group5_2_tests = CT.test_category(tests,Group5_2,"Group5_2",all_runouts,group5_2_test)

    Group5_3 = G5C.Rainbow_Turn(data)
    Group5_3.name = "Rainbow_Turn"
    # group5_3_test = pd.DataFrame()
    # group5_3_tests = CT.test_category(tests,Group5_3,"Group5_3",all_runouts,group5_3_test)

    Group5_4 = G5C.FlushClose_Turn(data)
    Group5_4.name = "FlushClose_Turn"
    # group5_4_test = pd.DataFrame()
    # group5_4_tests = CT.test_category(tests,Group5_4,"Group5_4",all_runouts,group5_4_test)

    Group5_5 = G5C.Monotone_Flop(data)
    Group5_5.name = "Monotone_Flop"
    # group5_5_test = pd.DataFrame()
    # group5_5_tests = CT.test_category(tests,Group5_5,"Group5_5",all_runouts,group5_5_test)
    # Group5_5.to_csv("Monotone_Flop_Matchups_test.csv")
    #Group 6
    Group6_1 = G6C.FlushRiver_4Card(data)
    Group6_1.name = "FlushRiver_4Card"
    # group6_1_test = pd.DataFrame()
    # group6_1_tests = CT.test_category(tests,Group6_1,"Group6_1",all_runouts,group6_1_test)

    Group6_2 = G6C.StraightRiver_4Card(data)
    Group6_2.name = "StraightRiver_4Card"
    # group6_2_test = pd.DataFrame()
    # group6_2_tests = CT.test_category(tests,Group6_2,"Group6_2",all_runouts,group6_2_test)

    Group6_3 = G6C.FlushTurn_4Card(data)
    Group6_3.name = "FlushTurn_4Card"
    # group6_3_test = pd.DataFrame()
    # group6_3_tests = CT.test_category(tests,Group6_3,"Group6_3",all_runouts,group6_3_test)

    Group6_4 = G6C.StraightTurn_4Card(data)
    Group6_4.name = "StraightTurn_4Card"
    # group6_4_test = pd.DataFrame()
    # group6_4_tests = CT.test_category(tests,Group6_4,"Group6_4",all_runouts,group6_4_test)

    # Generate results csv
    # z is 1.96 for 95% confidence interval
    # For the old report betsize is 0.5, new report betsize is 0.3
    z_factor=1.96
    bs=betsize
    All_Categories = [Group1_1, Group1_2, Group1_3, Group2_1, Group2_2, Group2_3, Group2_4, Group3, Group4_1, Group4_2, Group4_3,Group4_4, Group5_1, Group5_2, Group5_3, Group5_4, Group5_5, Group6_1, Group6_2, Group6_3, Group6_4, Group1_0]
    results = MSF.stats_gen_complete(bs, z_factor, All_Categories, 1)
# All_Categories_tests = [group1_1_tests,group1_2_tests, group1_3_tests, group2_1_tests,group2_2_tests,group2_3_tests,group3_1_tests,group4_1_tests,group4_2_tests,group4_3_tests,group5_1_tests,group5_2_tests,group5_3_tests,group5_4_tests,group5_5_tests,group6_1_tests,group6_2_tests,group6_3_tests,group6_4_tests]
# all_tests = pd.DataFrame(columns = ["Category", "Test","Count","Runout_Full","In_DataSet?"])
# for j in All_Categories_tests:
#     all_tests = pd.concat([all_tests,j])
#     all_tests = all_tests[all_tests["Test"]!="Pass"]

# if (len(all_tests)==0)&(len(results)==21)&(StatTest.Test_Stats()==True):
#     print("All Tests Passed")
# if (len(all_tests)==0)&(StatTest.Test_Stats()==True)&(len(results)!=21):
#     print("Tests passed, but results is missing data")
# if (len(all_tests)!=0)&(StatTest.Test_Stats()!=True)&(len(results)==21):
#     print("Tests Failed")
    
    return results
# raw_data = pd.read_csv("report.csv",skiprows=3,header=None)
# new_header = raw_data.iloc[0]
# raw_data = raw_data[1:]
# raw_data.columns = new_header
# print(ReportGenerator2000(0.3,raw_data)[["Category(1)","% Total Matchups"]])


