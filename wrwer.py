
import pandas as pd

filename = "./big-mac-full-index.csv"           #./ means in this directory while if you dont its general
df = pd.read_csv(filename)

print(df)
print(type(df['dollar_price']))

print(df.columns)
