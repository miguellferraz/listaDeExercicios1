notas = [6.3, 7.5, 9.2, 5.1, 6.8]

media = sum(notas) / len(notas)

notasAcima = len([nota for nota in notas if nota > 6])

print(f"A média das notas é: {media:.2f}")
print(f"Quantidade de notas acima da média: {notasAcima}")

