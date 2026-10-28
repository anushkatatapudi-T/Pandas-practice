import pandas as pd
data = {
    'name': ['anu', 'ravi', 'priya', 'kiran', 'maya'],
    'marks': [98, 87, 97, 65, 76],
    'language': ['java', 'python', 'java', 'c++', 'python'],
    'age': [18, 19, 18, 20, 22]
}
df = pd.DataFrame(data)
#first 5
print(df.head())
#number of rows and columns
print(df.shape)
#display name and marks
print(df[['name','marks']])
#marks > 80
print(df.query('marks > 80'))
#sort by marks (desc)
print(df.sort_values(by = 'marks',ascending = False))
#columns  name and language
print(df[['name','language']])
#sort marks from low - high
print(df.sort_values(by='marks' , ascending=True))
#counts
print(df['language'].value_counts())
#avg
print(df.groupby('language')['marks'].mean())
#hightest marks row
print(df.loc[df['marks'].idxmax()])
#new column
#apply()
df['result'] = df['marks'].apply(
    lambda x : "A" if x >= 90 else
               "B" if x >= 80 else
               "C" if x >= 70 else
               "D" if x >= 60 else
               "F"
)  
print(df[['name','marks','result']])
#map
import pandas as pd

df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul'],
    'subject': ['java', 'python', 'java', 'python']
})
df['subject-code']=df['subject'].map({
    'java':101,
    'python':102
})
print(df)
#map
df['city'] =['Hyderabad', 'Chennai', 'Hyderabad', 'Mumbai']
df['city-code']=df['city'].map({
    'Hyderabad': 1,
    'Chennai':2,
    'Mumbai' : 3
    })
print(df)
#map
df['level']=['beginner','advanced','intermediate','beginner']
df['level_code'] = df['level'].map({
    'beginner':1,
    'intermediate':2,
    'advanced':3
})
print(df)
#fillna
df = pd.DataFrame({
    'name': ['Anu', 'Ravi', 'Priya', 'Rahul'],
    'marks': [90, None, 85, None]
})
df['marks']=df['marks'].fillna(0)
print(df)