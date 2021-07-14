import pandas as pd
url = "https://raw.githubusercontent.com/GokuMohandas/MadeWithML/main/datasets/titanic.csv"
df = pd.read_csv(url, header=0)
pd.set_option('display.max_columns', None)
 #Show all lines
pd.set_option('display.max_rows', None)
#pd.set_option('max_colwidth',100)
print(df.head(3))