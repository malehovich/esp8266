def get(url):
    import urequests
    response = urequests.get(url)
    return (response.text)

