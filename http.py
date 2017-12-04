def get(url):
    import urequests
    print (url)
    response = urequests.get(url)
    print(response.text)
    return (response.text)
print ('gello')
