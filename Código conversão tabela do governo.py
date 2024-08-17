# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:49:16 2023

@author: edgar
"""



import pandas as pd
import numpy as np
import matplotlib as mpl
import random as ri


FilePath = 'C:/Users/edgar/Downloads/Power BI'
FileName = 'Dengue 2023 - www.saude.sp.gov.brcve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranja.xlsx'
"FileName = 'Dengue 2023 - www.saude.sp.gov.brcve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranja - Copia.xlsx'"
dfs = pd.read_excel(FilePath+'/'+FileName,sheet_name=0)
    
print(dfs)
"""for key, value in dfs.items():
    print(key)
sala = np.array(sala)
print(pd.DataFrame.from_dict(sala, orient='index'))"""