"""-Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#MEDIA
media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
    status = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = "B"
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = "C"
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = "D"
    status = "REPROVADO"
else:
    conceito = "E"
    status = "REPROVADO"

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")