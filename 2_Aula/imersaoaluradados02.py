# -*- coding: utf-8 -*-
"""ImersaoAluraDados02.ipynb

## < IMPORTS >
"""

import pandas as pd

url_dados = "https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true"

dados = pd.read_csv(url_dados, compression="zip")

colunas = dados.columns
for i in range(5,877):
  coluna = colunas[i]
  newColuna = coluna.replace('-','')
  dados = dados.rename(columns={coluna : newColuna})

dados

"""## Imersao Dados 03 - Aula 02"""

mapa = {'droga':'composto'}
dados.rename(columns=mapa, inplace=True)
dados

compostos = dados['composto'].value_counts()
cod_compostos = dados['composto'].value_counts().index[0:5]

dados.query('composto in @cod_compostos')

import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

plt.figure(figsize=(8,6))
ax = sns.countplot(x = 'composto',data=dados.query('composto in @cod_compostos'))
ax.set_title('Top 5 - Compostos')
plt.show()

len(dados['g0'].unique())

dados['g0'].min()

dados['g0'].max()

dados['g0'].hist(bins = 100, range=[-10, 10])
plt.show()

dados['g1'].hist(bins = 100, range=[-10, 10], facecolor='red', align='mid')
plt.show()

dados[{'g0','g1'}]

dados.loc[:,'g0':'g771'].describe()

dados.loc[:,'g0':'g771'].describe().T['mean'].hist(bins=40)

dados.loc[:,'g0':'g771'].describe().T['min'].hist(bins=40)

dados.loc[:,'g0':'g771'].describe().T['max'].hist(bins=40)

dados.loc[:,'c0':'c99'].describe().T['mean'].hist(bins=40, facecolor='red', align='mid')
plt.show()

import seaborn as sns
sns.set_theme()

plt.figure(figsize=(10,7))
sns.boxplot(x='g0', data=dados)

plt.figure(figsize=(10,8))
sns.boxplot(y='g0', x='tratamento',data=dados)

"""##Desafios Aula 02:
###01) Ordenar o grafico countplot  
###02) melhorar o plot alterando fonte,traducao...
###03) plotar com seaborn
###04) estudar os metodos de estatistica
###05) refletir sobre a manipulacao dos tamanhos das visualizacoes
###06) novos boxplots para realizar comparativos
###07) resumo do que voce aprendeu com os dados
"""

poker = dados.query('composto in @cod_compostos')
poker

poker = dados.query('composto in @cod_compostos')
plt.figure(figsize=(8,6))
ax = sns.countplot(x = 'composto',
                   data=poker,
                   facecolor=(0, 0, 0, 0),
                   linewidth=2,
                   edgecolor=sns.color_palette("dark", 3),
                   order = poker['composto'].value_counts().index
                   )
ax.set_title('Top 5 - Compostos')
plt.show()