cont = 0

for i in range (len(Dias)):

  if (Dias[i][1] <=28 and Dias[i][2] == "sim"):
    cont += 1

print("Dias chuvosos e com temperatura menor ou igual a 28º: ", cont)
