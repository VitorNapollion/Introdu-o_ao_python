Clientes = [["Maria Tavares Raposo", 28, "Rua das Flores, 50", "50357-987"], ["Ivo Souza Marques", 37, "Alameda Iguaçu, 1428, apto 36", "58037-145"], ["bianca nunes dias", 50, "rua livramento, 1078, apartamento 12", "58074-123"]]

novaLista = []
n1 = ["0", "1", "2", "3", "4", "5"]
n2 = ["0", "1", "2"]

for i in range(len(Clientes)):
  
  if (Clientes[i][3][0] in n1) and (Clientes[i][3][1] in n2):
    novalista.append(Clientes[i][0])

print("O numero de pessoas quem moram em Recife é": novaLista)
