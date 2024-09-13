"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

while True:

    vogalconso = input("Digite uma letra que deseja saber se é vogal ou consoante: ").lower()


    if len(vogalconso) != 1 or not vogalconso.isalpha():
        print("Digite uma unica letra.")
        continue

    if vogalconso in 'aeiou':
        print(f"A letra '{vogalconso}' é uma vogal.")
        break
    else:
        print(f"A letra '{vogalconso}' é uma consoante.")
        break