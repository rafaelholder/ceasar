#CALCULADORA DE TAXA METABÓLICA BASAL
def CalcularTaxaBasal():
    #VARIÁVEIS
    idade = int(input('Digite a sua idade: ')) 
    altura = float(input('Agora a sua altura(CM): '))
    peso = float(input('Agora o seu peso(KG): ')) 
    sexo = int(input('Finalizando, qual é o seu sexo? \n   Digite 1 para Masculino e 2 para Feminino: '))

    fatorAtvFisica = float(input('''\nQual é a sua taxa de atividade física?
        1 - Sedentários (pouco ou nenhum exercício)
        2 - Levemente ativo (exercício leve 1 a 3 dias por semana)
        3 - Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana)
        4 - Altamente ativo (exercício pesado de 5 a 6 dias por semana)
        5 - Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia)  
    Digite sua resposta: '''))
    
    match fatorAtvFisica:
        case 1:
            fatorAtvFisica = 1.2
        case 2: 
            fatorAtvFisica = 1.375
        case 3:
            fatorAtvFisica = 1.55
        case 4: 
            fatorAtvFisica = 1.725
        case 5:
            fatorAtvFisica = 1.9

    if sexo == 1:
        taxaMetabolicaBasal = float(fatorAtvFisica * (66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)))
    elif sexo == 2:
        taxaMetabolicaBasal = float(fatorAtvFisica * (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)))

    return taxaMetabolicaBasal

#MOSTRANDO A TAXA
# TMB= CalcularTaxaBasal()
# print('Sua taxa metabólica basal é de: {:.2f}'.format(TMB))


