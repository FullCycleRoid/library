import requests



def geodata(request):
    is_cashed = ('geodata' in request.session)
    if not is_cashed:
        data = requests.get(f'http://api.ipstack.com/176.59.5.122?access_key=c45f12aa73d4a5e01c67d2ec41b37122')
        request.session['geodata'] = data.json()
    geodata = request.session['geodata']

    return {'ip': geodata['ip'],
            'city': geodata['city'],
            'is_cashed': is_cashed,
            'api': 'c45f12aa73d4a5e01c67d2ec41b37122',
            'longitude': geodata['longitude'],
            'latitude': geodata['latitude']
            }