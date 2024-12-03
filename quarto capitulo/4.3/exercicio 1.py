"""
1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um
turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para o square e
então execute o programa novamente.
"""
import turtle


def square(t):
    """
    :param t: objeto do tipo turtle
    :return: retorna o desenho de um quadrado
    """
    for i in range(4):
        t.fd(100)
        t.lt(90)


bob = turtle.Turtle()

square(bob)
turtle.mainloop()