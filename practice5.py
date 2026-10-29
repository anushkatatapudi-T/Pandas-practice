import pandas as pd
# df = pd.DataFrame({
#     'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha'],
#     'marks': [90, None, 85, None, 72],
#     'city': ['Hyderabad', 'Chennai', None, 'Mumbai', None]
# })
# df['marks']=df['marks'].fillna(0)
# df['city']=df['city'].fillna('Unknown')

# print(df)
# df = pd.DataFrame({
#     'name': ['Anu', 'Ravi', 'Priya', 'Rahul'],
#     'marks': [80, None, 95, None],
#     'age': [19, 20, None, 21]
# })
# avg= df['marks'].mean()
# df['marks']=df['marks'].fillna(avg)
# df['age']=df['age'].fillna(18)
# print(df)

df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha', 'Ajay'],
    'language': ['Python', 'Java', 'Python', 'Java', 'Python', 'Java'],
    'marks': [90, 75, 85, 65, 95, 80]
})
avg = df.groupby('language')['marks'].mean()
print(avg)
print(df[df['marks']>=95]) #or
print(df.query('marks >= 95'))
df['results'] = df['marks'].apply(
    lambda x : 'Pass' if x >= 80 else 'Fail'
)
print(df[['name','marks','results']])