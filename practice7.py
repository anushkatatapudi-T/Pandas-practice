
import pandas as pd

df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha', 'Ajay'],
    'language': ['Python', 'Java', 'Python', 'Java', 'Python', 'Java'],
    'marks': [90, 75, 85, 65, 95, 80],
    'age': [19, 20, 18, 21, 19, 20]
})
avg = df.groupby('language')['marks'].agg(['mean','max','min','sum'])
print(avg)
df['language_avg']=df.groupby('language')['marks'].transform('mean')
print(df)
df['rank']=df['marks'].rank(ascending=False)

df['performance']=pd.cut(
    df['marks'],
    bins = [0, 70, 80, 90, 100],
    labels=['needs improvement', 'average', 'good', 'excellent']
)
print(df)
final = df.pivot_table(
    index='language',
    columns='age',
    values='marks',
    aggfunc='mean'
)

print(final)