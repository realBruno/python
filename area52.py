sentence = input()
dancing = ''
for i in range(len(sentence)):
    if i % 2 == 0:
        dancing += sentence[i].upper()
    else:
        dancing += sentence[i].lower()

print(dancing)