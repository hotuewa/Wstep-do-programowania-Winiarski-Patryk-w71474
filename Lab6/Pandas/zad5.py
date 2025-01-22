import pandas as pd


data_studenci = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
df_studenci = pd.DataFrame(data_studenci)


high_grades = df_studenci[df_studenci['Ocena'] > 4]
print(high_grades)


sorted_studenci = df_studenci.sort_values(by='Wiek')
print(sorted_studenci)


oceny_i_wiek = df_studenci.groupby('Ocena')['Wiek'].mean()
print(oceny_i_wiek)


data_poprawa = {
    'Nr_albumu': [2, 5],
    'Ocena_poprawa': [4.0, 3.5]
}
df_poprawa = pd.DataFrame(data_poprawa)

df_studenci_polaczony = pd.merge(df_studenci, df_poprawa, on='Nr_albumu', how='left')
print(df_studenci_polaczony)


df_studenci.to_csv('studenci.csv', index=False)
df_studenci_nowy = pd.read_csv('studenci.csv')
print(df_studenci_nowy)


nowy_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imię': ['Patryk'],
    'Nazwisko': ['Winiarski'],
    'Ocena': [5.0],
    'Wiek': [20]
})
df_studenci = pd.concat([df_studenci, nowy_student], ignore_index=True)
print(df_studenci)


unikalne_oceny = df_studenci['Ocena'].unique()
print(unikalne_oceny)


studenci_z_5 = len(df_studenci[df_studenci['Ocena'] == 5])
print(f"Liczba studentów z oceną 5: {studenci_z_5}")