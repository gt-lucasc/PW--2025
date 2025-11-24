alunos = {
    "Nome": "Lucas",
    "Idade": 20,
    "Curso": "Programador Web",
    "Local": "Senac"
}

print("Informações do aluno")
for chave, valor in alunos.items():
    print(f"{chave}: {valor}")