# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:33:09 2021

@author: ebenezer.an
"""

import requests
import pandas as pd
import string
import numpy as np
import sys


# In[Class for Pulling Data]

class DataPull:
    
    def __init__(self):
        self.lowercase_letters = list(string.ascii_lowercase)

        
    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):        
        if exc_type == TypeError:
            print(f"An exception occurred - {exc_val} line {exc_tb.tb_lineno}")
            print('You have entered a value that is not a string. Please use public root URL like "https://public.wiwdata.com/"')
        elif exc_type == FileNotFoundError:
            print(f"An exception occurred - {exc_val} line {exc_tb.tb_lineno}")
            print('Non existent public root URL provided. Please provide an accurate directory"')
        elif exc_type == IndexError or exc_type == NameError:
            print(f"An exception occurred {exc_val} line {exc_tb.tb_lineno}")
            print('Please provide a public root URL like "https://public.wiwdata.com/"')
        elif exc_type != None:
            print(f"An exception occurred - {exc_type}")
            print(f"{exc_val} at line {exc_tb.tb_lineno}")
        else:
            print("Program Successfully Finished!")
            
        return self
    
    
    def pull_files(self, path):
        dataframe = pd.DataFrame()

        for letter in self.lowercase_letters:
            data = pd.read_csv(path + letter + '.csv')
            dataframe = pd.concat([dataframe, data], sort = False, ignore_index=True)            
            print('Pulling file: ' + letter + '.csv')
    
        return dataframe
    
    
    def transform_data(self, d_frame):
        data_pivot = pd.pivot_table(d_frame, values=['length'], index=['user_id'], columns=['path'], aggfunc=np.sum, fill_value=0)
        data_pivot.reset_index(level=data_pivot.index.names, inplace=True)        
        data_pivot.columns = data_pivot.columns.map(lambda x: (x[1] + " " + x[0].replace('length', '')).strip() if x[1] != '' else (x[0].replace('length', '')).strip())

        return data_pivot
    
    
    def create_csv(self, pivot, file_name):
        pivot.to_csv(file_name, index = False)
                
        
# In[]

try:    
    path = sys.argv[1]
except IndexError:
    pass
    
with DataPull() as data_pull:
    user_data = data_pull.pull_files(path)
    user_pivot = data_pull.transform_data(user_data)
    data_pull.create_csv(user_pivot, 'User Journey.csv')


    
    
    
        
