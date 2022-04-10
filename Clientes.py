
Clientes = [["Maria Tavares Raposo", 28, "Rua das Flores, 50", "50357-987"], ["Ivo Souza Marques", 37, "Alameda Iguaçu, 1428, apto 36", "58037-145"], ["bianca nunes dias", 50, "rua livramento, 1078, apartamento 12", "58074-123"]]

endereco = []
cont = 0
idade = 0

for i in range (len(Clientes)):
    endereco = Clientes[i][2].split(" ")
    for j in range(len(endereco)):
        if endereco[j] == 'apto' or endereco[j] == 'apartamento':
            cont+=1
            idade+= Clientes[i][1]
print(idade/cont)
