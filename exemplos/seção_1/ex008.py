import os
os.system('cls' if os.name == 'nt' else 'clear')

velocidade = 60
local_do_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passa_radar = velocidade > RADAR_1
carro_passou_radar_1 = local_do_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_do_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = velocidade_carro_passa_radar and carro_passou_radar_1

if velocidade_carro_passa_radar:
    print(
        f'O carro está a uma velocidade de {velocidade} km/h passando da velocidade do radar de {RADAR_1} km/h')

if carro_passou_radar_1:
    print(f'O carro passou pelo radar 1 com a velocidade de {velocidade} km/h')

if carro_multado_radar_1:
    print('O carro será multado')

else:
    print('O carro não será multado')
