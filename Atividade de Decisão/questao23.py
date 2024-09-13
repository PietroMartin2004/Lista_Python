"""-Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e arruelas. Têm-se os preços unitários de cada tipo de peça e sabe-se que sobre estes preços incidem descontos de 10% para porcas, 20% para parafusos e 30% para arruelas. Escreva um programa que calcule o valor total da compra de um cliente. Deve ser mostrado o nome do cliente. O número de cada tipo de peça que o mesmo comprou, o total de desconto e o total a pagar pela compra."""

nome_cliente = input("Digite o nome do cliente: ")

# preço das pecas
preco_parafuso = 2.00
preco_porca = 4.00
preco_arruela = 6.00

# solictando cada tipo de peça comprada
quantidade_parafuso = int(input("Digite a quantidade de parafusos comprados: "))
quantidade_porca = int(input("Digite a quantidade de porcas compradas: "))
quantidade_arruela = int(input("Digite a quantidade de arruelas compradas: "))

# calculo do valor bgruto de cada peca
valor_bruto_parafuso = preco_parafuso * quantidade_parafuso
valor_bruto_porca = preco_porca * quantidade_porca
valor_bruto_arruela = preco_arruela * quantidade_arruela

# calculo desconto
desconto_parafuso = valor_bruto_parafuso * 0.20
desconto_porca = valor_bruto_porca * 0.10
desconto_arruela = valor_bruto_arruela * 0.30

# calculo do total de desconto e valor final de cada peca
total_desconto = desconto_parafuso + desconto_porca + desconto_arruela
valor_total = (valor_bruto_parafuso - desconto_parafuso) + (valor_bruto_porca - desconto_porca) + (valor_bruto_arruela - desconto_arruela)

# Informacoes
print("\nResumo da Compra:")
print(f"Nome do Cliente: {nome_cliente}")
print(f"Quantidade de Parafusos: {quantidade_parafuso}")
print(f"Quantidade de Porcas: {quantidade_porca}")
print(f"Quantidade de Arruelas: {quantidade_arruela}")
print(f"Total de Desconto: R$ {total_desconto:.2f}")
print(f"Total a Pagar: R$ {valor_total:.2f}")