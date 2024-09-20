atual = 0
anterior = 1
aut = 0

for i in range(10):
    print(atual)
    aut = anterior
    anterior = atual
    atual = anterior + aut