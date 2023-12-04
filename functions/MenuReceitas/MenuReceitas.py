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
            print('\nReceita de café da manhã: ')
            for i in range(1,3):
                filePath = f'{RelativePath}Cafe/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                print(f.read(), end='\n\n')

        elif option == 2:
            print('\nReceita de almoço: ')
            for i in range(1,3):
                filePath = f'{RelativePath}Almoco/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                print(f.read(), end='\n\n')

        elif option == 3:
            print('\nReceita de almoço: ')
            for i in range(1,3):
                filePath = f'{RelativePath}Jantar/{i}.txt'
                f = open(filePath, 'r', encoding='utf8')
                print(f.read(), end='\n\n')
        
