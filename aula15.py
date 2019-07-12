"""cont = 1
while cont <= 10:
    print(cont, " ", end="")
    cont += 1
print("ACABOU")
...........................................
cont = 1
while cont <= 10:
    print(cont, "... ", end="")
    cont += 1
print("ACABOU")
..........................................
cont = 1
while cont <= 10:
    print(cont, " -> ", end="")
    cont += 1
print("ACABOU")
...........................................
cont = 1
while True:
    print(cont, " -> ", end="")
    cont += 1
print("ACABOU")
.........................................
n = 0
while n != 999:
    n = int(input("Digite um número: "))
........................................
n = cont = 0
while cont < 3:
    n = int(input("Digite um número: "))
    cont +=1
.........................................
n = 0
while n != 999:
    n = int(input("Digite um número: "))
...........................................
n = s = 0
while n != 999:
    n = int(input("Digite um número: "))
    s += n
s -= 999# gambiarra não pode ser feito
print("A soma vale {}".format(s))
............................................
n = s = 0
while True:
    n = int(input("Digite um número: "))
    s += n
print("A soma vale {}".format(s))
........................................

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
#print("A soma vale {}".format(s))
print(f"A soma vale {s}")#f string simplificão a forma de escrever (tecnica de interpulação dentro da string)
.................................................
nome = "José"
idade = 33
print(f"O {nome} tem {idade} anos.")#Python 3.6+
print("O {} tem {} anos.".format(nome, idade)#PYTHON 3
print("O %s tem %d anos."%(nome, idade))#Python 2
.......................................................

nome = "José"
idade = 33
#salario = 987.35
salario = 987.3
print(f"O {nome} tem {idade} anos e ganha R${salario:.2f}")
"""


