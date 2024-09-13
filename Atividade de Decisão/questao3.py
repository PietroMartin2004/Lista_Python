"""-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

while True:

    sexo = input("Qual seu sexo? (F para Feminino ou M para Masculino): ").upper()

    if sexo == 'F':
        print("Feminino")
        break
    elif sexo == 'M':
        print("Masculino")
        break
    else:
        print("Sexo Inválido. Continuando...")