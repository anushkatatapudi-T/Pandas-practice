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

print(df)
missing = df.isnull().sum()
print(missing)
total_missing =  missing.sum()
print(total_missing)

df['city']=df['city'].replace('Hyd','Hyderabad')
print(df['city'].value_counts())
print(df)

top_city_students = df.sort_values(by='marks',ascending=False)
print(top_city_students.drop_duplicates(subset='city'))