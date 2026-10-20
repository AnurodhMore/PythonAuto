import numpy as np
import pandas as pd
from pandas import pivot_table

df = pd.read_excel('/Users/anurodhmore/Downloads/supermarket_sales.xlsx')
df = df[['Gender','Product line','Total']]

pivot_table =  df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc=sum)

pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report')