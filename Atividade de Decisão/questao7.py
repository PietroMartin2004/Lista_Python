"""-Faça um Programa que leia três números e mostre o maior e o menor deles."""

num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maiornum = num
menornum = num

#maior
if num2 > maiornum:
    maiornum = num2

if num3 > maiornum:
    maiornum = num3

#menor
if num2 < menornum:
    menornum = num2

if num3 < menornum:
    menornum = num3


print(f"O maior número é: {maiornum}")
print(f"O menor número é: {menornum}")