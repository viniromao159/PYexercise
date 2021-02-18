'''11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo 
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = float(input("Digite o Terceiro numero: "))

print("A = ", (n1*2)+(n2/2))
print("B = ", (n1*3)+n3)
print("C = ", n3*n3*n3)