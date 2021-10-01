import pandas as pd

db = pd.read_excel('../databases/filteredDatabase2.xlsx')

# _____POR REGIÃO GEOGRÁFICA

# ___POR UF

# Comparar número de empréstimos entre UF

numero_de_emprestimos_por_uf = db.groupby(['UF']).size().reset_index(name='Nº de Empréstimos')

# Comparar valores de empréstimos entre UF

valor_operacao_por_uf = db[['UF', 'Valor da Operação em R$']].groupby('UF').sum()

# valor_medio_operacao_por_uf = (valor_operacao_por_uf['Valor da Operação em R$'] / numero)

# valor_desembolsado_por_uf = db[['UF', 'Valor Desembolsado R$ (*)']].groupby('UF').sum()


