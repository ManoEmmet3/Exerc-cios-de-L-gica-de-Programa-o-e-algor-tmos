"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""

import math


area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))


cobertura_por_litro = 3  
capacidade_lata = 18  
preco_lata = 80  


litros_necessarios = area / cobertura_por_litro


latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)


custo_total = latas_necessarias * preco_lata


print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
print(f"Preço total: R$ {custo_total:.2f}")
