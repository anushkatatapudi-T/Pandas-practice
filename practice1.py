import pandas as pd
df =pd.read_csv('data.csv')
print(df[df['marks'] >85 ])
print(df.query('marks > 85'))
m = df.groupby('subject')['marks'].mean()
print(m)
print(df.sort_values(
    by ='marks',
    ascending=False
    ))
data = df[df['marks']>80].sort_values(by='marks',ascending=False)
print(data)
maximum = df.loc[df['marks'].idxmax()]
print(maximum)
top = df.sort_values(by='marks',ascending=False).head(2)
print(top[['name','marks']])
value = df['subject'].value_counts()
print(value)