"""2-Um hotel com 30 quartos cobra R$ 50,00 por diária e mais uma taxa de serviços. A taxa de serviços é de:

• R 4,00 por diária, se o número de diárias for < 15;

• R 3,60 por diária, se o número de diárias for = 15;

• R 3,00 por diária, se o número de diárias for > 15.

Faça um programa que imprima o nome e o total da conta de cada cliente do hotel.
Imprima também o total ganho pelo hotel."""

diaria = 50.00
dia = 0
totalcontahotel = 0.0
for i in range (0, 2, 1):
  print("-=-"*7)
  nomecliente = input("Insira seu nome: ")
  dia = int(input("Quantos dias ficara no hotel: "))
  if dia < 15:
      taxa = 4.00
  elif dia == 15:
      taxa = 3.60
  else:
      taxa = 3.00

  totalconta = dia*diaria+taxa
  print("Sua conta é de ", totalconta)
  totalcontahotel += totalconta
print("-=-"*7)
print("Totla conta do HOTEL: ",totalcontahotel)
print("-=-"*7)