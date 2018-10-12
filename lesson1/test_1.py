import requests



def test_check_country():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    country = data.get('country')

    assert country == 'Belarus' , 'Country is wrong'


def test_check_city():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    city = data.get('city')

    assert city == 'Minsk'

def test_check_countryCode():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    countryCode = data.get('countryCode')

    assert countryCode == 'BY'

def test_check_isp():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    isp = data.get('isp')

    assert isp == 'Beltelecom'



def test_check_lat():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    lat = data.get('lat')

    assert lat == 53.9

def test_check_lon():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    lon = data.get('lon')

    assert lon == 27.5667


def test_check_org():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    org = data.get('org')

    assert org == 'Beltelecom'





