"""-Um hotel cobra R$ 60.00 a diária e mais uma taxa de serviços. A taxa de serviços é de:

• R$ 5.50 por diária, se o número de diárias for maior que 15;

• R$ 6.00 por diária, se o número de diárias for igual a 15;

• R$ 8.00 por diária, se o número de diárias for menor que 15.

Construa um algoritmo que mostre o nome e o total da conta de um cliente.**"""


nome_cliente = input("Digite o nome do cliente: ")

num_diarias = int(input("Digite o número de diárias: "))

# valor da diaria
valor_diaria = 60.00

if num_diarias > 15:
    taxa_servico = 5.50
elif num_diarias == 15:
    taxa_servico = 6.00
else:
    taxa_servico = 8.00

# calcula o total na conta
total_conta = (valor_diaria * num_diarias) + (taxa_servico * num_diarias)

# informacoes
print(f"\nNome do Cliente: {nome_cliente}")
print(f"Total da Conta: R$ {total_conta:.2f}")