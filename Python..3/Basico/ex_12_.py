"""
Faça um Programa que pergunte quanto você ganha por hora e o número 
de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se
que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato,

faça um programa que nos dê: salário bruto. quanto pagou ao INSS. 
quanto pagou ao sindicato. o salário líquido. calcule os descontos 
e o salário líquido, conforme a tabela abaixo:

"""

ganho_por_hora = float(input("Quanto você ganha por hora (em R$)? "))

horas_trabalhadas_no_mes = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = ganho_por_hora * horas_trabalhadas_no_mes

percentual_ir = 11 / 100
percentual_inss = 8 / 100
percentual_sindicato = 5 / 100

valor_ir = salario_bruto * percentual_ir
valor_inss = salario_bruto * percentual_inss
valor_sindicato = salario_bruto * percentual_sindicato

salario_liquido = salario_bruto - (valor_ir + valor_inss + valor_sindicato)

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda (11%): R$ {valor_ir:.2f}")
print(f"Desconto do INSS (8%): R$ {valor_inss:.2f}")
print(f"Desconto do sindicato (5%): R$ {valor_sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")


