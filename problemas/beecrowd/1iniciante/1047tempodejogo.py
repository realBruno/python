# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
# A seguir calcule a duração do jogo.

# 7 7 7 7

hi, mi, hf, mf = map(int, input().split())

hora_total = ...
minuto_total = mf - mi if mf >= mi else 60 + mf - mi

print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')