import pandas as pd

db = pd.read_excel('../../databases/queried/filteredDatabase2.xlsx')

valor_operacao_por_uf = db[['UF', 'Valor da Operação em R$']].groupby('UF').sum()

with pd.ExcelWriter('../../databases/queried/byUF/emprestimos_por_uf.xlsx', mode='a', engine='openpyxl') as writer:
    valor_operacao_por_uf.to_excel(writer, sheet_name='valor_operacao_por_uf')

# valor_medio_operacao_por_uf = (valor_operacao_por_uf['Valor da Operação em R$'] / numero)