
import pandas as pd 
df=pd.read_csv(r"Data\region_sales.csv")
#print(df.head(10))

#print(df["sales"].sum())
new_df=pd.DataFrame()
#df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

new_df['total sales']=pd.to_numeric(df['sales'], errors='coerce')

print(type(df))
print(new_df['total sales'].sum())
#totalsale =new_df['slaes']. sum()
