from time import sleep
from machine import Pin
from dht import DHT22



sensor = DHT22(Pin(2, Pin.IN, Pin.PULL_UP))  # DHT-22 on GPIO 15 (input with internal pull-up resistor)
import wifi
wifi.connect()
sost=2
import driver
driver.step(-1,3400,600,12,13,4,5)
sost=0

while True:
    try:
        sensor.measure()  # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            print(msg)
            url='http://192.168.88.100/objects/?script=espdata&mac=' + wifi.mac() + '&ip=' + wifi.ip()+'&h='+str(h)+'&t='+str(t)
            import http
            tmust=http.get(url)
            print(tmust)
            print(sost)
            if (float(tmust)<t) and (sost!=0):
                driver.step(-1,3400,600,12,13,4,5)
                sost=0
            if (float(tmust)>t) and (sost!=1) :
                driver.step(1,3400,600,12,13,4,5)
                sost=1

        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(15)
