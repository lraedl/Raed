#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
}
# Указать надо только по 2 магазина с минимальными ценами
sweets = {}

# Собираем все уникальные названия сладостей
all_sweets = set()
for shop_name, items in shops.items():
    for item in items:
        all_sweets.add(item['name'])

# Для каждой сладости собираем информацию из магазинов
for sweet in all_sweets:
    sweets[sweet] = []
    for shop_name, items in shops.items():
        for item in items:
            if item['name'] == sweet:
                sweets[sweet].append({
                    'shop': shop_name,
                    'price': item['price']
                })

print(sweets)