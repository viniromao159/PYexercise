'''13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = str(input("M - Masculino / F - Feminino: "))
altura = float(input("Insira sua altura: "))

if sexo == "F" or sexo == "M":
    if sexo == "M":
        peso_ideal_homem = (72.7*altura)-58
        print("O peso ideal pra homem é: ", peso_ideal_homem)
    else:
        peso_ideal_mulher = (62.1*altura)-44.7
        print("Para mulheres é: ", peso_ideal_mulher)
else:
    print("Operador invalido")
