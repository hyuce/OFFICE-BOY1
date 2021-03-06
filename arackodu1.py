from gpiozero import Button, LED
from time import sleep

mr_2 = LED(17)
mr_1 = LED(27)
mr_e = LED(22)

ml_2 = LED(18)
ml_1 = LED(23)
ml_e = LED(24)

button_1 = Button(5)
button_2 = Button(6)
button_3 = Button(13)

button_4 = Button(19)
button_5 = Button(26)
button_6 = Button(12)
button_7 = Button(16)

while True:
    mr_1.on()
    mr_2.off()
    mr_e.off()

    ml_1.on()
    ml_2.off()
    ml_e.off()

    if button_4.is_pressed == 1 and button_5.is_pressed == 1:
        while not button_6.is_pressed == 1 or not button_7.is_pressed == 1:
            if button_1.is_pressed and not button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.off()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and not button_2.is_pressed and button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.off()

    if button_4.is_pressed == 0 and button_5.is_pressed == 1:
        while not button_6.is_pressed == 0 or not button_7.is_pressed == 1:
            if button_1.is_pressed and not button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.off()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and not button_2.is_pressed and button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.off()

    if button_4.is_pressed == 1 and button_5.is_pressed == 0:
        while not button_6.is_pressed == 1 or not button_7.is_pressed == 0:
            if button_1.is_pressed and not button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.off()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and button_2.is_pressed and not button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.on()

            if not button_1.is_pressed and not button_2.is_pressed and button_3.is_pressed:
                mr_1.on()
                mr_2.off()
                mr_e.on()

                ml_1.on()
                ml_2.off()
                ml_e.off()