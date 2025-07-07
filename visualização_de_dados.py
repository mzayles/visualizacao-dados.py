import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando base de dados pública
df = sns.load_dataset('iris')

df.shape
df.info()
df['species'].unique()

# Gráfico de Linha: Largura da pétala
plt.figure(figsize=(15, 5))
plt.plot(df.index, df['petal_width'], color='skyblue')
plt.title('Largura da Pétala por Índice')
plt.xlabel('Índice')
plt.ylabel('Largura (cm)')
plt.legend(['Largura da Pétala'])
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Gráfico de Linha: Comprimento vs Largura
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['petal_length'], color='skyblue', label='Comprimento')
plt.plot(df.index, df['petal_width'], color='pink', linewidth=1.8, linestyle='--', label='Largura')
plt.title('Comprimento e Largura da Pétala')
plt.xlabel('Índice')
plt.ylabel('Medidas (cm)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Gráfico de Barras: Quantidade por espécie
plt.figure(figsize=(8, 6))
sns.countplot(data=df, y='species', color='lightgreen')
plt.title('Quantidade de Espécies')
plt.xlabel('Contagem')
plt.ylabel('Espécie')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Gráfico de Barras: Largura da pétala por espécie
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='petal_width', y='species', ci=None, palette='pastel')
plt.title('Média da Largura da Pétala por Espécie')
plt.xlabel('Largura da Pétala (cm)')
plt.ylabel('Espécie')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Gráfico de Pizza: Distribuição das espécies
df_contagem = df['species'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(df_contagem, labels=df_contagem.index, explode=[0.1, 0, 0], autopct='%1.1f%%', colors=['#FBB4AE', '#B3CDE3', '#CCEBC5'])
plt.title('Distribuição das Espécies (Pie Chart)')
plt.tight_layout()
plt.show()

# Gráfico de Dispersão: Largura x Comprimento da pétala
plt.figure(figsize=(8, 6))
plt.scatter(df['petal_length'], df['petal_width'], color='skyblue', alpha=0.7)
plt.title('Dispersão: Comprimento vs Largura da Pétala')
plt.xlabel('Comprimento (cm)')
plt.ylabel('Largura (cm)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()