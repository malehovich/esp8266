from machine import Pin
import time

LOW = 0
HIGH = 1

HALF_STEP = [
    [LOW, LOW, LOW, HIGH],
    [LOW, LOW, HIGH, HIGH],
    [LOW, LOW, HIGH, LOW],
    [LOW, HIGH, HIGH, LOW],
    [LOW, HIGH, LOW, LOW],
    [HIGH, HIGH, LOW, LOW],
    [HIGH, LOW, LOW, LOW],
    [HIGH, LOW, LOW, HIGH],
]

def step(direction,count,tim,pn1,pn2,pn3,pn4):

    for x in range(count):
        for bit in HALF_STEP[::direction]:
            p1 = Pin(pn1, Pin.OUT, value=bit[0])
            p1 = Pin(pn2, Pin.OUT, value=bit[1])
            p1 = Pin(pn3, Pin.OUT, value=bit[2])
            p1 = Pin(pn4, Pin.OUT, value=bit[3])
            time.sleep_us(tim)
    p1 = Pin(pn1, Pin.OUT, value=0)
    p2 = Pin(pn2, Pin.OUT, value=0)
    p3 = Pin(pn3, Pin.OUT, value=0)
    p4 = Pin(pn4, Pin.OUT, value=0)

