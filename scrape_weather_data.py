import pandas as pd

url = 'https://www.accuweather.com/en/in/bengaluru/204108/{}-weather/204108?monyr={}/1/{}&view=table'

months = {'1':'january',
         '2':'february',
         '3':'march',
         '4':'april',
         '5':'may',
         '6':'june',
         '7':'july',
         '8':'august',
         '9':'september',
         '10':'october',
         '11':'november',
         '12':'december'}

year = '2017'

df_annual = pd.DataFrame()

for i in range(1,13):
    df_list = pd.read_html(url.format(months[str(i)], str(i), year))
    df = df_list[0]
    df1 = df[['Date', 'Hi/Lo', 'Precip', 'Forecast']]
    df_annual = df_annual.append(df1,ignore_index=True)
    
#print (df_annual)

df_annual.to_csv('{}_weather.csv'.format(year))
