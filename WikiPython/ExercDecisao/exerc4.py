''' Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''

letra = str(input("Digite a letra: "))

if letra in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
    print("A letra", letra, "é vogal!")
else:
    print("A letra", letra, "é consoante!")
