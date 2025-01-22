import pandas as pd


df = pd.read_csv('demografia.csv', decimal=',', na_values=['NA', 'n/a', 'NaN'])

najwiekszy_przyrost = df.loc[df['2022'].idxmax(),"KRAJE"]
print(f"Kraj z największym przyrostem w 2022 roku: {najwiekszy_przyrost}")