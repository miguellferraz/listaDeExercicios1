turma = ("André", "Fernanda", "Luiz")

pesquisa = input("Digite um nome: ")
x = False
for i in range(len(turma)):
    if (turma[i] == pesquisa):
        x = True
if (x):
    print(f"O nome {pesquisa} está na tupla")
else:
    print(f"O nome {pesquisa} não está na tupla")
