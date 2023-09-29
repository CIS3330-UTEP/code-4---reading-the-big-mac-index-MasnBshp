import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('big-mac-full-index.csv')
# year = int(input("Enter the year of interest: "))
# country_code = input("Enter the country code: ").upper()

def get_big_mac_price_by_year(year,country_code):
    #print(year)
    #print(country_code)
    #query = f"(iso_a3 == '{country_code}' and date == '{year}')"
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
    df_result = df.query(query)
    mean_dollar_price = (round(df_result['dollar_price'].mean(),2))
    return mean_dollar_price

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code.upper()}')"
    df_result = df.query(query)
    dollar_price_of_country = (round(df_result['dollar_price'].mean(),2))
    return dollar_price_of_country


def get_the_cheapest_big_mac_price_by_year(year):

    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query)
    getmin_query = df_result['dollar_price'].idxmin()
    cheapest_big_mac = round(df_result.loc[getmin_query]['dollar_price'],2)    
    row = df_result.loc[getmin_query]
    country_name = row['name']
    iso_a3 = row['iso_a3']
    sentence_cheapest_big_mac = f"{country_name}({iso_a3}): ${cheapest_big_mac}"
    return sentence_cheapest_big_mac


    #row = df_result.loc[0]
    #return row
    #concatenation = (df_result['name'])+(df_result['iso_a3'])
    to_print_out_cheapest_big_mac = f"the output for {year} will be: " + (df_result['name'])+(df_result['iso_a3']) + f" : {cheapest_big_mac}" 
    #return cheapest_big_mac
    return to_print_out_cheapest_big_mac
    #country_min_cost = (round(return_of_series['dollar_price'].idxmin()))
    #testvideo = df.loc[(return_of_series['date'] >= '{year}-01-01') & (return_of_series['date'] <= '{year}-12-31')]
    
    #return testvideo#country_min_cost
   # min
#Year(date)
#      print(df_result['dollar_price'].min())
#     #return message, in 2008, the message is Malaysia(MYS): $1.7
def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query)
    getmax_query = df_result['dollar_price'].idxmax()
    expensive_big_mac = round(df_result.loc[getmax_query]['dollar_price'],2)    
    row = df_result.loc[getmax_query]
    country_name = row['name']
    iso_a3 = row['iso_a3']
    sentence_expensive_big_mac = f"{country_name}({iso_a3}): ${expensive_big_mac}"
    return sentence_expensive_big_mac

if __name__ == "__main__":
    pass # Remove this line and code your user interface
    year = int(input("Enter the year of interest: "))
    country_code = input("Enter the country code: ").lower()
    result_a = get_big_mac_price_by_year(year,country_code)
    print(f"The price of a bigmac in {year}, location: {country_code}, was ${result_a}.")
    
    result_b = get_big_mac_price_by_country(country_code)
    print(f"The mean price of a bigmac was currently ${result_b}.")

    result_c = get_the_cheapest_big_mac_price_by_year(year)

    print(f"The cheapest bigmac in {year} was in {result_c}")

    result_d = get_the_most_expensive_big_mac_price_by_year(year)

    print(f"The most expensive bigmac in {year} was in {result_d}")