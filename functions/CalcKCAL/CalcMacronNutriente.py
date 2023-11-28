def calcularMacroNutri(foodName):
    proteina = 4 * (float(input("Digite quantas gramas de proteina tem o alimento: ")))
    carbo = 4 * (float(input("Digite quantas gramas de carboidratos tem o alimento: ")))
    gorduras = 9 * (float(input("Digite quantas gramas de gordura tem o alimento: ")))

    calorias_totais = proteina + carbo + gorduras 
    salvarKCAL(calorias_totais, foodName)
    lerKCAL()

    return calorias_totais



# Para calcular as calorias dos alimentos deve-se multiplicar a quantidade, em gramas, de proteínas, carboidratos e gorduras, 
# de cada porção do alimento, pelo seu respectivo valor calórico. Cada grama de gordura fornece 9 calorias, 
# já os carboidratos e as proteínas fornecem 4 calorias por grama. Por exemplo, uma colher de sopa de azeite contém 8g de gordura 
# e cada grama de gordura tem 9 calorias, logo esta porção de azeite contém 72 calorias.

# Os carboidratos, proteínas e gorduras são digeridos no intestino, onde se dividem nas suas unidades fundamentais:
# Carboidratos em açúcares
# Proteínas em aminoácidos
# Gorduras em ácidos graxos e glicerol

#CONTROLE DE ARQUIVO
filePath = './functions/CalcKCAL/CalcKCAL.txt'
def salvarKCAL(KCAL, foodName):
    op = input('Deseja salvar as informações calóricas acima em um arquivo(S/N)? ').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'w')
        f.writelines(f'Alimento: {foodName}\nCalorias totais: {KCAL}')
        f.close()
    else:
        return
    
def lerKCAL():
    op = input('Deseja ler as informações calóricas que estão salvas(S/N)? ').capitalize().strip()
    if op == 'S':
        f = open(filePath, 'r')
        print(f.read())
        f.close()
    else: 
        return

def deletarKCAL():
    f = open(filePath, 'w')
    f.writelines('')
    f.close()