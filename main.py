import pandas as pd
import numpy as np

df_vendas= pd.read_csv("vendas_tech.csv", low_memory=False)

#df_vendas= pd.read_csv("vendas_tech.csv", sep=",") definir o caractere separador
#df_vendas= pd.read_csv("vendas_tech.csv", encoding="latin1 ou utf-8") para evitar nao localizar caracteres

print(df_vendas)

df_gerentes = pd.read_excel("gerentes_lojas.xlsx")

print(df_gerentes)
