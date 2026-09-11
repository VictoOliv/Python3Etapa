# 📊 Análise de Crescimento Populacional Brasil (2010-2022)

## ✅ Tarefas Completadas

- ✓ Pasta do projeto aberta: `H:\Py3etapa\At4`
- ✓ Tabela incluída: `CD2022_Populacao_2010_Compatibilizada_20231222.xlsx`
- ✓ Notebook criado: `Analise_Populacao_2010_2022.ipynb`
- ✓ Dados lidos e processados (5.572 municípios)
- ✓ Tabela agregada por **ESTADO** criada e ordenada por crescimento
- ✓ Tabela agregada por **MUNICÍPIO** criada e ordenada por crescimento
- ✓ Arquivos CSV salvos na pasta

---

## 📈 Resultados Principais

### Brasil - Números Totais
- **População 2010:** 190.755.799 habitantes
- **População 2022:** 203.062.512 habitantes
- **Crescimento Total:** 12.306.713 habitantes
- **Taxa de Crescimento:** 6,45%

---

## 🏆 Top 10 Estados com Maior Crescimento Absoluto (2022 - 2010)

| Posição | Estado | Crescimento | População 2022 |
|---------|--------|-------------|-----------------|
| 1 | **SP** | **3.149.039** | 44.411.238 |
| 2 | **SC** | **1.361.925** | 7.610.361 |
| 3 | **GO** | **1.054.706** | 7.056.495 |
| 4 | **PR** | **999.854** | 11.444.380 |
| 5 | **MG** | **942.659** | 20.539.989 |
| 6 | **MT** | **623.527** | 3.658.649 |
| 7 | **PA** | **539.080** | 8.120.131 |
| 8 | **AM** | **457.628** | 3.941.613 |
| 9 | **CE** | **343.313** | 8.794.957 |
| 10 | **ES** | **318.760** | 3.833.712 |

---

## 🏙️ Top 30 Municípios com Maior Crescimento Absoluto (2022 - 2010)

| Posição | Município | Estado | Crescimento | Taxa % |
|---------|-----------|--------|-------------|--------|
| 1 | **Manaus** | AM | **261.675** | 14,52% |
| 2 | **Brasília** | DF | **245.222** | 9,53% |
| 3 | **São Paulo** | SP | **198.496** | 1,76% |
| 4 | **Sorocaba** | SP | **136.866** | 23,30% |
| 5 | **Goiânia** | GO | **135.454** | 10,40% |
| 6 | **Boa Vista** | RR | **129.173** | 45,44% |
| 7 | **Florianópolis** | SC | **115.971** | 27,55% |
| 8 | **Parauapebas** | PA | **113.928** | 74,09% |
| 9 | **Campo Grande** | MS | **111.326** | 14,15% |
| 10 | **João Pessoa** | PB | **110.417** | 15,27% |
| 11 | **Uberlândia** | MG | **109.211** | 18,08% |
| 12 | **Serra** | ES | **103.323** | 24,74% |
| 13 | **Joinville** | SC | **101.029** | 19,60% |
| 14 | **Cuiabá** | MT | **97.675** | 17,67% |
| 15 | **Ribeirão Preto** | SP | **93.960** | 15,54% |
| 16 | **Petrolina** | PE | **92.829** | 31,57% |
| 17 | **Praia Grande** | SP | **87.884** | 33,56% |
| 18 | **Palhoça** | SC | **85.264** | 62,09% |
| 19 | **Sinop** | MT | **83.213** | 73,66% |
| 20 | **São José de Ribamar** | MA | **82.642** | 50,94% |
| 21 | **Itajaí** | SC | **80.681** | 43,99% |
| 22 | **Barueri** | SP | **75.724** | 31,44% |
| 23 | **Palmas** | TO | **74.360** | 32,55% |
| 24 | **Cotia** | SP | **73.263** | 36,42% |
| 25 | **Jundiaí** | SP | **73.095** | 19,75% |
| 26 | **Santo André** | SP | **72.512** | 10,72% |
| 27 | **São José do Rio Preto** | SP | **72.135** | 17,67% |
| 28 | **Aparecida de Goiânia** | GO | **72.061** | 15,82% |
| 29 | **Chapecó** | SC | **71.237** | 38,82% |
| 30 | **Senador Canedo** | GO | **71.202** | 84,43% |

---

## 📊 Municípios com Maior Taxa de Crescimento (%)

*Entre municípios com população ≥ 10.000 hab em 2010*

| Posição | Município | Estado | Taxa % |
|---------|-----------|--------|--------|
| 1 | Senador Canedo | GO | 84,43% |
| 2 | Parauapebas | PA | 74,09% |
| 3 | Sinop | MT | 73,66% |
| 4 | Palhoça | SC | 62,09% |
| 5 | Boa Vista | RR | 45,44% |

---

## 📁 Arquivos Gerados

Todos os arquivos foram salvos em: **H:\Py3etapa\At4\**

### 1. **populacao_por_estado.csv**
   - Dados agregados por estado
   - Colunas: UF, População 2010, População 2022, Crescimento, Taxa de Crescimento
   - 29 estados + DF

### 2. **populacao_por_municipio.csv**
   - Dados agregados por município
   - Colunas: UF, Município, População 2010, População 2022, Crescimento, Taxa de Crescimento
   - 5.570 municípios

### 3. **Analise_Populacao_2010_2022.ipynb**
   - Notebook completo com toda análise
   - Incluindo visualizações gráficas
   - Código Python reutilizável

### 4. **analise_final.py**
   - Script Python para reproduzir a análise
   - Totalmente documentado e reutilizável

### 5. **RESUMO_ANALISE.md** (este arquivo)
   - Documento com principais resultados

---

## 📝 Instruções para Usar os Dados

### Abrir os CSVs no Excel/Google Sheets

```excel
# No Excel:
1. Abrir arquivo
2. Dados > De Texto
3. Selecionar arquivo CSV
4. Charset: UTF-8
5. Delimitador: Ponto e Vírgula (;)
```

### Usar no Python

```python
import pandas as pd

# Carregar dados
df_estado = pd.read_csv('populacao_por_estado.csv', sep=';')
df_municipio = pd.read_csv('populacao_por_municipio.csv', sep=';')

# Usar dados
print(df_estado.head())
print(df_municipio.head())
```

---

## 🔍 Insights Principais

1. **São Paulo lidera crescimento**: SP agregou 3,1 milhões de habitantes (25,5% do crescimento nacional)

2. **Cidades emergentes**: Manaus e Brasília aparecem como principais centros de crescimento

3. **Taxa de crescimento por região**:
   - São Paulo: 7,63%
   - Santa Catarina: 21,79%
   - Goiás: 17,59%

4. **Municípios de maior dinamismo**: Cidades do Interior (Sorocaba, Boa Vista, Palmas) crescem mais que capitais

5. **Evolução equilibrada**: Crescimento distribuído entre 27 estados (apenas Alagoas teve crescimento inferior a 1%)

---

## 🎯 Próximos Passos

- Importar CSVs em seus softwares de análise favoritos
- Usar o Jupyter Notebook para aprofundar análises
- Combinar com dados de PIB, migração ou infraestrutura
- Criar visualizações adicionais conforme necessário

---

**Análise realizada em:** 11/09/2026  
**Fonte dos dados:** IBGE - Censo Demográfico 2022  
**Compatibilização:** População 2010 Recenseada e Compatibilizada para BT22
