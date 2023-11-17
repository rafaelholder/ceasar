import time

# IMC = peso / (altura * altura)
def calcularIMC():
    weight = float(input("Digite seu peso(KG): "))  
    height = float(input("Digite sua altura(CM): ")) / 100
    imc = weight / (height ** 2)
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
    
    return '\nSeu IMC eh de: {:.1f} \nSua classificação eh: {}'.format(imc, classe)

# imc = calcularIMC()
# classeIMC = classificarIMC(imc)
# print('Processando...')
# time.sleep(2)
# print('\nSeu IMC eh de: {:.1f} \nSua classificacao eh: {}'.format(imc, classeIMC))