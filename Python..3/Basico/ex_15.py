"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
de download do arquivo usando este link (em minutos).

"""

tamanho_arquivo = int(input("Digite o tamanho do arquivo em (MB)"))
velocidade_internet = int(input("Digite a velocidade da internet em (MBps)"))

velocidade_mbps = velocidade_internet / 8 

tempo_em_segundos = tamanho_arquivo / velocidade_mbps

tempo_em_minutos = tempo_em_segundos / 60

print(f"\nTempo aproximado de download: { tempo_em_minutos:.2f} minutos")