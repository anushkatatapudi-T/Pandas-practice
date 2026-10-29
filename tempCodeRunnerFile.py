df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul'],
    'marks': [80, None, 95, None],
    'age': [19, 20, None, 21]
})
avg= df['marks'].mean()
df['marks']=df['marks'].fillna(avg)
df['age']=df['age'].fillna(18)
print(df)