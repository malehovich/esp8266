from network import WLAN
import ubinascii
import network

ssid = "tit"
password = "qazwsxedc"

station = network.WLAN(network.STA_IF)

if station.isconnected() == True:
    print("Already connected")



while station.isconnected() == False:
   station.active(True)
   station.connect(ssid, password)

print("Connection successful")
s = station.ifconfig()
macAddress = WLAN().config('mac')
binaryToAscii = ubinascii.hexlify(WLAN().config('mac'),':')
mac=ubinascii.hexlify(WLAN().config('mac'),':').decode()
print(mac)
print(s[0])

