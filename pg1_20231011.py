from gpiozero import LED, Button
import time

Resp=input('Ingrese color: ')
opcPar=input('Parpadear SI o NO:')

opc={'Verde':LED(17),'ROJO':LED(18),'AZUL':LED(19)}

while decision == 0:
    if Resp in opc:
        ledOp=opc(Resp)
        decision = 1
    else:
        Resp=input('Color incorrecto, ingrese otro: ')

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



