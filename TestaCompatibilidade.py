def TestaCompatibilidade (nome1, data1, nome2, data2):
  nome1 = str(nome1)
  nome1 = str.lower(nome1)
  data1 = str(data1)
  nome2 = str(nome2)
  nome2 = str.lower(nome2)
  data2 = str(data2)

  if (data1[6:10]) == (data2[6:10]):
    if (len(nome1) == len(nome2)):
      if (nome1[0]) == (nome2[0]):
        if (nome1[-1]) == (nome2[-1]):
          resultado = True
  else:
    resultado = False
  return resultado