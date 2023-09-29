import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv('big-mac-full-index.csv')

query = f"(iso_a3 == 'NZL' or iso_a3 == 'DNK')"

df_result = df.query(query)

mean_dollar_price = df_result['dollar_price'].mean()

mean_dollar_price_two_decimals = round(mean_dollar_price,2)

# print(mean_dollar_price)
# print(mean_dollar_price_two_decimals)

# print(df_result.min())
# print(df_result['dollar_price'].max())
# print(round(df_result['dollar_price'].median(),3))


#new area
#YYYY-MM-DY
# year = '2000'          #{year}                  {year}              v to isolate a country
# country = 'Argentina' #could do the same as year but instead over here
# new_query = f"(date >= '2000-01-01' and date <= '2000-12-31' and iso_a3 == 'CHL')"

# df_by_date = df.query(new_query)
# print(df_by_date)

# print(df)

# doing2years = '2017'                               #this adds 2018
# new_query = f"(date >= '{year}-01-01' and date <= '{int(year)+1}-12-31' and iso_a3 == 'CHL')"

#The row that has the minimum value of bigmac

index_of_min_value = df['dollar_price'].idxmin()

print(index_of_min_value)
#^prints which index its at

print(df.loc[index_of_min_value]) #returns a series
