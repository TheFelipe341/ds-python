import csv

with open("notas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["aluno", "nota"])
    w.writerows([["Ana", 8.5], ["Bruno", 6.0], ["Carla", 9.5]])

with open("notas.csv", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        print(linha["aluno"], linha["nota"])
