from helpers import gerar_palavra_secreta, jogo

if __name__ == '__main__':

    palavra_secreta = gerar_palavra_secreta()
    # for looping que imprime a palavra escolhida
    print(f"\n = = = JOGO DA FORCA = = = ")
    print("\n Palavra é: ")
    for letra in palavra_secreta:
        print("*", end = " ")

    # Calculando o tamanho da palavra
    tamanho_palavra = len(palavra_secreta)
    print(f"\n - Palavra tem {tamanho_palavra} letras")

    jogo(palavra_secreta)