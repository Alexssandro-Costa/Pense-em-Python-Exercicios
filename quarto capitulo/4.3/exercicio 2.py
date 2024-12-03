"""
2. Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o
comprimento dos lados seja length e então altere a chamada da função para fornecer
um segundo argumento. Execute o programa novamente. Teste o seu programa com
uma variedade de valores para length.
"""

import turtle


def square(t, length):
    """
    :param t: objeto do tipo turtle
    :param length: comprimento dos lados do quadrado
    :return: retorna o desenho de um quadrado
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

L = 50
bob = turtle.Turtle()
square(bob, L)
turtle.mainloop()