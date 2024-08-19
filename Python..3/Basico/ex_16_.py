"""
Exercício 1: Divisão Segura

Peça dois números ao usuário e tente realizar a divisão do primeiro
pelo segundo. Se ocorrer uma divisão por zero ou se o usuário i
nserir um valor inválido, exiba uma mensagem de erro apropriada.


"""

try:
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    divisao = numero_1 / numero_2
    print(f"O resultado é: {divisao}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Você digitou um valor inválido.")


