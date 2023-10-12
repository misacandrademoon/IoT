from gpiozero import LED, Button
import time
# import random
# import threading


led_Gr=LED(17)
# self.led_Blue = LED(led_io)
# self.led_Red = LED(led_io)

while True:
    led_Gr.on()
    time.sleep(1)
    led_Gr.off()
    time.sleep(1)




