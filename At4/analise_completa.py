import pandas as pd
import os

arquivo = r'H:\Py3etapa\At4\CD2022_Populacao_2010_Compatibilizada_20231222.xlsx'
diretorio = r'H:\Py3etapa\At4'

print("Carregando dados...")
df = pd.read_excel(arquivo, header=1)

df = df.dropna(how='all', axis=1)
df = df[df['UF'].notna()]

print(f"✓ Dados carregados: {len(df)} linhas")
print("\nColunas:")
print(df.columns.tolist())
print("\nPrimeiras linhas:")
print(df.head(10))

df.columns = ['VAZIO1', 'UF', 'COD_UF', 'COD_MUNIC', 'NOME_MUNICIPIO', 'POP_2010', 'POP_2010_ALT', 'POP_2022']
df = df.drop('VAZIO1', axis=1)

df['POP_2010'] = pd.to_numeric(df['POP_2010'], errors='coerce')
df['POP_2010_ALT'] = pd.to_numeric(df['POP_2010_ALT'], errors='coerce')
df['POP_2022'] = pd.to_numeric(df['POP_2022'], errors='coerce')

df = df[df['UF'] != 'UF'].copy()

print("\n" + "="*80)
print("1. AGREGAÇÃO POR ESTADO")
print("="*80)

df_estado = df.groupby('UF').agg({
    'POP_2010': 'sum',
    'POP_2010_ALT': 'sum',
    'POP_2022': 'sum'
}).reset_index()

df_estado['CRESCIMENTO_2010_2022'] = df_estado['POP_2022'] - df_estado['POP_2010_ALT']

df_estado = df_estado.sort_values('CRESCIMENTO_2010_2022', ascending=False).reset_index(drop=True)

print("\nEstados ordenados por crescimento populacional:")
print(df_estado.to_string())

arquivo_estado = os.path.join(diretorio, 'populacao_por_estado.csv')
df_estado.to_csv(arquivo_estado, sep=';', index=False, encoding='utf-8')
print(f"\n✓ Arquivo salvo: {arquivo_estado}")

print("\n" + "="*80)
print("2. AGREGAÇÃO POR MUNICÍPIO")
print("="*80)

df_municipio = df.groupby(['UF', 'NOME_MUNICIPIO']).agg({
    'POP_2010': 'sum',
    'POP_2010_ALT': 'sum',
    'POP_2022': 'sum'
}).reset_index()

df_municipio['CRESCIMENTO_2010_2022'] = df_municipio['POP_2022'] - df_municipio['POP_2010_ALT']

df_municipio = df_municipio.sort_values('CRESCIMENTO_2010_2022', ascending=False).reset_index(drop=True)

print(f"\nTotal de municípios: {len(df_municipio)}")
print("\nTop 20 municípios com maior crescimento:")
print(df_municipio.head(20).to_string())

arquivo_municipio = os.path.join(diretorio, 'populacao_por_municipio.csv')
df_municipio.to_csv(arquivo_municipio, sep=';', index=False, encoding='utf-8')
print(f"\n✓ Arquivo salvo: {arquivo_municipio}")

print("\n" + "="*80)
print("RESUMO FINAL")
print("="*80)
print(f"✓ Dados originais: {len(df)} linhas")
print(f"✓ Estados únicos: {df_estado.shape[0]}")
print(f"✓ Municípios únicos: {df_municipio.shape[0]}")
print(f"\n✓ Arquivos gerados:")
print(f"  1. populacao_por_estado.csv")
print(f"  2. populacao_por_municipio.csv")
print(f"\nLocalização: {diretorio}")
