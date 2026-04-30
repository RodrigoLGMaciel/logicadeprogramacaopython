#solicite o valor do salário do usuário e coloque o valor do salário mínimo, calcule quantos salários mínimos o usuário recebe
salarioU = float(input("Digite seu salário atual: "))
salarioM = 1621.0
resultado = salarioU/salarioM
print(f"Você recebe {salarioU}, o salário mínimo vale atualmente {salarioM}, então você recebe {resultado:.2f} salários mínimos")