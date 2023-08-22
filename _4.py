import pandas as pd
df=pd.DataFrame(columns=['name','age','per'])
df.loc[0]=['Abhi',19,88]
df.loc[1]=['Om',19,77]
df.loc[2]=['sai',19,67]
df.loc[3]=['ram',19,47]

df.loc[4]=['om',10,88]
df.loc[5]=['','','']

df.loc[6]=['om',10,88]
df.loc[7]=['','','']
df["remarks"]=''
print(df)
