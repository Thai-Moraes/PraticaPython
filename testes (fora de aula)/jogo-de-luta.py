import random
import time
import os
nome = input("Qual o seu nome? ").upper()

ataques = {1 : ['Ataque Fraco', 10, 3], 2 : ['Ataque Forte', 25, 10], 3 : ['Soquinho', 3, 0]}
ataques_rival = {1 : ['Ataque Congelante', 15, 4], 2 : ['Ataque Supremo', 30, 15], 3 : ['Chute Fraco', 4, 0]}

vida_total = 150
vida = vida_total
vida_rival = vida_total

energia_total = 50
energia = energia_total
energia_rival = energia_total

def Luta():

    global vida
    global vida_total
    global vida_rival

    global energia
    global energia_rival
    global energia_total

    while vida <= 0 or vida_rival <= 0:
        if vida <= 0:
            novamente = input("\nVOCÊ PERDEU! TENTAR NOVAMENTE? (S/N): ")
            if novamente == 's' or novamente == 'S':
                vida = vida_rival = vida_total
                energia = energia_rival = energia_total
            else:
                exit()

        elif vida_rival <= 0:
            novamente = input("\nVOCÊ GANHOU! TENTAR NOVAMENTE? (S/N): ")
            if novamente == 's' or novamente == 'S':
                vida = vida_rival = vida_total
                energia = energia_rival = energia_total
            else:
                exit()

    print(f'\n{nome}: \nVida: {vida}/{vida_total}\nEnergia: {energia}/{energia_total}\nAtaques: {ataques[1][0]}, {ataques[2][0]}, {ataques[3][0]}')


    print(f'\nSUBZERO: \nVida: {vida_rival}/{vida_total}\nEnergia: {energia_rival}/{energia_total}\nAtaques: {ataques_rival[1][0]}, {ataques_rival[2][0]}, {ataques_rival[3][0]}')

    ataque_esc = int(input(f'\n[SELECIONE SEU ATAQUE!]\n1. {ataques[1][0]}\n2. {ataques[2][0]}\n3. {ataques[3][0]}\n'))

    ataque_esc_rival = random.choice([1,3])

    esquiva = random.choice([1,50])
    esquiva_rival = random.choice([1,50])

    if esquiva <= 10:
        print(f'\n{nome.upper()} DESVIOU DE {ataques_rival[ataque_esc_rival][0].upper()}!')
    if esquiva_rival <= 10:
        print(f'\nSUBZERO DESVIOU DE {ataques[ataque_esc][0].upper()}!')

    if esquiva > 10:
        vida = vida - ataques_rival[ataque_esc_rival][1]
        energia = energia - ataques_rival[ataque_esc_rival][2]
        print(f'\n{nome.upper()} FOI ATINGIDO POR {ataques_rival[ataque_esc_rival][0].upper()}!')
    if esquiva_rival > 10:
        vida_rival = vida_rival - ataques[ataque_esc][1]
        energia_rival = energia_rival - ataques[ataque_esc][2]
        print(f'\nSUBZERO FOI ATINGIDO POR {ataques[ataque_esc][0].upper()}!')

    time.sleep(3)

    os.system('cls')

    return 0

if __name__ == '__main__':
    while True:
        Luta()








