n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
m = (n1 + n2)/2
print("A sua média foi {:.1f}".format(m))
print("PARABÉNS!"if m >=6 else"ESTUDE MAIS!")