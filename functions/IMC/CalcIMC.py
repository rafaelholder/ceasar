import time

# IMC = peso / (altura * altura)
def calcularIMC():
    weight = float(input("Digite seu peso(KG): "))  
    height = float(input("Digite sua altura(CM): ")) / 100
    imc = (weight / (height ** 2))
    return imc
#Classificar IMC
def classificarIMC(imc):
    classe = ''
    if imc > 1 and imc <= 18.4:
        classe = 'Magreza'
    elif imc >= 18.5 and imc <= 24.9:
        classe = 'Normal'
    elif imc >= 25 and imc <= 29.9:
        classe = 'Sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        classe = 'Obesidade grau I'
    elif imc >= 35 and imc <= 39.9:
        classe = 'Obesidade grau II'
    elif imc >= 40:
        classe = 'Obesidade grau III'
    else:
        classe = 'Invalido'
    print('Processando...')
    time.sleep(2)
    salvarImc(imc)
    lerImc()

    return '\nSeu IMC eh de: {:.1f} \nSua classificação eh: {}'.format(imc, classe)

#CONTROLE DE ARQUIVO
filePath = './functions/IMC/IMC.txt'
def salvarImc(imc):
    op = input('Deseja salvar seu IMC em um arquivo(S/N)? ').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'w')
        name = input('Digite seu nome: ')
        f.writelines(f'Nome: {name}\nTaxa IMC: {imc:.2f}')
        f.close()
        print(time.sleep(2),'Processando...')
    else:
        return
    
def lerImc():
    op = input('Deseja ver o IMC que esta salvo(S/N)? ').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'r')
        print(f.read())
        f.close()
        print(time.sleep(2),'Processando...')
    else:
        return
    
def deletarImc():
    f = open(filePath, 'w')
    f.writelines('')
    f.close()
    
