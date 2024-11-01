# Dancing Sentence
# 15/10/2024, 31/10/2024

word = input()
wordlist = word.split()
word = word.replace(' ', '')
dancing_word, d_sentence = '', ''
y = 0

for i in range(len(word)):
    if i % 2 == 0:
        dancing_word += word[i].upper()
    else:
        dancing_word += word[i].lower()

for item in wordlist:
    for i in range(len(item)):
        d_sentence += dancing_word[i + y]
    y = len(item) + y
    
    d_sentence += ' '

d_sentence = d_sentence.strip()
print(d_sentence)