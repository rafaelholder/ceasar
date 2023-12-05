from functions.CalcKCAL import CalcMacronNutriente
from functions.IMC import CalcIMC
from functions.TMB import CalcTaxaMetaBasal
from functions import PlanilhasPythonTACO
from functions.MenuReceitas import MenuReceitas 
from time import sleep


#VARIAVEIS DE CONTROLE
ctrl = ''
sairFunc = 'SAIDADAFUNÇÃO'
ctrlGeneral = ''
msg = '''\nMenu:
    1. Calcular IMC
    2. Calcular taxa metabólica basal
    3. Calcular macronutrientes e calorias de alimentos
    4. Visualizar alimentos e suas informações por grupos
    5. Receitas
    6. Sair da aplicação
    Escolha uma opção: '''

#INICIO DO PROGRAMA
print('---\nBem vindo ao Fitness Assistant, o assistente e gerenciador da sua Saúde!\n---')
while ctrlGeneral != 'out':
    op = input(msg).strip()
    if op == '1':
        while ctrl != sairFunc:
            try:
                print('\nOk, vamos calcular seu IMC!')
                sleep(0.7)
                numIMC = CalcIMC.calcularIMC()
                classIMC = CalcIMC.classificarIMC(imc = numIMC)
                sleep(0.7)
                print(classIMC)
                ctrl = sairFunc
            except:
                print('--------\nO valor digitado para peso(KG) ou altura(cm) deve ser um numero em formato de digito.\nVerifique e digite novamente.\n--------\n')
    elif op == '2':
        while ctrl != sairFunc:
            try:
                print('\nOk, vamos ver sua taxa metabólica basal!')
                sleep(0.7)
                numTMB = CalcTaxaMetaBasal.CalcularTaxaBasal()
                sleep(0.7)
                print(f'---\nSua taxa metabólica basal é de: {numTMB:.2f} KCAL por dia.\n---')
                ctrl = sairFunc
            except:
                print('--------\nQualquer valor digitado para calcular sua TMB deve ser um numero em formato de digito.\nVerifique e digite novamente.\n--------\n')
    elif op == '3':
        while ctrl != sairFunc:
            try:
                print('\nOk, vamos calcular quantas calorias tem seus alimentos!')
                sleep(0.7)
                foodName = input('Digite o nome do alimento: ').capitalize().strip()
                numKCAL = CalcMacronNutriente.calcularMacroNutri(foodName)
                sleep(0.7)
                print(f'---\nCalorias: {numKCAL:.2f} kcal.\n---')
                ctrl = sairFunc
            except:
                print('--------\nQualquer valor digitado para calcular as calorias de seu alimento deve ser um numero em formato de digito.\nVerifique e digite novamente.--------')
    elif op == '4':
         while ctrl != sairFunc:
            try:
                print('\nOk, vamos verificar os alimentos e seus grupos!')
                sleep(0.7)
                PlanilhasPythonTACO.planilhasTESTE()
                sleep(0.7)
                ctrl = sairFunc
            except:
                print('--------\nQualquer valor digitado para calcular as calorias de seu alimento deve ser um numero em formato de digito.\nVerifique e digite novamente.--------')
    elif op == '5':
            try:
                print('\nOk, vamos verificar algumas receitas!')

                MenuReceitas.MenuDeReceitas()

                ctrl = sairFunc
            except:
                print('--------Erro na receita.\nVerifique e digite novamente.--------')
    elif op == '6':
        op = input('\tCerteza que deseja sair da aplicação(S/N)? ').capitalize().strip()
        if op == 'S':
            ctrlGeneral = 'out'
    else:
        print('Opção inválida. Digite novamente...\n')

    #CONTROLE FINAL DO PROGRAMA
    ctrl = ''
    sleep(2)

