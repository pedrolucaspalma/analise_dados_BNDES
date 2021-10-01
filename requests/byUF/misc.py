import pandas as pd

valores_de_operacao = pd.read_excel('../../databases/queried/byUF/emprestimos_por_regiao.xlsx',sheet_name='valor_operacao_por_uf')
quantidade_de_operacoes = pd.read_excel('../../databases/queried/byUF/emprestimos_por_regiao.xlsx',sheet_name='numero_de_emprestimos_por_uf')

with pd.ExcelWriter('../../databases/queried/byUF/emprestimos_por_regiao_dataFrame.xlsx') as writer:
    quantidade_de_operacoes.to_excel(writer, sheet_name='numero_de_emprestimos_por_uf')

with pd.ExcelWriter('../../databases/queried/byUF/emprestimos_por_regiao_dataFrame.xlsx', mode="a", engine="openpyxl") as writer:
    valores_de_operacao.to_excel(writer, sheet_name='valor_de_emprestimos_por_uf')

