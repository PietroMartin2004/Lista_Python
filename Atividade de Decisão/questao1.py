"""-Faça um Programa que peça dois números e imprima o maior deles."""

num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if (num > num2):
    print(f"Número maior: {num}")
elif (num2 > num):
    print(f"Número Maior: {num2}")
else:
    print("Números iguais.")