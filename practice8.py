import pandas as pd
import pandas as pd

df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul', 'Sneha',
             'Ajay', 'Kiran', 'Maya'],
    'language': ['Python', 'Java', 'Python', 'Java',
                 'Python', 'Java', 'C++', 'C++'],
    'marks': [90, 75, 85, 65, 95, 80, 70, 88],
    'age': [19, 20, 18, 21, 19, 20, 18, 21],
    'city': ['Hyd', 'Chennai', 'Hyd', 'Mumbai',
             'Chennai', 'Hyd', 'Mumbai', 'Hyd']
})
s = df.query('marks >= 80 and age <= 20').sort_values(by='marks' , ascending = False)
print(s[['name','marks','age']])
city_stats = df.groupby('city').agg(
    average_marks=('marks', 'mean'),
    maximum_marks=('marks', 'max'),
    student_count=('name', 'count')
)

print(city_stats)
df['city_avg']=df.groupby('city')['marks'].transform('mean')
print(df)
language_percentage = df['language'].value_counts(normalize=True) * 100
print(language_percentage)
language_city = df.pivot_table(
    index='language',
    columns='city',
    values='marks',
    aggfunc='mean'
)
print(language_city)