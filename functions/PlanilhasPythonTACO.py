# VALORES DA TABELA SAO RELATIVOS A 100G DO ALIMENTO
import time
import pandas as pd
#
# ARQUIVO INACABADO
#
#
#VARIAVEIS
table = pd.read_excel("Tabela_Taco_Excel\Taco.xlsx")
# print(table)
msg = '''
    1. Cereais e derivados;
    2. Verduras, hortaliças e derivados;
    3. Frutas e derivados;
    4. Gorduras e óleos;
    5. Pescados e frutos do mar;
    6. Carnes e derivados;
    7. Leite e derivados;
    8. Bebidas (alcoólicas e não alcoólicas);
    9. Ovos e derivados;
    10. Produtos açucarados;
    11. Miscelâneas;
    12. Outros alimentos industrializados;
    13. Alimentos preparados;
    14. Leguminosas e derivados;
'''
def planilhasTESTE():

    codigo = 1
    while codigo == 1:

        print("--------------------------------------------------")
        print(msg)
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
        codigo = input('Aperte 0 para sair: ')
    

    
