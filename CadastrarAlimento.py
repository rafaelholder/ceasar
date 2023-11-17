def cadastrarAlimento():
    nomeAlimento = input('Digite o nome do alimento a ser cadastrado: ').capitalize()
    
    op = int(input('1. Cadastrar as calorias totais do alimento.\n2. Cadastrar gorduras, proteínas e carboidratos.\nEscolha uma opção: '))
    if op == 1:
        caloriasTotais = float(input('Digite as calorias totais(kcal): '))

    elif op == 2:
        gordurasTotais = float(input('Digite as gorduras totais: '))
        protTotais = float(input('Digite as proteínas totais: '))
        carboTotais = float(input('Digite os carboidratos totais: '))
        caloriasTotais = (protTotais * 4) + (carboTotais * 4) + (gordurasTotais * 9)
    
    print(f"\nNome do alimento: {nomeAlimento}\nCalorias totais: {caloriasTotais}kcal")

