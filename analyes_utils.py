import pandas as pd

def read_list(csv_path):
   return  pd.read_csv(csv_path)

def class_table(df):
   table=pd.pivot_table(df,values=["math","english","japanese"],aggfunc="mean",index="class")
   return table