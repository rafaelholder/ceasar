def cadastrarAlimento():
    foodName = input('Digite o nome do alimento a ser cadastrado: ').capitalize().strip()
    
    op = int(input('1. Cadastrar as calorias totais do alimento.\n2. Cadastrar gorduras, proteínas e carboidratos.\nEscolha uma opção: '))
    print('--CALORIAS BASEADA EM PROPORÇÃO DE 100G DO ALIMENTO--')
    if op == 1:
        caloriasTotais = float(input('Digite as calorias totais(kcal): '))
    elif op == 2:
        gordurasTotais = float(input('Digite as gorduras totais: '))
        protTotais = float(input('Digite as proteínas totais: '))
        carboTotais = float(input('Digite os carboidratos totais: '))
        caloriasTotais = (protTotais * 4) + (carboTotais * 4) + (gordurasTotais * 9)
    
    print(f"\nNome do alimento: {foodName}\nCalorias totais: {caloriasTotais}kcal")
    salvarAlimento(foodName, caloriasTotais)
    lerAlimentos()


#CONTROLE DE ARQUIVO
filePath = './functions/CadastrarAlimentos/ListaAlimentos.txt'
def salvarAlimento(foodName, KCAL):
    op = input('Deseja salvar este alimento em um arquivo(S/N)?').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'w')
        f.writelines(f'-Nome do Alimento: {foodName}\n-Calorias totais: {KCAL} ')
        f.close()
    else:
        return
    
def lerAlimentos():
    op = input('Deseja ler as informações salvas sobre o alimento no arquivo(S/N)?').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'r')
        print(f.read())
        f.close()

def deletarAlimento():
    f = open(filePath, 'w')
    f.writelines('')
    f.close()