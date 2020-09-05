import random

from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS

def gerar_palavra_secreta():
    """
    Função que seleciona randomicamente uma palavra do arquivo texto
    :return: Uma palavra aleatória
    """
    with open(ARQUIVO_PALAVRAS_SECRETAS, 'r') as f_obj:
        palavra = f_obj.read().splitlines()
    return random.choice(palavra)


def verificar_letra_informada(palavra_secreta,suas_tentativas,tentativa):
    """
    Verifica se a letra informada está correta com base no arquivo
    :param palavra_secreta:
    :param suas_tentativas:  tentaivas feitas para acertar a palavra
    :param tentativas: numero de vezes que o usuario tem para acertar
    :return: retorna um status
    """
    status = ''
    acertos = 0
    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
        else:
            status += '*'
        if letra.lower() == tentativa.lower():
             acertos +=1

    print(f"\n - Acertou {acertos} letra(s) '{tentativa}' ")
    return status

def total_tentativas(palavra_secreta):
    """
    Define a quantidade de tentativas de acordo com a palavra definida
    :param palavra_secreta: 
    :return: O numero de vezes utilizados
    """
    chances = len(palavra_secreta)

    return chances + TENTATIVAS_ADICIONAIS

def jogo(palavra_secreta):
    """
    Função principal do jogo, para definir a palavra escolhida e seguir as regras definidas
    :param palavra: 
    :return: Retorna a palavra escolhida
    """
    chute = 0
    adivinhando = False
    suas_tentativas = [] # incluir a letra já testada anteriormente
    chances = total_tentativas(palavra_secreta)
    total_chances = chances
    print(f" - Total de chances: {chances}")

    while chute < total_chances:
        letra_tentativa = input("\n Entre com a sua primeira letra: ")
        # abaixo, diminuindo as chances de um em um
        chances -= 1

        #Se a letra ja foi informada ou adivinhada
        if letra_tentativa in suas_tentativas:
            print(f" * * * ATENCAO * * * voce já tentou essa letra !!! ")
        elif len(letra_tentativa) == 1:
            # add a letra ao lugar correto
            suas_tentativas.append(letra_tentativa)
            resultado = verificar_letra_informada(palavra_secreta, suas_tentativas, letra_tentativa)
            if resultado == palavra_secreta:
                  adivinhando = True
                  print(f"Parabéns, você venceu o jogo !!! a palavra é: {palavra_secreta}")
                  break
            else:
                  print(f" - {' '.join(resultado)}")
        else:
            print(f" Entrada incorreta, informe apenas 1(uma) letra")

         # mostra as tentativas restantes
        print(f"\nTentativas restantes: {chances}")
        chute +=1
    if chute == total_chances:
        print(f"\n *** Suas Tentativas acabaram. A palavra secreta é: {palavra_secreta}")

