"""
Exercício 3.3
Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros
recursos que aprendemos até agora.
1. Escreva uma função que desenhe uma grade como a seguinte:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de
valores separados por vírgula:
print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma: python print('+', end='
') print('-') A saída dessas instruções é + -. Uma instrução print sem argumento
termina a linha atual e vai para a próxima linha.
2. Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro
colunas
"""

# 1:

print("+ ", "- "*4, "+ ", "- "*4, "+")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("+ ", "- "*4, "+ ", "- "*4, "+")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("/", " "*9, "/", " "*9, "/")
print("+ ", "- "*4, "+ ", "- "*4, "+")


# 2:

def linha():
    print("+ ", "- "*2, "+ ", "- "*2, "+ ", "- "*2, "+ ", "- "*2, "+")

def coluna():
    print("|", " " * 5, "|", " " * 5, "|", " " * 5, "|", " " * 5, "|")
    print("|", " " * 5, "|", " " * 5, "|", " " * 5, "|", " " * 5, "|")
    

print("\n\n\n")
def desenho(l,c):
    l()
    c()
    l()
    c()
    l()
    c()
    l()
    c()
    l()

desenho(linha, coluna)
