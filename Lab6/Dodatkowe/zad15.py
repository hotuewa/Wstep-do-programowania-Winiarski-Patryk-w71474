import pandas as pd
import matplotlib.pyplot as plt


data_oceny = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Ocena_1_termin': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Ocena_2_termin': [4.7, 3.5, 5.0, 4.0, 3.0]
}
df_oceny = pd.DataFrame(data_oceny)


plt.plot(df_oceny['Nr_albumu'], df_oceny['Ocena_1_termin'], label='1. termin', marker='o')
plt.plot(df_oceny['Nr_albumu'], df_oceny['Ocena_2_termin'], label='2. termin', marker='x')
plt.title('Porównanie ocen z terminów')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()


# Eksperymentalny wykres
plt.bar(df_oceny['Nr_albumu'], df_oceny['Ocena_1_termin'], color='skyblue', label='1. termin')
plt.bar(df_oceny['Nr_albumu'], df_oceny['Ocena_2_termin'], color='orange', label='2. termin', alpha=0.7)
plt.title('Eksperyment z kolorami i przezroczystością')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.show()

