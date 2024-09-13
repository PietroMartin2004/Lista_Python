"""-Faça um Programa que leia três números e mostre o maior deles."""

num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maiornum = num

if num2 > maiornum:
    maiornum = num2

if num3 > maiornum:
    maiornum = num3

print(f"O maior número é: {maiornum}")