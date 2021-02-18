'''15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido'''

ganho_hora = float(input("Ganho por hora: "))
horas_mensais = float(input("Horas trabalhadas: "))
salario_bruto = float(ganho_hora*horas_mensais)
desc_impostorenda = 11/100 * salario_bruto
desc_inss = 8/100 * salario_bruto
desc_sindicato = 5/100 * salario_bruto
salario_liquido = salario_bruto - (desc_impostorenda + desc_inss + desc_sindicato)

print("Salario bruto: ", salario_bruto)
print("Pago ao INSS: ", desc_inss)
print("Pago ao Sindicato: ", desc_sindicato)
print("Salario Liquido: ", salario_liquido)
print("Descontos: ", desc_impostorenda + desc_inss + desc_sindicato)