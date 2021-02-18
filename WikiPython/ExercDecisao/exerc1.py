'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print("Os valores inseridos são identicos!")
