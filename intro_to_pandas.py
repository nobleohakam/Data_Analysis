#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:14:20 2024

@author: nobleohakam
"""

import pandas as pd 
import numpy as np
  
# Calling DataFrame constructor 
df = pd.DataFrame() 
print(df)

# list of strings 
#s_lst = ['This', 'is', 'a', 'Data', 'Frame'] 

#dictionary of lists
lst = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
#print(df)

#call specific columns in list
#print(df[['Name', 'Age']])
#print(df['Address'])


#call specific row in list
first_row = df.iloc[0]
#print(first_row)

#reading each one of the items in the list 
for i, j in df.iterrows():
    print(i, j)
    print()

# Creating empty series 
ser = pd.Series() 
print("Pandas Series: ", ser) 

# simple array 
data = np.array(['This', 'is', 'a', 'Panda', 'Series']) 
  
ser = pd.Series(data) 
print("Pandas Series:\n", ser)