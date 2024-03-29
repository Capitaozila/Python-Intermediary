import os

palavra_secreta = 'vasco'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''.join([letra_secreta if letra_secreta in letras_acertadas else '*' for letra_secreta in palavra_secreta])

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('VOCÊ GANHOU! PARABÉNS!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'Número de tentativas: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0
