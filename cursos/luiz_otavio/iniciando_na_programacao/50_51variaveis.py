# variáveis, constantes e complexidade de código
# 02/10/2024

# constantes são variáveis que não vão mudar
# são definidas por letras maiúsculas

velocidade = 61
local_carro = 100

RADAR_1 = 60 # velocidade máxima permitida pelo radar
LOCAL_1 = 100 # local do radar
RADAR_RANGE = 1 # range de captura do radar

VEL_RANGE_RADAR = velocidade > RADAR_1
MULTAR_CARRO = local_carro >= LOCAL_1 - 1 and local_carro <= LOCAL_1 + 1

if VEL_RANGE_RADAR and MULTAR_CARRO:
        print('O carro passou da velocidade e foi multado.')