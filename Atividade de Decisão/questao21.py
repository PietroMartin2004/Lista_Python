"""-Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:

a) o nome e as notas em cada prova do candidato

b) a média do candidato

c) uma informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0**"""

nome = input("Digite o nome do candidato: ")

nota_portugues = float(input("Digite a nota em Português: "))
nota_matematica = float(input("Digite a nota em Matemática: "))
nota_conhecimentos_gerais = float(input("Digite a nota em Conhecimentos Gerais: "))


media = (nota_portugues + nota_matematica + nota_conhecimentos_gerais) / 3

aprovado = media > 7.0 and nota_portugues >= 5.0 and nota_matematica >= 5.0 and nota_conhecimentos_gerais >= 5.0

# Exibição
print("\nInformações do Candidato:")
print(f"Nome: {nome}")
print(f"Nota em Português: {nota_portugues}")
print(f"Nota em Matemática: {nota_matematica}")
print(f"Nota em Conhecimentos Gerais: {nota_conhecimentos_gerais}")
print(f"Média: {media:.2f}")

# Se nao for aprovado
if aprovado:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")
