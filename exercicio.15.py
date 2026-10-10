import pandas as pd

df = pd.read_csv(r"C:\exercicioaula15\funcionarios - Null.csv")

print (df.head())

# VARIAVEL COM DEPARTAMENTO PREENCHIDO 

df_departamento_preenchido = df.copy()
df_departamento_preenchido['departamento'] = df_departamento_preenchido['departamento'].fillna('Não Informado')
print (df_departamento_preenchido.head())

#VARIAVEL COM LUCRO SEM NULOS

df_lucro_sem_nulos = df.copy()
df_lucro_sem_nulos = df_lucro_sem_nulos.dropna(subset=['lucro'])
print (df_lucro_sem_nulos.head()
    )