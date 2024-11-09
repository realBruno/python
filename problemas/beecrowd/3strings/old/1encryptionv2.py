# Encryption (v2)
# 22/10/2024

palavras = []
for i in range(int(input())):
    palavra, formatada = input(), ''
    
    for letra in palavra:
        if ord(letra) in range(65, 91) or ord(letra) in range(97, 123):
            formatada += chr(ord(letra) + 3)
        else:
            formatada += letra
    
    formatada = formatada[::-1]
    palavra = formatada[:len(formatada)//2]

    for letra in formatada[len(formatada)//2:]:
        palavra += chr(ord(letra) - 1)
    
    palavras.append(palavra)

for palavra in palavras:
    print(palavra)
    