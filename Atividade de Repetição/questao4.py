"""4-Faça um programa que leia um conjunto de números (X) e imprima a quantidade de números pares (QPares) 
e a quantidade de números impares (QImpares) lidos. Admita que o valor 9999 é utilizado como sentinela para fim de leitura."""

numero = 0
pares = 0
impares = 0
contador = 0
while (contador !=9999):
  numero = int(input("Informe o número:"))
  if (numero%2==0):
    pares=pares+1
  elif(numero%2==1):
    impares=impares+1

  print("Pares:",pares)
  print("Impares:",impares)
  contador=int(input("Parar-9999 Continuar-1:"))