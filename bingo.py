import random

print('Escolha o modo desejado:\n 0: Modo rápido\n 1: Modo demorado')
difficulty = int(input())
playercount = int(input())

match difficulty:
    case 0:
        cartelas = []
        for _ in range(playercount):
            appender = []
            for __ in range(2):
                moreappender = []
                for ranging in range(1, 31, 10):
                    moreappender.append(random.randint(ranging, ranging + 10))
                print(moreappender)
                appender.append(moreappender)

    case 1:
        pass
 
print(cartelas)