"""
EDA Refractarios
"""
import pandas as pd
import os

# Working directory
os.chdir('C:\\proyectos 2025\\refractarios')

# load data
df0=pd.read_csv('prod_2324.csv')

# EDA
df0.head()
