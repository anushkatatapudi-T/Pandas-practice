import pandas as pd
data = {
    'name' : [
        'anu', 'ravi', 'priya', 'kiran', 'maya',
        'rahul', 'sneha', 'arjun', 'divya', 'rohan',
        'neha', 'vijay', 'meena', 'ajay', 'kavya',
        'suresh', 'pavani', 'teja', 'nikhil', 'riya'
    ],
    'marks' : [
        98, 87, 97, 65, 76,
        88, 92, 54, 81, 73,
        25, 68, 84, 90, 79,
        61, 89, 22, 96, 85
    ],
    'language':[
        'java', 'python', 'java', 'c++', 'python',
        'java', 'python', 'c++', 'java', 'python',
        'java', 'c++', 'python', 'java', 'python',
        'c++', 'java', 'python', 'java', 'python'
    ],
    'age':[
        18, 19, 18, 20, 22,
        19, 18, 21, 20, 19,
        18, 22, 20, 19, 18,
        21, 20, 19, 18, 21
    ]
}
df = pd.DataFrame(data)
# print(df)
#Filter students
filter_students = df.query('marks >= 80')
# print(filter_students)
#sort values
sort_values = df.sort_values(by='marks' , ascending=False)
# print(sort_values)
#count subjects
count_lang=df['language'].value_counts()
print(count_lang)
#calculate avg
print(df.groupby('language')['marks'].mean())
#find the topper
print(df.loc[df['marks'].idxmax()])
#select top-5
top= df.sort_values(by='marks' , ascending=False).head(5)[['name','marks']]
print(top)
#filter with two conditions
print(df.query('age > 18 and marks >=90'))
#find maximum by subject
print(df.groupby('language')['marks'].max())
#missing values
print(df.isnull().sum())
#create a new column 
df['result'] = df['marks'].apply(
    lambda x : 'Pass' if x >= 40 else 'Fail'
)
print(df[['name','marks','result']])