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
filtered_students=df.groupby('language').filter(lambda group : group['marks'].mean() > 75)
print(filtered_students)

language_avg = df.groupby('language')['marks'].transform('mean')

above_avg = df[df['marks'] > language_avg][['name', 'language', 'marks']]

print(above_avg)

language_stats=df.groupby('language')['marks'].agg(['max','mean','min','count'])
print(language_stats)

city_language_avg = df.pivot_table(
    index='language',
    columns='city',
    values='marks',
    aggfunc='mean'

)
print(city_language_avg.fillna('Unknown'))
print(df.duplicated().any())
dup_rows = df[df.duplicated()]
clean_df=df.drop_duplicates()
print(clean_df)