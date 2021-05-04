# -*- coding: utf-8 -*-

import pandas as pd

url_dados = "https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true"

dados = pd.read_csv(url_dados, compression="zip")

dados

dados.head()

dados["id"]

dados["tratamento"].unique()

dados["dose"].unique()

dados['g-0'].unique()

dados["tempo"].unique()

dados["droga"].unique()

dados['tratamento'].value_counts()

dados['dose'].value_counts()

pr = 21948/1866

pr

dados['tratamento'].value_counts(normalize = True)

dados['dose'].value_counts(normalize = True)

dados['tratamento'].value_counts().plot.pie()

dados['tempo'].value_counts().plot.pie()

dados['tempo'].value_counts().plot.bar()

dados[dados['g-0'] > 0]



"""#01) porque a diferenca nas quantidades de tratamento ?
#02) plotar ultimos 5 numeros da tabela
#03) proporcao das classes tratamento
#04) quantos tipos de drogas foram investigados ?
#05) procurar na documentacao(pandas) o metodo query 
#06) renomear as colunas e retirar os hifens
#07) deixar os graficos bonitos (matplotlib.pyplot)
#08) resumo do que você aprendeu com os dados

02:
"""

dados.tail()

"""03:"""

Trat = dados['tratamento'].value_counts()
propsTrat = (Trat/Trat.sum())*100
propsTrat

"""04:"""

Dorogas = dados["droga"].unique()

Dorogas.size

"""05:

"""

queryTest = dados.head()
queryTest.query('tempo > 24')

"""06:"""

colunas = dados.columns
for i in range(5,877):
  coluna = colunas[i]
  newColuna = coluna.replace('-','')
  dados = dados.rename(columns={coluna : newColuna})

dados

"""##-- Desafios concluidos --"""