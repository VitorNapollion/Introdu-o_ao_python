total = 0
media = total/len(Dias)
for i in range(len(Dias)):
  total += Dias[i][1]

print("Temperatura Média do mês: ".format(media))

Novalista = []
for i in range(len(Dias)):
  if Dias[i][1] > media:
    Novalista.append(Dias[i][0])

print(Novalista)
