"""-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até 280,00 (incluindo): aumento de 20%

salários entre 280,00 e 700,00: aumento de 15%

salários entre 700,00 e 1500,00: aumento de 10%

salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:

salário antes do reajuste;
percentual de aumento aplicado;
valor do aumento;
novo salário, após o aumento."""

salario_atual = float(input("Digite o salário atual do colaborador: "))

if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")