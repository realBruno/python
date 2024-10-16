# Dancing Sentence
# 15/10/2024

# Decidi fazer uma segunda versão do código anterior, pois não o vejo a tanto
# tempo que estou com preguiça de tentar entender o que escrevi
# update: não faço a menor ideia de como fazer isso funcionar.

dancingSentences = []
originalSentences = []

while True:
        userInput = input()
        if userInput == '':
            break

        originalSentences.append(userInput)
        userInput = userInput.replace(' ', '')
        
        dancing_sentence = ''
        
        for i in range(len(userInput)):
            if i % 2 == 0:
                dancing_sentence += userInput[i].upper()
            else:
                dancing_sentence += userInput[i].lower()
        dancingSentences.append(dancing_sentence)
        
print(lista)

for dancingSentence in dancingSentences:
    print(sentence)
