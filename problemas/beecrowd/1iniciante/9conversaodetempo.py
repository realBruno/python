# Conversão de tempo
# 01/11/2024

total = int(input())

horas = total//3600
minutos = (total % 3600) // 60
segundos = (total % 3600) % 60
print(f'{horas}:{minutos}:{segundos}')