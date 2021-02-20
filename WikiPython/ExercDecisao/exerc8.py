'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

produto1 = float(input("Insira o valor do primeiro produto: "))
produto2 = float(input("Insira o valor do segundo produto: "))
produto3 = float(input("Insira o valor do terceiro produto: "))

if produto1 < produto2 and produto3:
    print("O primeiro produto custa R$", produto1)

elif produto2 < produto1 and produto3:
    print("O segundo produto custa R$", produto2)

elif produto3 < produto1 and produto3:
    print("O terceiro produto custa R$", produto3)

else:
    print("Preços iguais!")
