import random
nome = input("Qual o seu nome? ").upper()

ataques = {1 : ['Ataque Fraco', 10, 3], 2 : ['Ataque Forte', 25, 10], 3 : ['Chute Atordoante', 5, 2]}
ataques_rival = {1 : ['Ataque Congelante', 15, 4], 2 : ['Ataque Supremo', 35, 14], 3 : ['Chute Fraco', 7, 4]}

vida_total = 150
vida = vida_total
vida_rival = vida_total

energia_total = 30
energia = energia_total
energia_rival = energia_total

print(f'\n{nome}: \nVida: {vida}/{vida_total}\nEnergia: {energia}/{energia_total}\nAtaques: {ataques[1][0]}, {ataques[2][0]}, {ataques[3][0]}')


print(f'\nSUBZERO: \nVida: {vida_rival}/{vida_total}\nEnergia: {energia_rival}/{energia_total}\nAtaques: {ataques_rival[1][0]}, {ataques_rival[2][0]}, {ataques_rival[3][0]}')

ataque_esc = int(input(f'\n[SELECIONE SEU ATAQUE!]\n1. {ataques[1][0]}\n2. {ataques[2][0]}\n3. {ataques[3][0]} '))

