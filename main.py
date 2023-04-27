# Passo 1 - Percorrer os arquivis da base de dados (Pasta Vendas)
import os
import pandas as pd
import plotly.express as px

listaArquivo = os.listdir("C:\Estudos\Python Hashtag\Vendas")
#print(listaArquivo)

# Passo 2 - Importar as bases de dados de vendas
tabelaTotal = pd.DataFrame()

for arquivo in listaArquivo:
    if "Vendas" in arquivo:
        # importar o arquivo
        tabela = pd.read_csv(f"C:\Estudos\Python Hashtag\Vendas\{arquivo}")
        tabelaTotal = pd.concat([tabelaTotal, tabela])

# Passo 3 - Tratar / Compilar as bases de dados
#print(tabelaTotal)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabelaProdutos = tabelaTotal.groupby('Produto').sum()
tabelaProdutos = tabelaProdutos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
#print(tabelaProdutos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabelaTotal['Faturamento'] = tabelaTotal["Quantidade Vendida"] * tabelaTotal["Preco Unitario"]
#print(tabelaTotal)
tabelaFaturamento = tabelaTotal.groupby('Produto').sum()
tabelaFaturamento = tabelaFaturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
#print(tabelaFaturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabelaLojas = tabelaTotal.groupby('Loja').sum()
tabelaLojas = tabelaLojas[['Faturamento']] 
print(tabelaLojas)

grafico = px.bar(tabelaLojas,x=tabelaLojas.index,y='Faturamento')
grafico.show()
