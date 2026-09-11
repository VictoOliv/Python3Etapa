import pandas as pd
import os

arquivo = r'H:\Py3etapa\At4\CD2022_Populacao_2010_Compatibilizada_20231222.xlsx'
diretorio = r'H:\Py3etapa\At4'

print("Carregando dados...")
df = pd.read_excel(arquivo, header=2)

df = df.dropna(subset=['UF'], how='all')
df = df[df['UF'].notna()].copy()
df = df[df['UF'] != 'UF'].copy()

print(f"✓ Dados carregados: {len(df)} linhas")
print("\nColunas originais:")
print(df.columns.tolist())

df.columns = [col.strip() if isinstance(col, str) else col for col in df.columns]

colunas = df.columns.tolist()
print(f"Colunas encontradas: {colunas}")

pop_2010 = None
pop_2010_alt = None
pop_2022 = None

for col in colunas:
    if isinstance(col, str):
        if '2010' in col and 'Sinopse' in col:
            pop_2010 = col
        elif '2010' in col and 'Alterações' in col:
            pop_2010_alt = col
        elif '2022' in col:
            pop_2022 = col

print(f"\nColunas identificadas:")
print(f"  Pop 2010 (Sinopse): {pop_2010}")
print(f"  Pop 2010 (Alterações): {pop_2010_alt}")
print(f"  Pop 2022: {pop_2022}")

if pop_2010:
    df[pop_2010] = pd.to_numeric(df[pop_2010], errors='coerce')
if pop_2010_alt:
    df[pop_2010_alt] = pd.to_numeric(df[pop_2010_alt], errors='coerce')
if pop_2022:
    df[pop_2022] = pd.to_numeric(df[pop_2022], errors='coerce')

print("\nPrimeiras linhas dos dados limpos:")
print(df.head(10))

print("\n" + "="*80)
print("1. AGREGAÇÃO POR ESTADO")
print("="*80)

cols_agg = {}
if pop_2010:
    cols_agg[pop_2010] = 'sum'
if pop_2010_alt:
    cols_agg[pop_2010_alt] = 'sum'
if pop_2022:
    cols_agg[pop_2022] = 'sum'

df_estado = df.groupby('UF').agg(cols_agg).reset_index()

col_pop_2010_usar = pop_2010_alt if pop_2010_alt else pop_2010
df_estado['CRESCIMENTO_2022_2010'] = df_estado[pop_2022] - df_estado[col_pop_2010_usar]

df_estado = df_estado.sort_values('CRESCIMENTO_2022_2010', ascending=False).reset_index(drop=True)

print("\nEstados ordenados por crescimento populacional (2022 - 2010):")
print(df_estado.to_string())

arquivo_estado = os.path.join(diretorio, 'populacao_por_estado.csv')
df_estado.to_csv(arquivo_estado, sep=';', index=False, encoding='utf-8')
print(f"\n✓ Arquivo salvo: populacao_por_estado.csv")

print("\n" + "="*80)
print("2. AGREGAÇÃO POR MUNICÍPIO")
print("="*80)

df_municipio = df.groupby(['UF', 'NOME DO MUNICÍPIO']).agg(cols_agg).reset_index()

df_municipio['CRESCIMENTO_2022_2010'] = df_municipio[pop_2022] - df_municipio[col_pop_2010_usar]

df_municipio = df_municipio.sort_values('CRESCIMENTO_2022_2010', ascending=False).reset_index(drop=True)

print(f"\nTotal de municípios: {len(df_municipio)}")
print("\nTop 30 municípios com maior crescimento:")
print(df_municipio.head(30).to_string())

arquivo_municipio = os.path.join(diretorio, 'populacao_por_municipio.csv')
df_municipio.to_csv(arquivo_municipio, sep=';', index=False, encoding='utf-8')
print(f"\n✓ Arquivo salvo: populacao_por_municipio.csv")

print("\n" + "="*80)
print("RESUMO FINAL")
print("="*80)
print(f"✓ Dados originais processados: {len(df)} linhas")
print(f"✓ Estados únicos: {df_estado.shape[0]}")
print(f"✓ Municípios únicos: {df_municipio.shape[0]}")
print(f"\n✓ Arquivos gerados na pasta H:\\Py3etapa\\At4\\")
print(f"  1. populacao_por_estado.csv")
print(f"  2. populacao_por_municipio.csv")
print("="*80)
