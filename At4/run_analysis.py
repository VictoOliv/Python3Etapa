import pandas as pd
import os

arquivo = r'H:\Py3etapa\At4\CD2022_Populacao_2010_Compatibilizada_20231222.xlsx'

print("Carregando dados...")
df = pd.read_excel(arquivo)

print(f"✓ Dados carregados: {df.shape[0]} linhas x {df.shape[1]} colunas")
print("\n" + "="*80)
print("ESTRUTURA DOS DADOS")
print("="*80)
print("\nColunas:")
print(df.columns.tolist())
print("\nPrimeiras linhas:")
print(df.head(10))
print("\nTipos de dados:")
print(df.dtypes)
print("\nEstatísticas descritivas:")
print(df.describe())

colunas_numericas = df.select_dtypes(include=['number']).columns.tolist()
colunas_texto = df.select_dtypes(include=['object']).columns.tolist()

print(f"\nColunas numéricas: {colunas_numericas}")
print(f"Colunas de texto: {colunas_texto}")

col_2010 = [col for col in df.columns if '2010' in str(col).lower()]
col_2022 = [col for col in df.columns if '2022' in str(col).lower()]

print(f"\nColunas com 2010: {col_2010}")
print(f"Colunas com 2022: {col_2022}")

print("\n" + "="*80)
print("VALORES ÚNICOS - COLUNAS DE TEXTO")
print("="*80)
for col in colunas_texto:
    print(f"\n{col}: {df[col].nunique()} valores únicos")
    print(f"  Exemplos: {df[col].unique()[:10]}")
