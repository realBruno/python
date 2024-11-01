words = input().split()
dancing_word, dancing_words = '', []

for word in words:
    for i in range(len(word)):
        if i % 2 == 0:
            dancing_word += word[i].upper()
        else:
            dancing_word += word[i].lower()

    dancing_words.append(dancing_word)
    dancing_word = ''

sentence = ' '.join(dancing_words)
print(sentence)