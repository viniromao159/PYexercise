'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas
print("Salário bruto: (valor_hora  * horas_trabalhadas) : R$", salario_bruto)

desc_inss = salario_bruto*0.10
desc_fgts = salario_bruto*0.11


if salario_bruto <= 900:
    total_desconto = desc_inss + desc_fgts
    print('(-) IR (Isento): R$ 0.00')
    salario_liquido = salario_bruto - total_desconto

elif salario_bruto > 900 and salario_bruto <= 1500:
    desc_ir = salario_bruto * 0.05
    print('(-) IR (5%): R$', desc_ir)
    total_desconto = desc_inss + desc_fgts + desc_ir
    salario_liquido = salario_bruto - total_desconto

elif salario_bruto > 1500 and salario_bruto <= 2500:
    desc_ir = salario_bruto * 0.10
    print('(-) IR (10%): R$', desc_ir)
    total_desconto = desc_inss + desc_fgts + desc_ir
    salario_liquido = salario_bruto - total_desconto

else:
    desc_ir = salario_bruto * 0.20
    print('(-) IR (20%): R$', desc_ir)
    total_desconto = desc_inss + desc_fgts + desc_ir
    salario_liquido = salario_bruto - total_desconto

print('(-) INSS (10%): R$', desc_inss)
print('FGTS (11%): R$', desc_fgts)
print('Total descontos: R$', total_desconto)
print('Salario liquido: R$', salario_liquido)
