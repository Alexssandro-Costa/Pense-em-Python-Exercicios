"""
3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro
chamado n e altere o corpo para que desenhe um polígono regular de n lados.
Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.
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

bob = turtle.Turtle()
polygon(t=bob, length=50 , n=3)
turtle.mainloop()