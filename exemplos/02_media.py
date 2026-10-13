n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
print(f"Média: {media:.1f}")
print("Aprovado" if media >= 6 else "Recuperação" if media >= 4 else "Reprovado")
