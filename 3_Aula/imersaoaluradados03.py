# -*- coding: utf-8 -*-
"""ImersaoAluraDados03.ipynb

Automatically generated by Colaboratory.

#< IMPORTS >
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

url_dados = "https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true"

dados = pd.read_csv(url_dados, compression="zip")

colunas = dados.columns
for i in range(5,877):
  coluna = colunas[i]
  newColuna = coluna.replace('-','')
  dados = dados.rename(columns={coluna : newColuna})

mapa = {'droga':'composto'}
dados.rename(columns=mapa, inplace=True)

dados

"""# Alguns Testes:

"""

dados_controle = dados[dados['tratamento'] == 'com_controle']
dados_droga = dados[dados['tratamento'] == 'com_droga']

dados_controle_D1 = dados_controle[dados_controle['dose'] == 'D1']
dados_controle_D2 = dados_controle[dados_controle['dose'] == 'D2']
dados_droga_D1 = dados_droga[dados_droga['dose'] == 'D1']
dados_droga_D2 = dados_droga[dados_droga['dose'] == 'D2']

cod_dados_controle = dados_controle['composto'].value_counts().index[0:5]
top_dados_controle = dados_controle.query('composto in @cod_dados_controle')

cod_dados_droga = dados_droga['composto'].value_counts().index[0:100]
top_dados_droga = dados_droga.query('composto in @cod_dados_droga')

cod_dados_controle

top_dados_controle

cod_dados_droga

top_dados_droga

dados_controle['composto'].unique()

plot1 = sns.catplot(x='composto',data=top_dados_controle,col="dose",kind="count",col_wrap=2 ,height=4, aspect=.7)

plot2 = sns.catplot(x='composto',data=top_dados_droga,col="dose",kind="count",height=7, aspect=.8)

"""#### - achar o composto em 'cacb2b860' dados droga"""

findArray = dados_droga['composto'].unique()

exist = 'cacb2b860' in findArray
exist

"""#### - Posso concluir que o controle so foi realizado no composto 'cacb2b860'

##Separando compostos
"""

compUni = dados['composto'].unique()
arComps = []
for comp in compUni:
  temp = dados[dados['composto'] == comp]
  arComps.append(temp)

arComps[0]

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='mean')

"""##ser???"""

bla = pd.crosstab(dados_droga['tempo'], dados_droga['dose'], values=dados_droga['g0'], aggfunc='mean')
blo = pd.crosstab(dados_controle['tempo'], dados_controle['dose'], values=dados_controle['g0'], aggfunc='mean')

bla

blo

"""# Aula 03:"""

pd.crosstab(dados['dose'], dados['tempo'])

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'])

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize=True)

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='index')

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='mean')

dados[['g0', 'g3']]

sns.scatterplot(x='g0',y='g3',data=dados)

sns.scatterplot(x='g0',y='g8',data=dados)

sns.lmplot(x='g1',y='g8',data=dados ,line_kws={'color': 'red'})

sns.lmplot(x='g0',y='g8',data=dados ,line_kws={'color': 'red'})

sns.lmplot(x='g0',y='g8',data=dados ,line_kws={'color': 'red'}, col='tratamento', row='tempo')

# Correlacoes
## 1 = corr alta , 0 = corr baixa
## += proporcional , -= inversamente proporcional
dados.loc[:,'g0':'g771'].corr()

# Compute the correlation matrix
corr = dados.loc[:,'g0':'g50'].corr()

# import lib numpy
import numpy as np

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

corr_cell = dados.loc[:,'c0':'c50'].corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr_cell, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_cell, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

"""#Desafio Aula 3:
##Desafio 01) Criar tabelas de frequencia com o pandas.groupby()
##Desafio 02) Normalizar crosstab pela coluna
##Desafio 03) Explorar outros agregadores
##Desafio 04) Explorar o melt
##Desafio 05) Analizar correlacao de G e C, refletir sobre os efeitos biologicos
##Desafio 06) Estudar o codigo de plot do heatmap
"""