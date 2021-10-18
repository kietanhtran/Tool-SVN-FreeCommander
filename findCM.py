#! /usr/bin/env python
import pandas as pd

input=input("Find ticket: ")
ticket="IA "+input

xls_path=[
"D:/RCAR/xOS2/trunk/00_Investigation_Document/Impact_Analysis/Modules/GPT/R-CarGen3_MCAL_GPT_ChangeManagement_001.xlsx",
"D:/RCAR/xOS2/trunk/00_Investigation_Document/Impact_Analysis/Modules/GPT/R-CarGen3_MCAL_GPT_ChangeManagement_002.xlsx",
"D:/RCAR/xOS2/trunk/00_Investigation_Document/Impact_Analysis/Modules/GPT/R-CarGen3_MCAL_GPT_ChangeManagement_003.xlsx",
"D:/RCAR/xOS2/trunk/00_Investigation_Document/Impact_Analysis/Modules/GPT/R-CarGen3_MCAL_GPT_ChangeManagement_004.xlsx",
"D:/RCAR/xOS2/trunk/00_Investigation_Document/Impact_Analysis/Modules/GPT/R-CarGen3_MCAL_GPT_ChangeManagement_005.xlsx",
]
def main():
    for file in xls_path:
        xl = pd.ExcelFile(file) 
        for idx, name in enumerate(xl.sheet_names):
            my_list = []
            if isinstance(name, str):
                my_list.append(name)
            if ticket in my_list:
                print (ticket,"is in file", file)
                break
if __name__ == "__main__":
    main()