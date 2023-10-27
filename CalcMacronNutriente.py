def calcularMacroNutri(): 

    proteina = 4 * (float(input("Digite quantas gramas de proteina tem o alimento: "))) 
    carbo = 4 * (float(input("Digite quantas gramas de carboidratos tem o alimento: ")))
    gorduras = 9 * (float(input("Digite quantas gramas de gordura tem o alimento: ")))

    calorias_totais = proteina + carbo + gorduras 
    # print(calorias_totais)
    return calorias_totais



# Para calcular as calorias dos alimentos deve-se multiplicar a quantidade, em gramas, de proteínas, carboidratos e gorduras, 
# de cada porção do alimento, pelo seu respectivo valor calórico. Cada grama de gordura fornece 9 calorias, 
# já os carboidratos e as proteínas fornecem 4 calorias por grama. Por exemplo, uma colher de sopa de azeite contém 8g de gordura 
# e cada grama de gordura tem 9 calorias, logo esta porção de azeite contém 72 calorias.

# Os carboidratos, proteínas e gorduras são digeridos no intestino, onde se dividem nas suas unidades fundamentais:
# Carboidratos em açúcares
# Proteínas em aminoácidos
# Gorduras em ácidos graxos e glicerol