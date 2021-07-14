import pandas as pd


df1=pd.read_csv("C:\\Users\\Lenovo\\Downloads\\results\\submission.csv")
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print(df1.head(10))