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
df['city_rank'] =df.groupby('city')['marks'].rank(ascending=False)
print(df)
unique_cities = df['city'].drop_duplicates()
print(unique_cities)
total_languages=df['language'].nunique()
print(total_languages)
missing_values = df.isnull().sum()
print(missing_values)
df['language']=df['language'].replace('C++','Cpp')
print(df['language'])
duplicate_cities=df[df['city'].duplicated()]
print(duplicate_cities)