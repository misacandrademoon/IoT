from gpiozero import LED, Button
import time
import psutil

Verde=LED(17)
Rojo=LED(18)
Azul=LED(19)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    
    if cpu_percent<=10:
        Verde.on()
        Rojo.off()
        Azul.off()
    if cpu_percent>10 and cpu_percent<=20:
        Verde.off()
        Rojo.on()
        Azul.off()
    if cpu_percent>20:
        Verde.off()
        Rojo.off()
        Azul.on()
