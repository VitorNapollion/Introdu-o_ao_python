Pontuacao = int(input("Qual a Pontuação: "))
ValorT = float(input("Qual o Valor: "))

faculdade1 = ""
faculdade2 = ""
faculdade3 = ""

if (Pontuacao >= 600) and (ValorT / 3 >= 300.50 ):
  faculdade1 = "Eldorado"

if (Pontuacao >= 720) and (ValorT / 3 >= 410):
  faculdade2 = "Charlote"


if (Pontuacao >= 880) and (ValorT / 3 >= 550.30):
  faculdade3 = "Mirante"

print(faculdade1)
print(faculdade2)
print(faculdade3)
