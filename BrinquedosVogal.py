Brinquedos = [["Bola", 15.80],["Estela e bebê", 26.90], ["Alquimia", 31.20], ["Quebra-cabeça", 47.00]]

vogais = ["A", "Ã", "Á", "À", "Â", "E", "È", "É", "Ê", "I", "Í", "O", "Ó", "Ô", "Õ", "U", "Û"]

Quant = 0

for i in range(len(Brinquedos)):

    if (Brinquedos[i][0][0] in vogais) and (Brinquedos[i][1] > 20):
        Quant += 1

print(Quant)
