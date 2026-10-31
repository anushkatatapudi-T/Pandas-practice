import pandas as pd
df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha', 'Ajay'],
    'marks': [90, 75, 85, 65, 95, 80],
    'language': ['Python', 'Java', 'Python', 'Java', 'Python', 'Java'],
    'age': [19, 20, 18, 21, 19, 20]
})
great = df.sort_values(by='marks',ascending=False).head(3)
print(great[['name','marks']])
count=df['language'].value_counts()
print(count)

avg_age = df.groupby('age')['marks'].mean()
print(avg_age)

g = df[(df['marks']>=80) & (df['age'] <= 19)]
print(g[['name','marks','age']])
print(df.loc[df['marks'].idxmin()])