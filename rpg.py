import random
jogador1 = input("Informe o nome do jogador 1: ")
jogador2 = input("Informe o nome do jogador 2: ")

vidaJogador1 = 100
vidaJogador2 = 100

quemInicia = random.randint(1,2)
turnoAtual = quemInicia
escolhajogador = random.randint(1,2)
escolhaOponente = random.randint(1,2)

print(f"O jogador que inicia é o jogador{quemInicia}, cujo nome é {jogador1}, e seu oponente é {jogador2}")

def ataque(vida):
    return vida - 30

def cura(vida):
    return vida + 10

while vidaJogador1 >= 0 and vidaJogador2 >= 0:
    turnoAtual = input(
        "Escolha uma ação:\n"
        "(1) - Ataque\n"
        "(2) - Cura\n"
        "(3) - Sair\n"
    )

    if turnoAtual == "1":
        print(f'o {jogador1} está fazendo um ataque')
        vidaJogador2 = ataque(vidaJogador2)
        print("Vida do jogador 2:", vidaJogador2)

    elif turnoAtual == "2":
        print(f'o {jogador1} está se curando')
        vidaJogador1 = cura(vidaJogador1)
        print("Vida do jogador 1:", vidaJogador1)

    elif turnoAtual == "3":
        print(f'o {jogador1} saiu do jogo')
        print("Saindo do jogo...")
        break
    else:
        vidaJogador2 > 0
        print(f'O jogador {vidaJogador1} ganhou')
        break

    acaoOponente = random.randint(1, 2)

    if acaoOponente == 1:
        print(f'o {jogador2} está fazendo um ataque')
        vidaJogador1 = ataque(vidaJogador1)
        print("Vida do jogador 1:", vidaJogador1)
    
    elif acaoOponente == 2:
        print(f'o {jogador2} está se curando')
        vidaJogador2 =  cura(vidaJogador2)
        print("vida do jogador 2:", vidaJogador2)

    elif acaoOponente == 3:
        print(f'o {jogador2} saiu do jogo')
        print("Saindo do jogo...")
        break
    
    else:
        vidaJogador1 > 0
        print(f'O jogador {vidaJogador2} ganhou')
        break


