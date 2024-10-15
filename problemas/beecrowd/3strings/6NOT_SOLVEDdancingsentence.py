# Dancing Sentence
# 09/10/2024

# Decidi tentar este problema só para não quebrar a streak, pois estou muito
# cansado hoje.

string = input()

sentences = string.split()

new_sentence = ''
final_sentence = []

for sentence in sentences:
    if sentences.index(sentence) % 2 == 0:
        for i in range(len(sentence)):
            if i % 2 == 0:
                new_sentence += sentence[i].upper()
            else:
                new_sentence += sentence[i].lower()
    else:
        for i in range(len(sentence)):
            if i % 2 == 0:
                new_sentence += sentence[i].lower()
            else:
                new_sentence += sentence[i].upper()
    final_sentence.append(new_sentence)
    new_sentence = ''

final_sentence = ' '.join(map(str, final_sentence))
print(final_sentence)