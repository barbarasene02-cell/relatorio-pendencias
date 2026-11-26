import pandas as pd

# 1 e 2. Cria o DataFrame com Nome, CPF e Status (CPFs fictícios)
dados = {
    "Nome": ["Ana Souza", "Carlos Lima", "Marina Alves", "João Pereira"],
    "CPF": ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44"],
    "Status": ["Regular", "Pendente", "Regular", "Pendente"],
}
df = pd.DataFrame(dados)

# 3. Filtra apenas os funcionários com status "Pendente"
pendentes = df[df["Status"] == "Pendente"]

# 4. Salva o resultado em um arquivo Excel
pendentes.to_excel("relatorio_pendencias.xlsx", index=False)

print(pendentes)
