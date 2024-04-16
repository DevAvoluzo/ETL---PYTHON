# -*- coding: utf-8 -*-
"""EXEMPLO_ETL

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HvoziUU8KsTQ-c-JJ9ygnAjvtbBRz0Uz
"""

import pandas as pd
import sqlite3

# Extração dos dados da filial 1 (CSV)
vendas_filial1 = pd.read_csv('ETL_csv.csv')

# Extração dos dados da filial 2 (EXCEL)
vendas_filial2 = pd.read_excel('ETL_xlsx.xlsx')

#Visualizar
print("Dados da Filial 1:")
print(vendas_filial1.head())
print("Dados da Filial 2:")
print(vendas_filial2.head())

# Transformação dos dados: Calcular o valor total de vendas para cada filial
vendas_filial1['Valor Total'] = vendas_filial1['Quantidade Vendida'] * vendas_filial1['Preço Unitário']
vendas_filial2['Valor Total'] = vendas_filial2['Quantidade Vendida'] * vendas_filial2['Preço Unitário']

# Visualizar os dados transformados
print("Dados transformados da Filial 1:")
print(vendas_filial1.head())
print("Dados transformados da Filial 2:")
print(vendas_filial2.head())


# Conectar ao banco de dados SQLite
conn = sqlite3.connect("banco_de_dados.db")

# Importar dados do DataFrame vendas_filial1 para a tabela SQLite "vendas_filial1_csv"
vendas_filial1.to_sql('vendas_filial1_csv', conn, if_exists='replace', index=False)

# Importar dados do DataFrame vendas_filial2 para a tabela SQLite "vendas_filial2_xlsx"
vendas_filial2.to_sql('vendas_filial2_xlsx', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados SQLite
conn.close()