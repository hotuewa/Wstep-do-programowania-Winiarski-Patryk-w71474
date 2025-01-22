import pandas as pd

data = {
    'Numer ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}
df_pracownicy = pd.DataFrame(data)


wysokie_pensje = df_pracownicy[df_pracownicy['Pensja'] > 5000]
print(wysokie_pensje)


sortowanie_po_wieku = df_pracownicy.sort_values(by='Wiek')
print(sortowanie_po_wieku)


stanowisko_i_srednia= df_pracownicy.groupby('Stanowisko')['Pensja'].mean()
print(stanowisko_i_srednia)


data_awans = {
    'Numer ID': [2, 3],
    'Nowe Stanowisko': ['Manager', 'Senior Konsultant']
}
df_awans = pd.DataFrame(data_awans)

df_polaczony = pd.merge(df_pracownicy, df_awans, on='Numer ID', how='left')
print(df_polaczony)


df_polaczony.to_csv('pracownicy.csv', index=False)
df_nowy = pd.read_csv('pracownicy.csv')
print(df_nowy)