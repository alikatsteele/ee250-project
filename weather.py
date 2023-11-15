import requests
import time
import json

while True:
    res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=rain,snowfall,cloud_cover')
    data = json.loads(res.content)
    output = {
        'rain': data['current']['rain'],
        'snow': data['current']['snowfall'],
        'clouds': data['current']['cloud_cover']
    }
    d = json.dumps(output)
    print(d)
    requests.post('https://vibe-detector.jamm.es/update', data=d, headers={'Content-Type': 'application/json'})
    time.sleep(30)