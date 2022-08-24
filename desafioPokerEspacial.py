import random

class Carta:
    naipe = 0
    numero = 0


#Funções para verificação de combinações
def verificarCartaMaisAlta(combinacao = Carta()):
    numerosCartas = []
    cartaMaior = 0

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for i in range(0,len(numerosCartas)-1):
        if numerosCartas[i] > cartaMaior:
            cartaMaior = numerosCartas[i]

    return cartaMaior


def verificarPar(combinacao = Carta()):
    numerosCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for numero in numerosCartas:
        if numerosCartas.count(numero) == 2:
            return True

    return False



def verificarDoisPares(combinacao = Carta()):
    numerosCartas = []
    qtdPares = 0

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for numero in numerosCartas:
        if numerosCartas.count(numero) == 2:
            qtdPares+=1

    if qtdPares == 4:
        return True

    return False



def verificarTrio(combinacao = Carta()):
    numerosCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for numero in numerosCartas:
        if numerosCartas.count(numero) == 3:
            return True

    return False



def verificarStraight(combinacao = Carta()):

    numerosCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    # Verificando se na combinação existem 5 cartas seguidas
    for i in range(0,3):
        if (numerosCartas[i]+1) == numerosCartas[i+1] and (numerosCartas[i]+2) == numerosCartas[i+2] and (
                numerosCartas[i]+3) == numerosCartas[i+3] and (numerosCartas[i]+4) == numerosCartas[i+4]:
            return True

    return False



def verificarFlush(combinacao = Carta()):
    naipesCartas = []

    for carta in combinacao:
        naipesCartas.append(carta.naipe)

    for naipe in naipesCartas:
        if naipesCartas.count(naipe) >= 5:
            return True

    return False



def verificarFullHouse(combinacao = Carta()):
    numerosCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for i in range(0,len(numerosCartas)-1):
        if numerosCartas.count(numerosCartas[i]) == 3:
            continue

    return False



def verificarQuadra(combinacao = Carta()):
    numerosCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for numero in numerosCartas:
        if numerosCartas.count(numero) > 3:
            return True

    return False


def verificarStraightFlush(combinacao = Carta()):
    numerosCartas = []
    naipesCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for carta in combinacao:
        naipesCartas.append(carta.naipe)

    # Verificando se na combinação existem 5 cartas seguidas
    for i in range(0, 3):
        if (numerosCartas[i] + 1) == numerosCartas[i + 1] and (numerosCartas[i] + 2) == numerosCartas[i + 2] and (
                numerosCartas[i] + 3) == numerosCartas[i + 3] and (numerosCartas[i] + 4) == numerosCartas[i + 4]:

            if naipesCartas[i] == naipesCartas[i+1] and naipesCartas[i] == naipesCartas[i+2] and naipesCartas[i] == naipesCartas[i+3] and naipesCartas[i] == naipesCartas[i+4]:
                return True

    return False



def verificarRoyalFlush(combinacao = Carta()):
    numerosCartas = []
    naipesCartas = []

    for carta in combinacao:
        numerosCartas.append(carta.numero)

    for carta in combinacao:
        naipesCartas.append(carta.naipe)

    # Verificando se na combinação existem 5 cartas seguidas
    for i in range(0, 3):
        if (numerosCartas[i] + 1) == numerosCartas[i + 1] and (numerosCartas[i] + 2) == numerosCartas[i + 2] and (
                numerosCartas[i] + 3) == numerosCartas[i + 3] and (numerosCartas[i] + 4) == numerosCartas[i + 4]:

            if numerosCartas[i] == 10:

                if naipesCartas[i] == naipesCartas[i + 1] and naipesCartas[i] == naipesCartas[i + 2] and naipesCartas[i] == \
                        naipesCartas[i + 3] and naipesCartas[i] == naipesCartas[i + 4]:
                    return True

    return False



def substituirLetraPorNumero(baralho = Carta()):
    for carta in baralho:
        if carta.numero == 11:
            carta.numero = 'A'
        elif carta.numero == 12:
            carta.numero = 'J'
        elif carta.numero == 13:
            carta.numero = 'Q'
        elif carta.numero == 14:
            carta.numero = 'K'



def gerarCarta():

    carta = Carta()

    carta.naipe = random.randint(1, 4) # Gerando naipe aleatorio

    # Convertendo naipe para seu respectivo caractere
    if carta.naipe == 1:
        carta.naipe = 'C'
    elif carta.naipe == 2:
        carta.naipe = 'E'
    elif carta.naipe == 3:
        carta.naipe = 'O'
    elif carta.naipe == 4:
        carta.naipe = 'P'

    carta.numero = random.randint(2, 14) #Gerando numero/letra aleatorio

    return carta



maoJogador1 = []
maoJogador2 = []
mesa = []


# Lógica para invalidar baralhos com cartas repetidas
# A cartaRepetida sempre começa em 1 e vai ser incrementada se o teste validar uma carta repetida.
# Se cartaRepetida não for incrementada no teste, validando assim o baralho sorteado, ela recebe 0 e sai do loop.

cartaRepetida = 1

while cartaRepetida > 0:

    maoJogador1 = []
    maoJogador2 = []
    mesa = []

    cartaRepetida = 1

    # Adicionando cartas aleatorias na MESA e na mao dos Jogadores

    for i in range(0,2):
        maoJogador1.append(gerarCarta())


    for i in range(0,2):
        maoJogador2.append(gerarCarta())


    for i in range(0,5):
        mesa.append(gerarCarta())


    baralho = maoJogador1+maoJogador2+mesa
    baralhoNumeros = []

    for i in range(0,len(baralho)):
        baralhoNumeros.append(baralho[i].numero)


    cont = 0
    naipesNumerosRepetidos = []


    for numero in baralhoNumeros:
        if baralhoNumeros.count(numero) > 1:
            naipesNumerosRepetidos.append(baralho[cont].naipe)
        cont += 1


    for naipe in naipesNumerosRepetidos:
        if naipesNumerosRepetidos.count(naipe) > 1:
            cartaRepetida+=1


    if cartaRepetida > 1:
        continue
    else:
        cartaRepetida = 0



print('Baralho sem repetições formado!')


combinacaoJogador1 = maoJogador1+mesa
combinacaoJogador2 = maoJogador2+mesa

# Ordenando combinações pelo número
combinacaoJogador1.sort(key= lambda Carta: Carta.numero)
combinacaoJogador2.sort(key= lambda Carta: Carta.numero)


# Verificando melhor combinação do jogador 1
pontuacaoJogador1 = 0
combinacaoFeitaJogador1 = 0

cartaMaisAltaJogador1 = verificarCartaMaisAlta(maoJogador1)

if verificarPar(combinacaoJogador1):
    pontuacaoJogador1 = 1
    combinacaoFeitaJogador1 = 'Par'

if verificarDoisPares(combinacaoJogador1):
    pontuacaoJogador1 = 2
    combinacaoFeitaJogador1 = 'Dois pares'

if verificarTrio(combinacaoJogador1):
    pontuacaoJogador1 = 3
    combinacaoFeitaJogador1 = 'Trio'

if verificarStraight(combinacaoJogador1):
    pontuacaoJogador1 = 4
    combinacaoFeitaJogador1 = 'Straight'

if verificarFlush(combinacaoJogador1):
    pontuacaoJogador1 = 5
    combinacaoFeitaJogador1 = 'Flush'

if verificarFullHouse(combinacaoJogador1):
    pontuacaoJogador1 = 6
    combinacaoFeitaJogador1 = 'Full house'

if verificarQuadra(combinacaoJogador1):
    pontuacaoJogador1 = 7
    combinacaoFeitaJogador1 = 'Quadra'

if verificarStraightFlush(combinacaoJogador1):
    pontuacaoJogador1 = 8
    combinacaoFeitaJogador1 = 'Straight flush'

if verificarRoyalFlush(combinacaoJogador1):
    pontuacaoJogador1 = 9
    combinacaoFeitaJogador1 = 'Royal flush'



# Verificando melhor combinação do jogador 2
pontuacaoJogador2 = 0
combinacaoFeitaJogador2 = 0

cartaMaisAltaJogador2 = verificarCartaMaisAlta(maoJogador2)

if verificarPar(combinacaoJogador2):
    pontuacaoJogador2 = 1
    combinacaoFeitaJogador2 = 'Par'

if verificarDoisPares(combinacaoJogador2):
    pontuacaoJogador2 = 2
    combinacaoFeitaJogador2 = 'Dois pares'

if verificarTrio(combinacaoJogador2):
    pontuacaoJogador2 = 3
    combinacaoFeitaJogador2 = 'Trio'

if verificarStraight(combinacaoJogador2):
    pontuacaoJogador2 = 4
    combinacaoFeitaJogador2 = 'Straight'

if verificarFlush(combinacaoJogador2):
    pontuacaoJogador2 = 5
    combinacaoFeitaJogador2 = 'Flush'

if verificarFullHouse(combinacaoJogador2):
    pontuacaoJogador2 = 6
    combinacaoFeitaJogador2 = 'Full house'

if verificarQuadra(combinacaoJogador2):
    pontuacaoJogador2 = 7
    combinacaoFeitaJogador2 = 'Quadra'

if verificarStraightFlush(combinacaoJogador2):
    pontuacaoJogador2 = 8
    combinacaoFeitaJogador2 = 'Straight flush'

if verificarRoyalFlush(combinacaoJogador2):
    pontuacaoJogador2 = 9
    combinacaoFeitaJogador2 = 'Royal flush'



#Substituindo números por suas letras equivalentes para apresentação do jogo
substituirLetraPorNumero(maoJogador1)
substituirLetraPorNumero(maoJogador2)
substituirLetraPorNumero(mesa)



print()
print('________________________________')
print('Mão Rôbo 1:')

for carta in maoJogador1:
    print(carta.numero,end='')
    print(carta.naipe)


print('________________________________')
print('Mão Rôbo 2:')

for carta in maoJogador2:
    print(carta.numero,end='')
    print(carta.naipe)


print('________________________________')
print('MESA:')

for carta in mesa:
    print(carta.numero,end='')
    print(carta.naipe)


print('________________________________')
print('Mão Rôbo 1 + MESA:')

for carta in combinacaoJogador1:
    print(carta.numero,end='')
    print(carta.naipe)


print('________________________________')
print('Mão Rôbo 2 + MESA:')

for carta in combinacaoJogador2:
    print(carta.numero,end='')
    print(carta.naipe)


print('________________________________')


if pontuacaoJogador1 > 0:
    print(f'O Rôbo 1 conseguiu um {combinacaoFeitaJogador1}!')
else:
    print('Infelizmente o Rôbo 1 não conseguiu nenhuma combinação.')


if pontuacaoJogador2 > 0:
    print(f'O Rôbo 2 conseguiu um {combinacaoFeitaJogador2}!')
else:
    print('Infelizmente o Rôbo 2 não conseguiu nenhuma combinação.')


if pontuacaoJogador1 > pontuacaoJogador2:
    print('O Robô 1 venceu!')
elif pontuacaoJogador2 > pontuacaoJogador1:
    print('O Rôbo 2 venceu!')
elif pontuacaoJogador2 == pontuacaoJogador1 and pontuacaoJogador1 != 0 and pontuacaoJogador2 != 0:
    print('A rodada empatou! As combinações dos rôbos são iguais.')


if pontuacaoJogador1 == 0 and pontuacaoJogador2 == 0:
    print('Como nenhum dos dois rôbos conseguiram uma combinação, vencerá o rôbo que tiver a carta mais alta. ')

    if cartaMaisAltaJogador1 > cartaMaisAltaJogador2:
        print('O Robô 1 venceu!')
    elif cartaMaisAltaJogador2 > cartaMaisAltaJogador1:
        print('O Rôbo 2 venceu!')
    elif cartaMaisAltaJogador1 == cartaMaisAltaJogador2:
        print('A rodada empatou! As maiores cartas dos rôbos são iguais')
