"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa
 um algoritmo que calcule seu peso ideal, utilizando as seguintes 
fórmulas: 
Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
"""

height = float(input("Digite sua altura para calcular o peso ideal : "))

gender = input("qual seu genero : masculino ou feminino ? : ")

if gender == 'masculino':
    weight_man = (72.7 * height) - 58
    print(f"seu pelo ideal é: {weight_man}")

else:
    weight_woman = (62.1 * height) - 44.7
    print(f"seu peso idel é {weight_woman}")



