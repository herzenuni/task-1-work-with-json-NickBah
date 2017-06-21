import json
from pprint import pprint

filename = 'data.json'

try:
    data_file = open(filename)
    data = json.loads(data_file.read())

except FileNotFoundError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    status = 'Файл не найден'

for obj in data:
    pprint('Компания: ' + obj["company"])
    pprint('Эл.почта: ' + obj["email"])
    pprint('Телефон: ' + obj["phone"])
    pprint('Адрес: ' + obj["address"])
    pprint('-------------------------')
