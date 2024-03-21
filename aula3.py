##Análise de Dados

import pandas as pd
import plotly-express as px

dados = pd.read_excel("vendas.xlsx")

dados.head()# vai abrir as 5 primeiras linhas da tabela
dados.tail()# vai abrir as 5 últimas linhas da tabela
dados.info()# mostra o tipo dos dados na tabela (EX: int,str, ...)

dados.preço.describe().to_frame()# vai abrir uma tabela com algums infos, media, desvio, max, min ...

dados.loja.value_counts().to_frame()# descobrir quantas lojas tem, e quantas vendas ela fez
dados.cidade.value_counts().to_frame()# descobrir cidades lojas tem, e quantas vendas ela fez 
dados.forma_de_pagamento.value_counts().to_frame()# descobrir quanto cada dorma de pagamento esta sendo usada

dados.groupby("loja").preço.sum().to_frame()# forma uam tabela de faturamneto das lojas
dados.groupby(["estado","cidade"]).preço.sum().to_excel()# forma uma planilha automaticamente

colunas = ["loja","colunas","estado","regiao","local_consumo"]# array
for coluna in colunas:#estrutura de repetição
    grafico = px.histogram (dados, 
             x="coluna",
             y="preco", 
             text_auto=True, 
             title= "Faturamento por loja"
             color= "forma_pagamento")# faz um gráfico interativo

    grafico.show()# vai aparecer o gráfico feito
    grafico.write_html(f"gráfico-{coluna}.html")# cria uma arquivo html com o gráfico


















