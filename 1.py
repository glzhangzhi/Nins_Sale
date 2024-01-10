import json
from pathlib import Path
from typing import List

import config
from pb import send_push
from URL请求 import GetHTML

path_database = Path('data.json')

if path_database.exists():
    with open(path_database, 'r', encoding='utf-8') as f:
        database = json.load(f)
else:
    database = {}


url = config.url

r = GetHTML(url, 1)

num_items = int(r.xpath('//*[@id="am-ranges-am_on_sale"]/ol/li/a/span[2]/text()')[0])

num_pages = int(num_items / 24) + 1

change_flag = False

s = ''

for i in range(1, num_pages + 1):
    
    url = f"{config.url}&p={i}"
    r = GetHTML(url, 1)

    ids:List[str] = r.xpath(f'//*[@id="amasty-shopby-product-list"]/div[3]/div/div/div[2]/div[1]/div[2]/div/@data-product-id')
    titles:List[str] = r.xpath(f'//*[@id="amasty-shopby-product-list"]/div[3]/div/div/div[2]/div[2]/a/text()')
    
    for j in range(len(ids)):
        
        id = ids[j]
        title = titles[j].replace('\n', '').strip()
        old:str = r.xpath(f'//*[@id="old-price-{id}"]/span/text()')[0]
        old = float(old.split(' ')[-1].replace(',', ''))
        new:str = r.xpath(f'//*[@id="product-price-{id}"]/span/text()')[0]
        new = float(new.split(' ')[-1].replace(',', ''))
        discount = (old - new) / old * 100
        
        if id not in database:
            database[id] = {'title':title, 'old':old, 'new':new, 'dis':f'{discount:.2f}%'}
            change_flag = True
            s = s + f'{title}: {old} -> {new} ({discount:.2f}%) \n'
        else:
            if new < database[id]['new']:
                database[id]['new'] = new
                database[id]['dis'] = discount
                change_flag = True
                s = s + f'{title}: {old} -> {new} ({discount:.2f}%) \n'
    
if change_flag:
    with open(path_database, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=4, ensure_ascii=False)
    send_push('本日新增折扣信息', s)


exit()