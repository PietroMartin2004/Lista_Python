"""-Uma empresa de vendas tem três corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas.

Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido.

Se o valor da venda do corretor estiver entre R$ 30.000.00 e R50.000.00 (incluindo extremos) a comissão será de 9.5%.

Em qualquer outro caso, a comissão será de 7%. Escreva um algoritmo que gere um relatório contendo nome, valor da venda e comissão de cada um dos corretores. O relatório deve mostrar também o total de vendas da empresa."""

total_vendas = 0

# armazenar informaçlao dos corretores
corretores = []

#Informaçao dos corretores
for i in range(1, 4):
    print(f"\nCorretor {i}:")
    nome = input("Digite o nome do corretor: ")
    valor_venda = float(input("Digite o valor da venda: R$ "))

    if valor_venda > 50000.00:
        comissao = valor_venda * 0.12
    elif 30000.00 <= valor_venda <= 50000.00:
        comissao = valor_venda * 0.095
    else:
        comissao = valor_venda * 0.07


    total_vendas += valor_venda


    corretores.append((nome, valor_venda, comissao))

#RELATORIO
print("\nRelatório de Comissões:")
print("-=" * 40)
print(f"{'Nome':<20} {'Valor da Venda':<20} {'Comissão':<10}")
print("-" * 40)
for nome, valor_venda, comissao in corretores:
    print(f"{nome:<20} R$ {valor_venda:<19.2f} R$ {comissao:<10.2f}")

print("-" * 40)
print(f"Total de Vendas: R$ {total_vendas:.2f}")