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

    # SALVAR EM EXCEL
df.to_excel("funcionarios_original.xlsx", index=False)
df_departamento_preenchido.to_excel("funcionarios_departamento_preenchido.xlsx", index=False)
df_lucro_sem_nulos.to_excel("funcionarios_lucro_sem_nulos.xlsx", index=False)

print("\nArquivos Excel criados com sucesso!")