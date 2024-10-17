#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:59:12 2024

@author: nobleohakam
"""
#one way to read an excel file with pandas and python
# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file

excel_file = input("write a name of a file in this dir: ")
print(excel_file)

dataframe1 = pd.read_excel(excel_file)

print(dataframe1)

#get the top 5 rows in the file
top_data = dataframe1.head()
top_data
