from gpiozero import LED, Button
import time


import psutil

cpu_percent = psutil.cpu_percent(interval=1)

Verde=LED(17)
Rojo=LED(18)
Azul=LED(19)


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