"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre: o produto do dobro do primeiro com metade do 
segundo. a soma do triplo do primeiro com o terceiro. 
o terceiro elevado ao cubo.

"""


number_one = int(input("Digite um numero inteiro : "))
number_two = int(input("Digite um numero inteiro : "))
number_three = float(input("Digite um numero inteiro : "))

product = (number_one * 2) * (number_two / 2)

triple = number_one * 3 + number_three

cube =  triple ** 3


print(f"O produto do dobro do primeiro com metade do segundo é: {product}")
print(f"A soma do triplo do primeiro com o terceiro é: {triple}")
print(f"O terceiro elevado ao cubo é: {cube}")