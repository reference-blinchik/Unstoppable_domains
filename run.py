from pyuseragents import random as random_useragent
from requests import Session

print("Почты должны быть в виде: email или email:password")
file = input("Введите названия файла с почтами (файл должен находиться в папке с файлом скрипта): ")
with open(file) as f:
    for i in f.readlines():
        email = i.split(":")[0]
        session = Session()
        session.headers.update({'user-agent': random_useragent(),
                                'accept': 'application/json',
                                'accept-language': 'ru,en;q=0.9',
                                'content-type': 'application/json',
                                'origin': 'https://www.blockchain.com',
                                'referer': 'https://www.blockchain.com/'
                                })
        r = session.post('https://api.blockchain.info/marketing-automation/add-subscriber',
                         json={"dataFields": {"android": "true", "ios": "true", "web": "true"},
                               "email": email,
                               "listId": 1692647})
        if r.ok:
            print(email, "on the waitlist")