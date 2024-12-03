"""
4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e
desenhe um círculo aproximado ao chamar polygon com um comprimento e número
de lados adequados. Teste a sua função com uma série de valores de r.
Dica: descubra a circunferência do círculo e certifique-se de que length * n =
circumference.
"""

import turtle


def polygon(t, length, n):
    """
    :param t: objeto do tipo turtle
    :param length: comprimento dos lados do poligono
    :param n: quantidade de lados do poligono
    :return: retorna o desenho de um poligono
    """

    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    """

    :param t: objeto do tipo turtle
    :param r: raio do circulo
    :return: retorna a circunferência e o número de lados adequados
    """
    circ = 2 * 3.14159 * r
    polygon(t=t, length=int(circ/3.14159), n=int(50))


bob = turtle.Turtle()
circle(bob, 5)
turtle.mainloop()