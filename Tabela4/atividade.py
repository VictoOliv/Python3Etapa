import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Tabela4.csv", sep=";", decimal=",", skiprows=1, encoding="latin-1")
df = df.dropna(axis=1, how="all")

print(df.sort_values("2024", ascending=False)[["Estado", "2024"]])

delta = df["2024"] - df["1991"]
print(df.loc[delta.idxmax(), "Estado"], delta.max())

print(df[df["2024"] < df["1991"]][["Estado", "1991", "2024"]])

anos = [c for c in df.columns if str(c).isdigit()]
print(anos)

id_vars = [c for c in df.columns if c not in anos]
df_longo = df.melt(
    id_vars=id_vars,
    value_vars=anos,
    var_name="Ano",
    value_name="IDH",
)
df_longo["Ano"] = df_longo["Ano"].astype(int)
df_longo["IDH"] = pd.to_numeric(df_longo["IDH"], errors="coerce")
print(df_longo.head())

mg = df_longo[df_longo["Estado"] == "Minas Gerais"].sort_values("Ano")
fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(mg["Ano"], mg["IDH"], marker="o", markersize=3, linewidth=1.5, label="MG")
ax.set_title("Evolucao do IDH - Minas Gerais (1991-2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)
ax.legend()
fig.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 7))

for sigla, grupo in df_longo.groupby("Sigla"):
    grupo = grupo.sort_values("Ano")
    ax.plot(grupo["Ano"], grupo["IDH"], marker="o", markersize=3, linewidth=1.5, label=sigla)

ax.set_title("Evolucao do IDH por estado (1991-2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)
ax.legend(ncol=3, bbox_to_anchor=(1.02, 1), loc="upper left", title="UF")
fig.tight_layout()
plt.show()
