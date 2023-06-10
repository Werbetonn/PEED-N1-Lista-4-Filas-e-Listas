def encontrar_aluno_maior_nota(lista_alunos):
    maior_nota = float("-inf")
    nome_aluno_maior_nota = ""

    for aluno in lista_alunos:
        nota = aluno["nota"]
        if nota > maior_nota:
            maior_nota = nota
            nome_aluno_maior_nota = aluno["nome"]

    return nome_aluno_maior_nota

# Lista de alunos
alunos = [
    {"nome": "Larissa", "nota": 8.9},
    {"nome": "Laiz", "nota": 7.8},
    {"nome": "Lohanny", "nota": 7.2},
    {"nome": "Roberto", "nota": 9.7}
]

resultado = encontrar_aluno_maior_nota(alunos)

print("Aluno com maior nota:", resultado)