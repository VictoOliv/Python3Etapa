import pandas as pd

arquivo = r'H:\Py3etapa\At4\CD2022_Populacao_2010_Compatibilizada_20231222.xlsx'

df = pd.read_excel(arquivo, header=None)
print("Formato bruto:")
print(df.head(20))
print("\nShape:", df.shape)

for idx, row in df.iterrows():
    if any('UF' in str(val) for val in row):
        print(f"\nLinha {idx} contém 'UF':")
        print(row)
        break
