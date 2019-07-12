"""
print("\033[31mOlá, mundo!")#Letra vermelha
print("\033[31;43mOlá, mundo!")#Letra vermelha com fundo amarelo
print("\033[1;31;43mOlá, mundo!")#Negrito com letra vermelha e fundo amarelo
print("\033[1;31;43mOlá, mundo!\033[m")#Negrito com letra vermelha e fundo amarelo com faixa amarela ate o texto
print("\033[4;31;43mOlá, mundo!\033[m")#Sublinhado com letra vermelha e fundo amarelo com faixa amarela ate o texto
print("\033[4;30;45mOlá, mundo!\033[m")#Sublinhado com letra branca e fundo magenta com faixa magenta ate o texto
print("\033[30mOlá, mundo!\033[m")#Letra branca com fundo preto
print("\033[37mOlá, mundo!\033[m")#padrão
print("\033[7;30mOlá, mundo!\033[m")#Letra preta com fundo branco com faixa branco ate o texto
print("\033[0;33;44mOlá, mundo!\033[m")#Sem formatação(o 7 inverte a formatação) oom letra amarela e fundo azul com faixa azul ate o texto
print("\033[7;33;44mOlá, mundo!\033[m")#Inversão de formatação oom letra amarela e fundo azul com faixa azul ate o texto
"""

"""
a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m.".format(a, b))
print("Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m.".format(a, b))#Cores no texto
"""

nome = "Rafela"
cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "amarelo":"\033[33m",
         "pretoebranco":"\033[7;30m"}
#print("Olá! Muito prazer em te conhecer. {}{}{}!!!".format(cores["amarelo"],nome,cores["limpa"]))#Lista de cores
print("Olá! Muito prazer em te conhecer. {}{}{}!!!".format(cores["pretoebranco"],nome,cores["limpa"]))
#print("Olá! Muito prazer em te conhecer. {}{}{}!!!".format("\033[4;34m",nome,"\033[m"))#Cores no fim do texto junto do format