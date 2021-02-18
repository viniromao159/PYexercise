'''18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''


tamanho_arquivo = float(input("Digite o tamanho do arquivo: "))
velocidade_net = float(input("Digite a velocidade da internet (MBPS): "))
tempo_download = tamanho_arquivo / velocidade_net
conver = tempo_download / 60 

print("O sera baixado em ", conver, "min!")