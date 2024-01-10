import json

import requests

import config


def send_push(title, message):
    headers = {
        'Access-Token': config.pb_token,
        'Content-Type': 'application/json',
    }
    json_data = {
        'body': message,
        'title': title,
        'type': 'note',
        'device_iden' : config.device_id
    }
    
    requests.post('https://api.pushbullet.com/v2/pushes', headers=headers, json=json_data)


def get_device_id():
    headers = {
        'Access-Token': config.pb_token,
    }
    r = requests.get('https://api.pushbullet.com/v2/devices', headers=headers)
    l = json.loads(r.text)['devices']
    for i in l:
        print(f'nickname: {i['nickname']}  id:{i['iden']}')

if __name__ == "__main__":
    get_device_id()