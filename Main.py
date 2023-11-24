from functions import CalcMacronNutriente, PlanilhasPythonTACO
from functions.IMC import CalcIMC 
from functions.TMB import CalcTaxaMetaBasal
from time import sleep


#VARIAVEIS DE CONTROLE
ctrl = ''
ctrlGeneral = ''
msg = '''\nMenu:
    1. Calcular IMC
    2. Calcular taxa metabólica basal
    3. Calcular macronutrientes e calorias de alimentos
    4. Visualizar alimentos e suas informações por grupos
    5. Sair da aplicação
    Escolha uma opção: '''

#INICIO DO PROGRAMA
print('---\nBem vindo ao CEASAR, o gerenciador saudável!\n---')
while ctrlGeneral != 'out':
    op = input(msg).strip()
    if op == '1':
        while ctrl == '':
            try:
                print('\nOk, vamos calcular seu IMC!')
                sleep(0.7)
                numIMC = CalcIMC.calcularIMC()
                classIMC = CalcIMC.classificarIMC(imc = numIMC)
                sleep(0.7)
                print(classIMC)
                ctrl = classIMC
            except:
                print('--------\nO valor digitado para peso(KG) ou altura(cm) deve ser um numero em formato de digito.\nVerifique e digite novamente.\n--------\n')
    elif op == '2':
        while ctrl == '':
            try:
                print('\nOk, vamos ver sua taxa metabólica basal!')
                sleep(0.7)
                numTMB = CalcTaxaMetaBasal.CalcularTaxaBasal()
                sleep(0.7)
                print(f'---\nSua taxa metabólica basal é de: {numTMB:.2f} KCAL por dia.\n---')
                ctrl = numTMB
            except:
                print('--------\nQualquer valor digitado para calcular sua TMB deve ser um numero em formato de digito.\nVerifique e digite novamente.\n--------\n')
    elif op == '3':
        while ctrl == '':
            try:
                print('\nOk, vamos calcular quantas calorias tem seus alimentos!')
                sleep(0.7)
                nomeAlimento = input('Digite o nome do alimento: ').capitalize()
                numKCAL = CalcMacronNutriente.calcularMacroNutri()
                sleep(0.7)
                print(f'---\nCalorias: {numKCAL:.2f} kcal.\n---')
                ctrl = numKCAL
            except:
                print('--------\nQualquer valor digitado para calcular as calorias de seu alimento deve ser um numero em formato de digito.\nVerifique e digite novamente.--------')
    elif op == '4':
         while ctrl == '':
            try:
                print('\nOk, vamos verificar os alimentos e seus grupos!')
                
                PlanilhasPythonTACO.planilhasTESTE()

                ctrl = 'test'
            except:
                print('--------\nQualquer valor digitado para calcular as calorias de seu alimento deve ser um numero em formato de digito.\nVerifique e digite novamente.--------')
    elif op == '5':
        op = input('\tCerteza que deseja sair da aplicação(S/N)? ').capitalize()
        if op == 'S':
            ctrlGeneral = 'out'
    else:
        print('Opção invalida. Digite novamente...\n')
    
    #CONTROLE FINAL DO PROGRAMA
    ctrl = ''
    sleep(2)
