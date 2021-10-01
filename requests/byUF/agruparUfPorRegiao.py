import pandas as pd

db = pd.read_excel('../../databases/queried/byUF/emprestimos_por_regiao.xlsx', sheet_name='operacoes_por_uf')

valores_sudeste = db.loc[(db['UF'] == ' RJ') |
                       (db['UF'] == ' SP') |
                       (db['UF'] == ' MG') |
                       (db['UF'] == ' ES')
]

valores_centro_oeste = db.loc[(db['UF'] == ' MT') |
                       (db['UF'] == ' GO') |
                       (db['UF'] == ' MS') |
                       (db['UF'] == ' DF')
]

valores_sul = db.loc[(db['UF'] == ' RS') |
                       (db['UF'] == ' PR') |
                       (db['UF'] == ' SC')
]

valores_nordeste = db.loc[(db['UF'] == ' MA') |
                       (db['UF'] == ' PI') |
                       (db['UF'] == ' RN') |
                       (db['UF'] == ' PB') |
                       (db['UF'] == ' PE') |
                       (db['UF'] == ' BA') |
                       (db['UF'] == ' CE') |
                       (db['UF'] == ' AL') |
                       (db['UF'] == ' SE')
]

valores_norte = db.loc[(db['UF'] == ' TO') |
                       (db['UF'] == ' AP') |
                       (db['UF'] == ' PA') |
                       (db['UF'] == ' RR') |
                       (db['UF'] == ' AM') |
                       (db['UF'] == ' AC') |
                       (db['UF'] == ' RO')
]
valores_regiões_tabela = {'Região': ['Sul', 'Sudeste', 'Centro-Oeste', 'Norte', 'Nordeste'],
                          'Valor Total de Operações': [0,0,0,0,0],
                          'Total de Operações': [0,0,0,0,0]}

valores_regiões_df = pd.DataFrame(valores_regiões_tabela)

# sul
valores_regiões_df.loc[0, 'Valor Total de Operações'] = valores_sul['Valor da Operação em R$'].sum()
valores_regiões_df.loc[0, 'Total de Operações'] = valores_sul['Numero de operações'].sum()

#Sudeste
valores_regiões_df.loc[1, 'Valor Total de Operações'] = valores_sudeste['Valor da Operação em R$'].sum()
valores_regiões_df.loc[1, 'Total de Operações'] = valores_sudeste['Numero de operações'].sum()

#Centro-Oeste
valores_regiões_df.loc[2, 'Valor Total de Operações'] = valores_centro_oeste['Valor da Operação em R$'].sum()
valores_regiões_df.loc[2, 'Total de Operações'] = valores_centro_oeste['Numero de operações'].sum()

#Norte
valores_regiões_df.loc[3, 'Valor Total de Operações'] = valores_norte['Valor da Operação em R$'].sum()
valores_regiões_df.loc[3, 'Total de Operações'] = valores_norte['Numero de operações'].sum()

#Nordeste
valores_regiões_df.loc[4, 'Valor Total de Operações'] = valores_nordeste['Valor da Operação em R$'].sum()
valores_regiões_df.loc[4, 'Total de Operações'] = valores_nordeste['Numero de operações'].sum()

valores_regiões_df['Valor Médio de Operação'] = valores_regiões_df['Valor Total de Operações'] / valores_regiões_df['Total de Operações']

with pd.ExcelWriter('../../databases/queried/byUF/emprestimos_por_regiao.xlsx', mode='a', engine='openpyxl') as writer:
    valores_regiões_df.to_excel(writer, sheet_name='operacoes_por_regiao')

