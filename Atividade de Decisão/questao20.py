"""-Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não esteja neste intervalo, exibir mensagem: número inválido."""

numero = int(input("Digite um número de 1 a 5: "))

if numero == 1:
  print("Um")
elif numero == 2:
  print("Dois")
elif numero == 3:
  print("Três")
elif numero == 4:
  print("Quatro")
elif numero == 5:
  print("Cinco")
else:
  print("Número invalido...") 