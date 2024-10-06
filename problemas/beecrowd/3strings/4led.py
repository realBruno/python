# LED
# 06/10/2024

for i in range(int(input())):
    val_led = input()
    leds = 0
    for j in range(len(val_led)):
        if int(val_led[j]) == 1:
            leds = leds + 2

        elif int(val_led[j]) == 2 or int(val_led[j]) == 3 or \
            int(val_led[j]) == 5:
            leds = leds + 5

        elif int(val_led[j]) == 0 or int(val_led[j]) == 6 or \
            int(val_led[j]) == 9:
            leds = leds + 6

        elif int(val_led[j]) == 2 or int(val_led[j]) == 3 or \
             int(val_led[j]) == 5:
            leds = leds + 5

        elif int(val_led[j]) == 4:
            leds = leds + 4

        elif int(val_led[j]) == 8:
            leds = leds + 7

        else:
            leds = leds + 3
    print(f'{leds} leds')