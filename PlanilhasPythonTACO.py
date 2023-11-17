# VALORES DA TABELA SAO RELATIVOS A 100G DO ALIMENTO
import time
import pandas as pd

table = pd.read_excel("Taco.xlsx")
# print(table)

# nome_alimento = table.loc[table["Grupo"] == "Cereais e derivados", "Descrição do Alimento"]
# print(nome_alimento)
codigo = True
while codigo == True:

    print("--------------------------------------------------")
    print('''
    \n1 - Cereais e derivados;
    \n2 - Verduras, hortaliças e derivados;
    \n3 - Frutas e derivados;
    \n4 - Gorduras e óleos;
    \n5 - Pescados e frutos do mar;
    \n6 - Carnes e derivados;
    \n7 - Leite e derivados;
    \n8 - Bebidas (alcoólicas e não alcoólicas);
    \n9 - Ovos e derivados;
    \n10 - Produtos açucarados;
    \n11 - Miscelâneas;
    \n12 - Outros alimentos industrializados;
    \n13 - Alimentos preparados;
    \n14 - Leguminosas e derivados;
    '''
    )
    op = input("Digite o número do grupo de alimentos que você deseja ver: ")

    print('|INDEX|               |NOME DO ALIMENTO|')
    if op == '1':
        nome_alimento = table.loc[table["Grupo"] == "Cereais e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == "2":
        nome_alimento = table.loc[table["Grupo"] == "Verduras, hortaliças e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '3':
        nome_alimento = table.loc[table["Grupo"] == "Frutas e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '4':
        nome_alimento = table.loc[table["Grupo"] == "Gorduras e óleos", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '5':
        nome_alimento = table.loc[table["Grupo"] == "Pescados e frutos do mar", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '6':
        nome_alimento = table.loc[table["Grupo"] == "Carnes e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '7':
        nome_alimento = table.loc[table["Grupo"] == "Leite e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '8':
        nome_alimento = table.loc[table["Grupo"] == "Bebidas (alcoólicas e não alcoólicas)", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '9':
        nome_alimento = table.loc[table["Grupo"] == "Ovos e derivados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '10':
        nome_alimento = table.loc[table["Grupo"] == "Produtos açucarados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '11':
        nome_alimento = table.loc[table["Grupo"] == "Miscelâneas", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '12':
        nome_alimento = table.loc[table["Grupo"] == "Outros alimentos industrializados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '13':
        nome_alimento = table.loc[table["Grupo"] == "Alimentos preparados", "Descrição do Alimento"]
        print(nome_alimento)
    elif op == '14':
        nome_alimento = table.loc[table["Grupo"] == "Leguminosas e derivados", "Descrição do Alimento"]
        carbo = table.loc[table["Grupo"] == "Leguminosas e derivados", "Carboidrato(g)"]
        print(f"{nome_alimento} + {carbo}")
    else:
        print("Opção Invalida... \nDigite novamente.")
    time.sleep(3)
    

    
