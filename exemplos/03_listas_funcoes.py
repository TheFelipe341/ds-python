def media(valores):
    return sum(valores) / len(valores)


notas = [7.5, 8.0, 6.5, 9.0]
print("Notas:", notas)
print(f"Média da turma: {media(notas):.2f}")
print("Maior nota:", max(notas))
