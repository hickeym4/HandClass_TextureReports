import pandas as pd
import numpy as np
import sys, os
import Report_Generator_v1 as RepGen
import Mike_Stats_Functions as MSF
import Organize_Data_Functions as ODF
from pathlib import Path
pd.set_option('display.max_colwidth',None)
base_path = r'C:\Users\cam\Downloads\Robby-HandClasses-main\Robby-HandClasses-main\Reports_Round_1_2'
positions = os.listdir(base_path)
run_summary = pd.DataFrame(columns = ["Reports Found","Texture-Report Name","Bet Size","Error Log"])
rng = np.random.default_rng()
# for p in positions:
#     path2 = os.path.join(base_path,p)
#     list2 = os.listdir(path2)
#     for n in list2:
#         path3 = os.path.join(path2,n)
#         list3 = os.listdir(path3)
#         for AD in list3:
#             path4 = os.path.join(path3,AD)
#             list4 = os.listdir(path4)
#             for line in list4:
#                 #Delete this when fixed
#                 print(path2)
#                 print(path3)
#                 print(path4)
#                 print(line)
#                 run_report_start = 43
#                 error = ""
#                 betsize = 0
                
#                 report_name_string = "PotCaptureReport"+str(p)+"_"+str(n)+"_"+str(AD)+"_"+str(line)
#                 finalpath = os.path.join(path4,line)
#                 namecheck = finalpath
#                 finalpath = os.path.join(finalpath,"report.csv")
#                 #check if betsize is in file name
#                 if ODF.check_report_naming_format_betsize(namecheck):
#                     #get bet size
#                     betstr_1 = str(line).rsplit('-', 1)[-1]
#                     #check for "r"
#                     if 'r' in betstr_1:
#                         betstr_1 = float(betstr_1.rsplit('r',1)[0])
#                     else:
#                         betstr_1 = float(betstr_1)
#                     #check for decimal or pct value
#                     if betstr_1 > 1:
#                         betsize = betstr_1/100
#                     else:
#                         betsize = betstr_1
#                 else:
#                     betsize = "no betsize in file name!"

#                 if os.path.isfile(finalpath):
#                     raw_data = pd.read_csv(finalpath,skiprows=3,header=None)
#                     new_header = raw_data.iloc[0]
#                     raw_data = raw_data[1:]
#                     raw_data.columns = new_header
#                     if (isinstance(betsize, int) or isinstance(betsize, float)):
#                         #check fold frequency column
#                         if ODF.check_report_columns(raw_data):
#                             report_output_folder = r'C:\Users\cam\Downloads\Robby-HandClasses-main\Robby-HandClasses-main\TextureReports_Complete'
#                             # report_output_name = "Report_#"+str(len(run_summary))+".csv"
#                             if "IP" in str(finalpath):
#                                 report_output_name = str(line)+"_IP_betsize"+str(betsize)+".csv"
#                             if "OOP" in str(finalpath):
#                                 report_output_name = str(line)+"_OOP_betsize"+str(betsize)+".csv"
#                         else:
#                             report_output_name= "Texture report not generated, no fold frequency column"
#                     elif not (isinstance(betsize, int) or isinstance(betsize, float)) and ODF.check_report_columns == False:
#                         report_output_name= "Texture report not generated, no betsize, no fold frequency column"
#                     else:
#                         report_output_name= "Texture report not generated, no betsize"
#                 else:
#                     report_output_name = "Texture report not generated, file doesn't exist"
                
#                 new_summary_row = pd.DataFrame(columns=["Reports Found","Texture-Report Name","Bet Size","Error Log"],data=[[finalpath,report_output_name,betsize,error]])
#                 run_summary=pd.concat([run_summary,new_summary_row])
#                 run_summary.to_csv("Run_Preview_26_July_2024.csv")

for p in positions:
    path2 = os.path.join(base_path,p)
    list2 = os.listdir(path2)
    for n in list2:
        path3 = os.path.join(path2,n)
        list3 = os.listdir(path3)
        for AD in list3:
            path4 = os.path.join(path3,AD)
            list4 = os.listdir(path4)
            for line in list4:
                # run_report_start = 43
                error = ""
                betsize = 0
                
                report_name_string = "PotCaptureReport"+str(p)+"_"+str(n)+"_"+str(AD)+"_"+str(line)
                finalpath = os.path.join(path4,line)
                namecheck = finalpath
                finalpath = os.path.join(finalpath,"report.csv")
                #check if betsize is in file name
                if ODF.check_report_naming_format_betsize(namecheck):
                    #get bet size
                    betstr_1 = str(line).rsplit('-', 1)[-1]
                    #check for "r"
                    if 'r' in betstr_1:
                        betstr_1 = float(betstr_1.rsplit('r',1)[0])
                    else:
                        betstr_1 = float(betstr_1)
                    #check for decimal or pct value
                    if betstr_1 > 1:
                        betsize = betstr_1/100
                    else:
                        betsize = betstr_1
                else:
                    betsize = "no betsize in file name!"

                if os.path.isfile(finalpath):
                    raw_data = pd.read_csv(finalpath,skiprows=3,header=None)
                    new_header = raw_data.iloc[0]
                    raw_data = raw_data[1:]
                    raw_data.columns = new_header
                    if (isinstance(betsize, int) or isinstance(betsize, float)):
                        #check fold frequency column
                        if ODF.check_report_columns(raw_data):
                            report_output_folder = r'C:\Users\cam\Downloads\Robby-HandClasses-main\Robby-HandClasses-main\TextureReports_Complete_2'
                            # report_output_name = "Report_#"+str(len(run_summary))+".csv"
                            if "IP" in str(finalpath):
                                report_output_name = str(line)+"_IP_betsize"+str(betsize)+".csv"
                            if "OOP" in str(finalpath):
                                report_output_name = str(line)+"_OOP_betsize"+str(betsize)+".csv"
                            # if report_output_name not in pd.read_csv("Run_Summary_26_July_2024.csv")["Texture-Report Name"].tolist():
                            report_output = RepGen.ReportGenerator2000(betsize,raw_data)
                            report_output.to_csv(os.path.join(report_output_folder,report_output_name))
                        else:
                            report_output_name= "Texture report not generated, no fold frequency column"
                    elif not (isinstance(betsize, int) or isinstance(betsize, float)) and ODF.check_report_columns == False:
                        report_output_name= "Texture report not generated, no betsize, no fold frequency column"
                    else:
                        report_output_name= "Texture report not generated, no betsize"
                else:
                    report_output_name = "Texture report not generated, file doesn't exist"
                
                new_summary_row = pd.DataFrame(columns=["Reports Found","Texture-Report Name","Bet Size","Error Log"],data=[[finalpath,report_output_name,betsize,error]])
                run_summary=pd.concat([run_summary,new_summary_row])
                run_summary.to_csv("Run_Summary_06_AUG_2024.csv")
base_path = r'C:\Users\cam\Downloads\Robby-HandClasses-main\Robby-HandClasses-main\TextureReports_Complete_2'
filenames = os.listdir(base_path)
# Initialize an empty list to store dataframes
dataframes = []
# # Read each file and append the dataframe to the list
for file in filenames:
    data_ = pd.read_csv(os.path.join(base_path,file))
    cleaned_string=str(file).replace(".csv","")
    data_["Line"] = cleaned_string
    data_["Line"] = data_["Line"].where(data_["Category(1)"]=="AceHighOverRiver")
    dataframes.append(data_)

# Concatenate all dataframes into one
combined_df = pd.concat(dataframes, ignore_index=True)
combined_df=combined_df.drop(columns=combined_df.columns[0])
# Save the combined dataframe to a new CSV file
combined_df.to_csv('combined_reports_20_AUG_2024.csv', index=False)