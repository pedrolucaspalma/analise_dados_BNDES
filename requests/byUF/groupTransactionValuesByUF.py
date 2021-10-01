import pandas as pd

db = pd.read_excel('../databases/queried/filteredDatabase2.xlsx')

# Comparar número de empréstimos entre UF

numero_de_emprestimos_por_uf = db.groupby(['UF']).size().reset_index(name='Nº de Empréstimos')

with pd.ExcelWriter('../databases/queried/byUF/emprestimos_por_regiao.xlsx') as writer:
    numero_de_emprestimos_por_uf.to_excel(writer, sheet_name='numero_de_emprestimos_por_uf')