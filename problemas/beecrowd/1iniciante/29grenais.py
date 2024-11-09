# Grenais
# 09/11/2024

# Sometimes I forget I should be naming things in English

inter, gremio = map(int, input().split())
counter = 1
iwins, gwins, draws = 0, 0, 0
toggle = True

while toggle:
    grenais = int(input('Novo grenal (1-sim 2-nao)\n'))
    
    if grenais != 2:
        
        inter, gremio = map(int, input().split())
        counter += 1
        if inter > gremio:
            iwins += 1
        elif inter < gremio:
            gwins += 1
        else:
            draws += 1
    else:
        if inter > gremio:
            iwins += 1
        elif inter < gremio:
            gwins += 1
        else:
            draws += 1

        toggle = False

if iwins > gwins:
    winner = 'Inter venceu mais'
elif gwins > iwins:
    winner = 'Gremio venceu mais'
else:
    winner = 'Nao houve vencedor'

print(f"""{counter} grenais
Inter:{iwins}
Gremio:{gwins}
Empates:{draws}
{winner}""")
