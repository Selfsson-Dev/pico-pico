from machine import Pin
import utime

led1 = Pin(28,Pin.OUT)
led2 = Pin(27,Pin.OUT)
led3 = Pin(26,Pin.OUT)
led4 = Pin(22,Pin.OUT)
led5 = Pin(21,Pin.OUT)
delay = .15

while True:
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    
    utime.sleep(delay)
    
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    led5.value(0)

    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    led5.value(0)

    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    led5.value(0)

    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(1)

    utime.sleep(delay)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)