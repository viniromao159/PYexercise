'''17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''


area_metros2 = float(input("Quantos m² vai ser pintado: "))
litro_tinta = area_metros2 / 6
lata_tinta = litro_tinta / 18
galao_tinta = litro_tinta / 3.6
preço_galao = galao_tinta*25.00
preço_lata = lata_tinta*80.00


print("Lata - Deve comprar: ",lata_tinta," latas \nValor total é: ", preço_lata)
print("Galao - Deve comprar: ",galao_tinta," latas \nValor total é: ", preço_galao)