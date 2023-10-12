from gpiozero import LED, Button
import time
# import random
# import threading

Resp=input('Ingrese color: ')
opcPar=input('Parpadear SI o NO:')

opc={'Verde':LED(17),'ROJO':LED(18),'AZUL':LED(19)}
ledOp=opc(Resp)

# self.led_Blue = LED(led_io)
# self.led_Red = LED(led_io)

while True:
    if opcPar == 'SI':
        ledOp.on()
        time.sleep(1)
        ledOp.off()
        time.sleep(1)
    else:
        ledOp.on()



