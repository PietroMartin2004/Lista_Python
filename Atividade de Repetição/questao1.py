"""1-Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo."""
salario = 0.0
quant = 0
contador = 0
menor = 99999
totals = 0
soma = 0
media = 0
quant = int(input("Informe a quantidade de funcionários: "))
while (contador < quant):
  contador = contador +1
  print("-=-"*7)
  nome = str(input("Informe o nome: "))
  salario = float(input("Infome o salario: "))
  soma = soma+salario
  media = soma/quant
  if (salario > totals):
    totals = salario
  elif (salario < menor):
    menor = salario
print("-=-"*7)
print("Média salarial: ",media)
print("Maior salario: ", totals)
print("Menor salario: ",menor)
print("Quantidade de funcionário: ",quant)
print("-=-"*7)