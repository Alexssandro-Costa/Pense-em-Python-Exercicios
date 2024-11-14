"""
Exercício 2.2
Pratique o uso do interpretador do Python como uma calculadora:
1. O volume de uma esfera com raio r é 4/3 pi r³. Qual é o volume de uma esfera com raio
5?
2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por
quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa
para o café da manhã?

"""


# 1:
esfera = 4/3 * 3.14 * 5 ** 3 # calcula o volume de uma esfera de raio 5
print({esfera})

# 2:
livro = (24.95 * 0.60 * 60) # calcula o valor de 60 livros com 40% de desconto
frete = 3 + (59 * 0.75)  # calcula o valor total do frete
print(livro + frete)

# 3:
tempoKm= (8.15 * 2) + (7.12 * 3) # calcula a quantidade de minutos passados
hora_inicial =  6.0
minutos_inicias = 52

minutos_finais = (tempoKm + minutos_inicias) % 60 # calcula os minutos totais
hora_final = hora_inicial + (minutos_inicias + tempoKm) // 60 # calcula o valor em horas
print(hora_final+ (minutos_finais / 100))