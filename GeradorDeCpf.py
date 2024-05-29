import random

cpf_nove_digitos = ''
contador1 = 10
resultado1 = 0

for i in range(9):
    cpf_nove_digitos += str(random.randint(0, 9))


for num in cpf_nove_digitos:
    resultado1 += int(num) * contador1
    contador1 -= 1

num1 = resultado1 * 10 % 11
num1 = num1 if num1 <= 9 else 0

cpf_dez_digito = cpf_nove_digitos + str(num1)
contador2 = 11
resultado2 = 0

for num in cpf_dez_digito:
    resultado2 += int(num) * contador2
    contador2 -= 1

num2 = resultado2 * 10 % 11
num2 = num2 if num2 <= 9 else 0

novo_cpf = f"{cpf_nove_digitos}{num1}{num2}"

print(novo_cpf)

