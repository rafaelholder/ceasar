import CalcIMC, CalcMacronNutriente, CalcTaxaMetaBasal
from time import sleep

#VARIAVEIS DE CONTROLE
intervaloDeTempo = sleep(1)
ctrl = ''



op = input('''Bem vindo ao CEASAR, o gerenciador saudável!\n
1. Calcular IMC\n2. Calcular taxa metabólica basal\n3. Calcular macronutrientes e calorias de alimentos\n4. Visualizar alimentos e suas informações por grupos\nEscolha uma opção: ''').strip()

if op == '1':
    print('\nOk, vamos calcular seu IMC!')
    intervaloDeTempo
    while ctrl == '':
        try:
            numIMC = CalcIMC.calcularIMC()
            classIMC = CalcIMC.classificarIMC(imc = numIMC)
            ctrl = classIMC
        except:
            print('--------\nO valor digitado para peso(KG) ou altura(cm) deve ser um numero em formato de digito.\nVerifique e digite novamente.\n')
    print(classIMC)
elif op == '2':
    print('\nOk, vamos ver sua taxa metabólica basal!')
    intervaloDeTempo
    while ctrl == '':
        try:
            numTMB = CalcTaxaMetaBasal.CalcularTaxaBasal()
            print('Sua taxa metabólica basal é de: {:.2f}kcal por dia'.format(numTMB))
            ctrl = numTMB
        except:
            print('--------\nQualquer valor digitado para calcular sua TMB deve ser um numero em formato de digito.\nVerifique e digite novamente.\n')
elif op == '3':
    print('\nOk, vamos calcular quantas calorias tem seus alimentos!')
    intervaloDeTempo
    while ctrl == '':
        try:
            nomeAlimento = input('Digite o nome do alimento: ').capitalize()
            numKCAL = CalcMacronNutriente.calcularMacroNutri()
            print('Calorias: {:.2f}kcal'.format(numKCAL))
            ctrl = numKCAL
        except:
            print('--------\nQualquer valor digitado para calcular as calorias de seu alimento deve ser um numero em formato de digito.\nVerifique e digite novamente.\n')
        numKCAL = CalcMacronNutriente.calcularMacroNutri()
        ctrl = numKCAL
elif op == '4':
    intervaloDeTempo
else:
    print('Opção invalida. Digite novamente...\n')
