#solicite ao usuario o numero para ser dividido e o divisor
#o resultado tem valor real
num3 = float(input('Digite um número que deseja dividir:'))
divisor = float(input('Digite o divisor: '))
resultado = num3/divisor #resultado real
print(f"O resultado da sua divisão de {num3} dividido por {divisor} é: {resultado}")
#---------------------------------------------------
num3 = float(input('Digite um número que deseja dividir:'))
divisor = float(input('Digite o divisor: '))
resultado = num3//divisor #sem dizima periodica
print(f"O resultado da sua divisão de {num3} dividido por {divisor} é: {resultado}")
#---------------------------------------------------
num3 = float(input('Digite um número que deseja dividir:'))
divisor = float(input('Digite o divisor: '))
resultado = num3%divisor #resultado será somente o resto
print(f"O resultado da sua divisão de {num3} dividido por {divisor} é: {resultado}")