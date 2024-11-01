sentence = input()
dancing = ''
toggle = True

for i in range(len(sentence)):
    if sentence[i] == ' ':
        dancing += sentence[i]
        toggle = not toggle
    else:
        if toggle:
            dancing += sentence[i].upper()
        else:
            dancing += sentence[i].lower()
    toggle = not toggle
print(dancing)