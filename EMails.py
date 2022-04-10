def EmailsValidos(conta):
  quantEmails = 0
  num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  if ("@" in conta) and ((len(conta[0:conta.index("@")])) >= 5) and ((len(conta[0:conta.index("@")])) <= 15) and ("." in conta[conta.index("@"):-1]) and (len(conta[conta.index("@"):-1]) >= 7) and (conta[0] not in num) and (conta[-1] not in num):

    quantEmails += 1

  return quantEmails
