import pandas as pd

df = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])


columns = df.columns.drop('KRAJE')
max_growth = df[columns].max().max()
year_with_max_growth = df[columns].max().idxmax()
country_with_max_growth = df.loc[df[year_with_max_growth].idxmax(), 'KRAJE']


print(f"Największy przyrost ludności: {max_growth}")
print(f"Kraj: {country_with_max_growth}, Rok: {year_with_max_growth}")