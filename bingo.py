# ANOTAÇÕES:
# código feito pelo aluno Lucas Gabriel da Silva Duarte (20241011110026)
# eu fiz tudo sozinho e de uma vez só
# (por causa da junção da quantidade de trabalhos, provas e procrastinação nessa semana)
# enfim, tá feito e no github.

import random
import copy
import time

print('Escolha o modo desejado:\n 0: Modo rápido\n 1: Modo demorado')
difficulty = int(input())
playercount = int(input('Digite a quantidade de jogadores: '))

match difficulty:
    case 0:
        numbers = [i for i in range(1, 31)]
        drawnnumbers = []
        cards = []
        for _ in range(playercount):
            playercard = []
            for __ in range(2):
                cardappender = []
                used_numbers = set()
                for ___ in range(2):
                    cellappender = []
                    for ranging in range(1, 31, 10):
                        while True:
                            number = random.randint(ranging, ranging + 10)
                            if number not in used_numbers:
                                cellappender.append(number)
                                used_numbers.add(number)
                                break
                    cardappender.append(cellappender)
                playercard.append(cardappender)
            cards.append(playercard)

        cardscopy = copy.deepcopy(cards)

        for player_index, player in enumerate(cards, start=1):
            print(f'\nCartelas do jogador {player_index}:')
            time.sleep(1)
            for playercard_index, playercard in enumerate(player, start=1):
                print(f' Cartela {playercard_index}: ')
                for row in playercard:
                    print('  ', end='')
                    for cell in row:
                        print(f'{cell:02d}', end=' ')
                    print()
                time.sleep(1)

    case 1:
        numbers = [i for i in range(1, 41)]
        drawnnumbers = []
        cards = []
        for _ in range(playercount):
            playercard = []
            for __ in range(2):
                cardappender = []
                used_numbers = set()
                for ___ in range(3):
                    cellappender = []
                    for ranging in range(1, 41, 10):
                        while True:
                            number = random.randint(ranging, ranging + 10)
                            if number not in used_numbers:
                                cellappender.append(number)
                                used_numbers.add(number)
                                break
                    cardappender.append(cellappender)
                playercard.append(cardappender)
            cards.append(playercard)

        cardscopy = copy.deepcopy(cards)

        for player_index, player in enumerate(cards, start=1):
            print(f'\nCartelas do jogador {player_index}:')
            time.sleep(1)
            for playercard_index, playercard in enumerate(player, start=1):
                print(f' Cartela {playercard_index}: ')
                for row in playercard:
                    print('  ', end='')
                    for cell in row:
                        print(f'{cell:02d}', end=' ')
                    print()
                time.sleep(1)

# Lista para controlar cartelas que já venceram
winners = []

while numbers:
    chosennumber = random.choice(numbers)
    print(f"\nNúmero sorteado: {chosennumber}")
    drawnnumbers.append(chosennumber)
    print(f"Números sorteados anteriormente: {drawnnumbers}")
    print(f"Lista restante: {numbers}")

    for player in cards:
        for playercard in player:
            for row in playercard:
                for cell_index, cell in enumerate(row):
                    if cell == chosennumber:
                        row[cell_index] = 'XX'

    for player_index, player in enumerate(cards, start=1):
        print(f'\nCartelas do jogador {player_index}:')
        for playercard_index, playercard in enumerate(player, start=1):
            print(f' Cartela {playercard_index}: ')
            for row in playercard:
                print('  ', end='')
                for cell in row:
                    print(f'{cell:>2}', end=' ')
                print('\n', end='')

    numbers.remove(chosennumber)
    time.sleep(2)

    for player_index, player in enumerate(cards, start=1):
        for card_index, playercard in enumerate(player, start=1):
            if (player_index, card_index) not in winners:
                if all(cell == 'XX' for row in playercard for cell in row):
                    winners.append((player_index, card_index))

    if winners:
        print("\n--- BINGO! CARTELAS VENCEDORAS ---")
        for p_index, c_index in winners:
            print(f"\nCartela {c_index} do Jogador {p_index}:")
            for row in cardscopy[p_index - 1][c_index - 1]:
                print(' ', end='')
                for cell in row:
                    print(f'{cell:02d}', end=' ')
                print('\n', end='')
        exit()