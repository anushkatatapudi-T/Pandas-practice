import pandas as pd

df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha',
             'Ajay', 'Kiran', 'Maya', 'Teja', 'Riya'],
    'marks': [90, 45, 85, 65, 95, 40, 70, 88, 55, 92],
    'language': ['Python', 'Java', 'Python', 'Java', 'Python',
                 'C++', 'C++', 'Java', 'Python', 'C++'],
    'age': [19, 20, 18, 21, 19, 20, 18, 21, 19, 20],
    'city': ['Hyd', 'Chennai', 'Hyd', 'Mumbai', 'Chennai',
             'Hyd', 'Mumbai', 'Hyd', 'Chennai', 'Mumbai']
})
# df['result']=df['marks'].apply(
#     lambda x : "Pass" if x >= 80 else "Fail"
# )
# print(df)
# df['level_code']=df['language'].map({
#     'Python':1,
#     'Java':2,
#     'C++':3
# })
# print(df)
data = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha'],
    'marks': [90, None, 85, None, 75],
    'city': ['Hyd', 'Chennai', None, 'Mumbai', None]
})

avg = data['marks'].mean()
data['marks']=data['marks'].fillna(avg)
data['city']=data['city'].fillna('Unknown')
print(data)

top_student=(
    df.sort_values('marks',ascending=False)
    .groupby('language')
    .head(1)
)
print(top_student[['language','name','marks']])
high_scorers = (
    df.query('marks >= 80')
      .groupby('language')
      .size()
)
print(high_scorers)