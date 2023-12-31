import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()


df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count() # number of variables over 50 years old


df.loc[df["age"] > 50, "class"].head()

df.loc[df["age"] > 50, ["age" , "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age" , "class"]].head()

df_new = df.loc[(df["age"] > 50) & 
       (df["sex"] == "male") & 
       ((df["embark_town"] == "Cherbourg" ) | (  df["embark_town"] == "Southampton") ) , 
       ["age" , "class", "embark_town"]].head()
df_new["embark_town"].value_counts()

