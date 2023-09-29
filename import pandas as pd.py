import pandas as pd

colors = ['orange','white','blue','green']

print(type(colors))

colors_series = pd.Series(colors)

print(type(colors_series))

print(colors_series)

students = {"Kansas":"Yvan","New Mexico":"Adbel","Wisconsin":"Jon","Tennesee":"Andruw"}

print(type(students))

print(students.values())
print(students.keys())

student_series = pd.Series(data=students.values(),)



#Panda queries
df = pd.read_csv(filename)
query = f"(iso_a3 == 'MEX')"
mxn_df = df.query(query)

print(mxn_df)

df_mex.to_csv('mexico_report.csv')

#products mean product reviews