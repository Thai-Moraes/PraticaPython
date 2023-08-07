import random
import time
import os

print(r"""
   _____                 __         .__     ____  __.            ___.           __
  /     \   ____________/  |______  |  |   |    |/ _|____   _____\_ |__ _____ _/  |_
 /  \ /  \ /  _ \_  __ \   __\__  \ |  |   |      < /  _ \ /     \| __ \\__  \\   __\
/    Y    (  <_> )  | \/|  |  / __ \|  |__ |    |  (  <_> )  Y Y  \ \_\ \/ __ \|  |
\____|__  /\____/|__|   |__| (____  /____/ |____|__ \____/|__|_|  /___  (____  /__|
        \/                        \/               \/           \/    \/     \/
                        """)

nome = input("Qual o seu nome?: ").upper()
personagens = {1 : ['Subzero'], 2 : ['Kitana'], 3: ['Scorpion']}

inimigo = int(input(f"\n\nQuem você deseja enfrentar?\n1. {personagens[1][0]} (Fácil)\n2. {personagens[2][0]} (Médio) \n3. {personagens[3][0]} (Difícil)\n"))

if inimigo == 1:
    ataques_rival = {1: ['Ataque Congelante', 13], 2: ['Chute Gelado', 15], 3: ['Chute Fraco', 3]}

if inimigo == 2:
    ataques_rival = {1: ['Ataque Assassino', 12], 2: ['Fan-Nado', 20], 3: ['Chute Fraco', 5]}

if inimigo == 3:
    ataques_rival = {1: ['Soco Alto', 15], 2: ['Corrente', 30], 3: ['Corte Alto', 7]}

ataques = {1 : ['Ataque Fraco', 10], 2 : ['Ataque Forte', 25], 3 : ['Soquinho', 3]}

vida_total = 150
vida = vida_total
vida_rival = vida_total

os.system('cls')

def Luta():

    global vida
    global vida_total
    global vida_rival

    while vida <= 0 or vida_rival <= 0:
        if vida <= 0:
            novamente = input("\nVOCÊ PERDEU! TENTAR NOVAMENTE? (S/N): ")
            if novamente == 's' or novamente == 'S':
                vida = vida_rival = vida_total
            else:
                exit()

        elif vida_rival <= 0:
            novamente = input("\nVOCÊ GANHOU! TENTAR NOVAMENTE? (S/N): ")
            if novamente == 's' or novamente == 'S':
                vida = vida_rival = vida_total
            else:
                exit()

    print(f'\n{nome}: \nVida: {vida}/{vida_total}\nAtaques: {ataques[1][0]}, {ataques[2][0]}, {ataques[3][0]}')


    print(f'\n{personagens[inimigo][0].upper()}: \nVida: {vida_rival}/{vida_total}\nAtaques: {ataques_rival[1][0]}, {ataques_rival[2][0]}, {ataques_rival[3][0]}')

    ataque_esc = int(input(f'\n[SELECIONE SEU ATAQUE!]\n1. {ataques[1][0]}\n2. {ataques[2][0]}\n3. {ataques[3][0]}\n'))

    ataque_esc_rival = random.choice([1, 2, 3])

    esquiva = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    esquiva_rival = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    if esquiva <= 2:
        print(f'\n{nome.upper()} DESVIOU DE {ataques_rival[ataque_esc_rival][0].upper()}!')
    if esquiva > 2:
        vida = vida - ataques_rival[ataque_esc_rival][1]
        print(f'\n{nome.upper()} FOI ATINGIDO POR {ataques_rival[ataque_esc_rival][0].upper()}!')

    if esquiva_rival <= 2:
        print(f'\n{personagens[inimigo][0].upper()} DESVIOU DE {ataques[ataque_esc][0].upper()}!')
    if esquiva_rival > 2:
        vida_rival = vida_rival - ataques[ataque_esc][1]
        print(f'\n{personagens[inimigo][0].upper()} FOI ATINGIDO POR {ataques[ataque_esc][0].upper()}!')

    time.sleep(3)

    os.system('cls')

    return 0

if __name__ == '__main__':
    while True:
        Luta()








