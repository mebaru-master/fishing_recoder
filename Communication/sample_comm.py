# 富山県の週間天気予報を取得して表示するプログラム
# 2020/07/01
# 2020/07/02

import requests
import json
import pprint

# 週間天気予報を取得するURL
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=160010'

# 週間天気予報を取得する
response = requests.get(url)
data = response.json()
pprint.pprint(data)

# 週間天気予報を表示する
for weather in data['forecasts']:
    print(weather['dateLabel'] + ' : ' + weather['telop'])

