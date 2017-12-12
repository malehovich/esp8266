def connect():
    import network
    ssid = "maleha"
    password = "qazwsxedc"

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Connection successful")
    print(station.ifconfig())

def ip():
    import network
    station = network.WLAN(network.STA_IF)
    ip = station.ifconfig()
    return str(ip[0])


def mac():
    import network
    import ubinascii
    from network import WLAN
    mac = ubinascii.hexlify(WLAN().config('mac'), ':').decode()
    return str(mac)
