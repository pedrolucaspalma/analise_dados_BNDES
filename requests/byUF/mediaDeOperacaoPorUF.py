import pandas as pd

db = pd.read_excel('../../databases/queried/byUF/emprestimos_por_regiao.xlsx',sheet_name='operacoes_por_uf')

valores_de_operacoes = db['Valor da Operação em R$']
numero_de_operacoes = db['Numero de operações']

db['Valor Médio de Operação'] = valores_de_operacoes/numero_de_operacoes

with pd.ExcelWriter('../../databases/queried/byUF/emprestimos_por_regiao.xlsx', mode='a', engine='openpyxl') as writer:
    db.to_excel(writer, sheet_name='operacoes_por_uf2')