"""
5. Faça uma versão mais geral do circle chamada arc, que receba um parâmetro
adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle
está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo
completo.

"""

import turtle


def polygon(t, length, n, ang):
    """
    :param ang: define quanto do desenho será desenhado
    :param t: objeto do tipo turtle
    :param length: comprimento dos lados do poligono
    :param n: quantidade de lados do poligono
    :return: retorna o desenho de um poligono
    """

    for i in range(n):
        t.fd(length)
        t.lt(ang/n)

def arc(t, r, angle):
    """

    :param t: objeto do tipo turtle
    :param r: raio do circulo
    :param angle: define quanto do desenho será desenhado
    :return: retorna a circunferência e o número de lados adequados
    """
    circ = 2 * 3.14159 * r
    n = 100
    polygon(t=t, length=circ/n, n=int(n), ang=angle)


bob = turtle.Turtle()
arc(bob, 10, 180)
turtle.mainloop()