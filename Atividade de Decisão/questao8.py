"""-Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

preco = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

#minimo
menorpreco = min(preco, preco2, preco3)

if menorpreco == preco:
    print("Primeiro produto está na melhor faixa etária.")
elif menorpreco == preco2:
    print("Segundo produto está na melhor faixa etária.")
else:
    print("Terceiro produto está na melhor faixa etária.")