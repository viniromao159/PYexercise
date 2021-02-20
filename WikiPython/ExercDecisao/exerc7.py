'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segunda numero: "))
n3 = int(input("Insira o terceiro numero: "))

if n1 > n2 and n3:
    if n2 < n3:
        print("O menor numero é ", n2)
    else:
        print("O menor numero é ", n3)
    print("O maior numero é ", n1)

elif n2 > n1 and n3:
    if n1 < n3:
        print("O menor numero é ", n1)
    else:
        print("O menor numero é ", n3)
    print("O maior numero é ", n2)

elif n3 > n1 and n2:
    if n1 < n2:
        print("O menor numero é ", n1)
    else:
        print("O menor numero é ", n2)
    print("O maior numero é ", n3)

else:
    print("Numeros iguais!")
