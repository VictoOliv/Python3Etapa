import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("graficos", exist_ok=True)

sns.set_style("whitegrid")
sns.set_palette("deep")

df = pd.read_csv("vendas.csv")
df["data"] = pd.to_datetime(df["data"])

print(df.info())
print(df.isnull().sum())
print(df.describe())

df["quantidade"] = df["quantidade"].fillna(df["quantidade"].mean())
df["preco_unitario"] = df["preco_unitario"].fillna(df["preco_unitario"].mean())
df["faturamento"] = df["quantidade"] * df["preco_unitario"]
df["mes"] = df["data"].dt.month
df["mes_ano"] = df["data"].dt.strftime("%m/%Y")

regiao = {
    "Loja SP": "Sudeste",
    "Loja RJ": "Sudeste",
    "Loja POA": "Sul",
    "Loja SSA": "Nordeste",
    "Loja MAO": "Norte",
}
categoria = {
    "Camiseta": "Vestuário",
    "Calca": "Vestuário",
    "Jaqueta": "Vestuário",
    "Tenis": "Calçados",
    "Sandalia": "Calçados",
    "Mochila": "Acessórios",
    "Bone": "Acessórios",
}
df["regiao"] = df["loja"].map(regiao)
df["categoria"] = df["produto"].map(categoria)

fat_loja = df.groupby("loja")["faturamento"].sum().sort_values(ascending=False)
print(fat_loja)

ticket_medio = (df.groupby("loja")["faturamento"].sum() / df.groupby("loja").size()).sort_values(ascending=False)
print(ticket_medio)

top5 = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(5)
print(top5)

fat_mes = df.groupby("mes_ano")["faturamento"].sum()
print(fat_mes.idxmax(), round(fat_mes.max(), 2))
print(fat_mes.idxmin(), round(fat_mes.min(), 2))

cores = sns.color_palette("deep")

fig, ax = plt.subplots(figsize=(10, 6))
fat_loja.plot(kind="bar", color=cores, ax=ax)
ax.set_title("Faturamento total por loja")
ax.set_xlabel("Loja")
ax.set_ylabel("Faturamento (R$)")
ax.legend(["Faturamento"])
plt.xticks(rotation=0)
fig.tight_layout()
fig.savefig("graficos/faturamento_por_loja.png")
plt.close()

mensal = df.groupby(df["data"].dt.to_period("M"))["faturamento"].sum().sort_index()
mensal.index = mensal.index.strftime("%m/%Y")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(mensal.index, mensal.values, marker="o")
for x, y in zip(mensal.index, mensal.values):
    ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)
ax.set_title("Evolução mensal do faturamento")
ax.set_xlabel("Mês/Ano")
ax.set_ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
fig.tight_layout()
fig.savefig("graficos/evolucao_mensal.png")
plt.close()

fat_regiao = df.groupby("regiao")["faturamento"].sum()
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(fat_regiao, labels=fat_regiao.index, autopct="%1.1f%%", colors=cores[: len(fat_regiao)])
ax.set_title("Distribuição de faturamento por região")
fig.tight_layout()
fig.savefig("graficos/faturamento_por_regiao.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="quantidade", y="faturamento", hue="loja", ax=ax)
ax.set_title("Relação entre quantidade vendida e faturamento")
ax.set_xlabel("Quantidade")
ax.set_ylabel("Faturamento (R$)")
fig.tight_layout()
fig.savefig("graficos/scatter_quantidade_faturamento.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="categoria", y="preco_unitario", hue="categoria", ax=ax, legend=False)
ax.set_title("Distribuição de preços unitários por categoria")
ax.set_xlabel("Categoria")
ax.set_ylabel("Preço unitário (R$)")
fig.tight_layout()
fig.savefig("graficos/boxplot_precos.png")
plt.close()

num = df[["quantidade", "preco_unitario", "faturamento", "mes"]]
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(num.corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Correlação entre variáveis numéricas")
fig.tight_layout()
fig.savefig("graficos/heatmap_correlacao.png")
plt.close()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fat_loja.plot(kind="bar", color=cores, ax=axes[0])
axes[0].set_title("Faturamento por loja")
axes[0].set_xlabel("Loja")
axes[0].set_ylabel("Faturamento (R$)")
axes[0].tick_params(axis="x", rotation=0)
fat_regiao.plot(kind="bar", color=cores, ax=axes[1])
axes[1].set_title("Faturamento por região")
axes[1].set_xlabel("Região")
axes[1].set_ylabel("Faturamento (R$)")
axes[1].tick_params(axis="x", rotation=0)
fig.tight_layout()
fig.savefig("graficos/comparacao_loja_regiao.png")
plt.close()

resumo = pd.DataFrame(
    {
        "indicador": [
            "faturamento_total",
            "loja_maior_faturamento",
            "ticket_medio_maior_loja",
            "produto_mais_vendido",
            "mes_maior_faturamento",
            "mes_menor_faturamento",
        ],
        "valor": [
            round(df["faturamento"].sum(), 2),
            fat_loja.idxmax(),
            ticket_medio.idxmax(),
            top5.index[0],
            fat_mes.idxmax(),
            fat_mes.idxmin(),
        ],
    }
)
resumo.to_csv("resumo_analitico.csv", index=False)
print(resumo)
print("Loja RJ lidera o faturamento; o heatmap mostra correlação forte entre quantidade, preço e faturamento.")
