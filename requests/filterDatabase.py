import pandas as pd

tabela_geral = pd.read_excel('../database.xlsx')

tabela_geral['Data da contratação'] = pd.to_datetime(tabela_geral['Data da contratação'], dayfirst=True)

tabela_filtrada = tabela_geral.loc[ (tabela_geral['Instrumento Financeiro'] == 'LINHA EMPRÉSTIMO PARA MICRO E PEQUENAS EMPRESAS') & (tabela_geral['Data da contratação'] > '2020/01/01') & (tabela_geral['Data da contratação'] < '2021/01/01')]

tabela_filtrada.to_excel("filteredDatabase.xlsx")