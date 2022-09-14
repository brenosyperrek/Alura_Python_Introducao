import random

def jogar():
    print("*********************************")
    print("*Bem vindo ao Jogo de Adivinhção*")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    dificuldade = int(input("Escolha o nível de dificuldade. (1) Fácil (2) Médio (3) Difícil:"))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range (1,total_de_tentativas + 1):
        print("Tentativa {} de {}.".format(tentativa, total_de_tentativas))
        chute_str = input("Digite o seu palpite entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100! Perdeu uma rodada...")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Voce digitou {} e acertou. Parabéns".format(chute))
            print("Você fez {} pontos".format(pontos))

            break
        else:
            if (maior):
                print ("Você digitou {} e errou. Seu palpite é maior que o núnero secreto.".format(chute))
            elif (menor):
                print("Você digitou {} e errou. Seu palpite é menor que o núnero secreto.".format(chute))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    if (not acertou):
        print ("Você errou todas as tentativas. O número secreto era {}".format(numero_secreto))

    print("O jogo acabou. Zefini")

if(__name__ == "__main__"):
    jogar()
