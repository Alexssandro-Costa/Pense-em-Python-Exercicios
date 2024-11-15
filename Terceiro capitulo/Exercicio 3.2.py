"""
Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como
argumento. Por exemplo, do_twice é uma função que toma um objeto de função como
argumento e o chama duas vezes:
def do_twice(f):
    f()
    f()
Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam
duas vezes:
def print_spam():
    print('spam')
do_twice(print_spam)
1. Digite este exemplo em um script e teste-o.
2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
chame a função duas vezes, passando o valor como um argumento.
3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu
script.
4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
'spam' como um argumento.
5. Defina uma função nova chamada do_four que receba um objeto de função e um
valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
haver só duas afirmações no corpo desta função, não quatro.
"""

# 1. Digite este exemplo em um script e teste-o.

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)

# 2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
# chame a função duas vezes, passando o valor como um argumento.

def do_twice(f, a):
    f(a)
    f(a)

def print_spam(a):
    print(a)

do_twice(print_spam, "spam")

# 3. Copie a definição de print_twice que aparece
# anteriormente neste capítulo no seu script.


def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice(42)

# 4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
# 'spam' como um argumento.

def do_twice(f, a):
    f(a)
    f(a)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, "spam")

#5. Defina uma função nova chamada do_four que receba um objeto de função e um
#valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
#haver só duas afirmações no corpo desta função, não quatro.

def do_four(o, v):
    o(v)
    o(v)

do_four(print_twice, "spam")