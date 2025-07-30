import pandas as pd 
import random



df=pd.read_csv("Data\customers.csv")
df["score"]= [random.randint(60, 100) for x in range(len(df))]
#print(df.head(30))

new_df=df.head(3)

print(new_df)

total_score =new_df["score"].sum()
print(total_score)

evarage =new_df["score"].mean()
print(evarage)




total_score =df["score"].sum()
print(total_score)

evarage =df["score"].mean()
print(evarage)


count = evarage =df["score"].count()
print(count)