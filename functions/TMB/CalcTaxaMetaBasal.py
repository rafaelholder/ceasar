#CALCULADORA DE TAXA METABÓLICA BASAL
def CalcularTaxaBasal():
    #VARIÁVEIS
    idade = int(input('Digite a sua idade: ')).strip()
    altura = float(input('Agora a sua altura(CM): ')).strip()
    peso = float(input('Agora o seu peso(KG): ')).strip()
    sexo = int(input('Finalizando, qual é o seu sexo? \n   Digite 1 para Masculino e 2 para Feminino: ')).strip()
    msg = '''Qual é a sua taxa de atividade física?
        1 - Sedentários (pouco ou nenhum exercício)
        2 - Levemente ativo (exercício leve 1 a 3 dias por semana)
        3 - Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana)
        4 - Altamente ativo (exercício pesado de 5 a 6 dias por semana)
        5 - Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia)
        Digite sua resposta: '''.strip()

    fatorAtvFisica = float(input(msg))

    if fatorAtvFisica == 1:
        fatorAtvFisica = 1.2
    elif fatorAtvFisica == 2:
        fatorAtvFisica = 1.375
    elif fatorAtvFisica == 3:
        fatorAtvFisica = 1.55
    elif fatorAtvFisica == 4:
        fatorAtvFisica = 1.725
    elif fatorAtvFisica == 5:
        fatorAtvFisica = 1.9
    else:
        # Tratar o caso em que o valor inserido não é 1, 2, 3, 4 ou 5
        print("Valor inválido")

    if sexo == 1:
        taxaMetabolicaBasal = float(fatorAtvFisica * (66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)))
    elif sexo == 2:
        taxaMetabolicaBasal = float(fatorAtvFisica * (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)))


    salvarTMB(tmb=taxaMetabolicaBasal, age=idade)
    lerTMB()

    return taxaMetabolicaBasal

#CONTROLE DE ARQUIVO
filePath = './functions/TMB/TMB.txt'
def salvarTMB(tmb, age):
    op = input('Deseja salvar sua taxa metabólica basal em um arquivo(S/N)? ').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'w')
        name = input('Digite seu nome: ').capitalize().strip()
        f.writelines(f'Nome: {name}\nIdade: {age}\nTaxa metabólica basal: {tmb:.2f}')
        f.close()
    else:
        return

def lerTMB():
    op = input('Deseja ler a taxa metabólica basal que esta salva(S/N)?').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'r')
        print(f.read())
        f.close()
    else:
        return

def deletarTMB():
    f = open(filePath, 'w')
    f.writelines('')
    f.close()


