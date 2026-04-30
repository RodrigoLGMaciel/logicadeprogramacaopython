#crie um programa de calculo de imc, recebendo do usuario os dados de peso e altura
#lembrando que imc = (peso(altura²))
#usaremos altura para (² potência) **
nome = input('Qual é seu nome?: ')
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = (peso/(altura**2))
print(f"Obrigado {nome}, seu IMC é: {imc:.2f}") #(.2f) limita as casas decimais pós vírgula