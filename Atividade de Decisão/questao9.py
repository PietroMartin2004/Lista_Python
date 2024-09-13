"""-Faça um Programa que leia três números e mostre-os em ordem decrescente."""

num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num >= num2 and num >= num3:
    if num2 >= num3:
        print(num, num2, num3)
    else:
        print(num, num3, num2)
elif num2 >= num and num2 >= num3:
    if num >= num3:
        print(num2, num, num3)
    else:
        print(num2, num3, num)
else:
    if num >= num2:
        print(num3, num, num2)
    else:
        print(num3, num2, num)