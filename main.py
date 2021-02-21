from machine import Pin
from time import sleep, sleep_ms
#from time import sleep_ms


d5=Pin(14,Pin.OUT)
d6=Pin(15,Pin.OUT)

def bk():
    t=1
    while t<10:
        d5.on()
        d6.off()
        sleep_ms(40)
        d5.off()
        d6.on()
        sleep_ms(40)
        t=t+1
    d5.off()
    d6.off()