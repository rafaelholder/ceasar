#!/usr/bin/python
# -*- coding: UTF-8 -*-
def MenuDeReceitas():
    #VARIAVEIS
    RelativePath = './functions/MenuReceitas/'
    msg = """\nOk, qual o tipo de refeição desejada?
                1. Café da manhã
                2. Almoço
                3. Jantar
                4. Voltar ao menu principal
    """
    option = 0
    while option != 4:
        option = int(input(msg + '\nDigite o número da opção desejada: ').strip())

        if option == 1:
            print('\nReceita de café da manhã:\n')
            for i in range(1,3):
                filePath = f'{RelativePath}Cafe/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                fileInfo = f.read()
                print(fileInfo)
                print('==========\n')
                f.close()
        elif option == 2:
            print('\nReceita de almoço:\n')
            for i in range(1,3):
                filePath = f'{RelativePath}Almoco/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                fileInfo = f.read()
                print(fileInfo)
                print('==========\n')
                f.close()
        elif option == 3:
            print('\nReceita de jantar:\n')
            for i in range(1,3):
                filePath = f'{RelativePath}Jantar/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                fileInfo = f.read()
                print(fileInfo)
                print('==========\n')
                f.close()
        elif option == 4:
            print('Ok! Voltando para o menu principal.')
        else:
            print('Valor digitado é invalido. Digite novamente.')
