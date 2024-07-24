"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e 
os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.

"""
import math

area = float(input("Digite a área a ser pintada :  "))

area_com_folga = area * 1.10

litros_necessarios = area_com_folga / 6 

# Comprar apenas latas de 18 litros

latas_necessarias = math.ceil(litros_necessarios / 18)

Custo_lata = latas_necessarias * 80

# Comprar Apenas Galões de 3,6 Litros:

galoes_necessarios = math.ceil(litros_necessarios / 3.6)

Custo_galoes = litros_necessarios * 25

# Misturar Latas e Galões:

latas_mistura = math.floor(litros_necessarios / 18)
litros_restantes = litros_necessarios - (latas_mistura * 18)

galoes_mistura = math.ceil(litros_restantes / 3.6)
custo_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print(f"\nPara pintar {area:.2f} metros quadrados com 10% de folga:")
print(f"\n1. Comprando apenas latas de 18 litros:")
print(f"   - Quantidade de latas: {latas_necessarias}")
print(f"   - Custo total: R$ {Custo_lata:.2f}")

print(f"\n2. Comprando apenas galões de 3,6 litros:")
print(f"   - Quantidade de galões: {galoes_necessarios}")
print(f"   - Custo total: R$ {Custo_galoes:.2f}")

print(f"\n3. Misturando latas e galões para o menor preço:")
print(f"   - Quantidade de latas: {latas_mistura}")
print(f"   - Quantidade de galões: {galoes_mistura}")
print(f"   - Custo total: R$ {custo_mistura:.2f}")