#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules import (
    GeometryCalculator, MathPuzzle, MovieProcessor,
    FamilyAnalyzer, ZooManager, MusicCalculatorList,
    MusicCalculatorDict, MessageDecryptor, FlowerAnalyzer,
    ShopAnalyzer, StoreCalculator, DistanceCalculator
)

print("=" * 60)
print("ВЕРХНЕУРОВНЕВЫЙ МОДУЛЬ - КООРДИНАЦИЯ 11 МОДУЛЕЙ")
print("=" * 60)

print("\n1. ГЕОМЕТРИЯ:")
area = GeometryCalculator.circle_area(42)
print(f"   Площадь круга: {area}")
print(f"   Точка (23,34) в круге: {GeometryCalculator.is_point_in_circle((23, 34))}")
print(f"   Точка (30,30) в круге: {GeometryCalculator.is_point_in_circle((30, 30))}")

print("\n2. ГОЛОВОЛОМКА:")
result = MathPuzzle.solve()
print(f"   1 2 3 4 5 = {result}")

print("\n3. ФИЛЬМЫ:")
movies = MovieProcessor.extract('Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее')
print(f"   Первый: {movies['first']}")
print(f"   Последний: {movies['last']}")

print("\n4. СЕМЬЯ:")
father, total = FamilyAnalyzer.get_stats()
print(f"   Рост отца: {father} см")
print(f"   Общий рост: {total} см")

print("\n5. ЗООПАРК:")
zoo, lion_pos, lark_pos = ZooManager.manage(['lion', 'kangaroo', 'elephant', 'monkey'], ['rooster', 'ostrich', 'lark'])
print(f"   Финальный зоопарк: {zoo}")
print(f"   Лев в клетке: {lion_pos}")
print(f"   Жаворонок в клетке: {lark_pos}")

print("\n6. ПЕСНИ:")
songs_list = [
    ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56],
    ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]
]
songs_dict = {
    'World in My Eyes': 4.76, 'Sweetest Perfection': 4.43, 'Personal Jesus': 4.56,
    'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68
}
time1 = MusicCalculatorList.calculate(songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
time2 = MusicCalculatorDict.calculate(songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
print(f"   Первые три песни: {time1} мин")
print(f"   Вторые три песни: {time2} мин")

print("\n7. ДЕШИФРАЦИЯ:")
secret = [
    'квевтфппбщЗстмзалтнмаршг65длгуча',
    'дьсеыблц2бане4т64ь463ущея6втщл66',
    'т3пплвце1н3и2кд4лы12чф1ап36кычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ех61а',
]
decrypted = MessageDecryptor.decrypt(secret)
print(f"   Сообщение: {decrypted}")

print("\n8. ЦВЕТЫ:")
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
flowers = FlowerAnalyzer.analyze(garden, meadow)
print(f"   Все цветы: {flowers['all']}")
print(f"   Общие: {flowers['common']}")

print("\n9. МАГАЗИНЫ:")
shops = {
    'ашан': [{'name': 'печенье', 'price': 10.99}, {'name': 'конфеты', 'price': 34.99}],
    'пятерочка': [{'name': 'печенье', 'price': 9.99}, {'name': 'конфеты', 'price': 32.99}]
}
sweets = ShopAnalyzer.analyze(shops)
print(f"   Печенье: {sweets['печенье']}")

print("\n10. СКЛАД:")
goods = {'Лампа': '12345', 'Стол': '23456'}
store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}]
}
costs = StoreCalculator.calculate(goods, store)
for product, data in costs.items():
    print(f"   {product}: {data['quantity']} шт, {data['cost']:.2f} руб")

print("\n11. РАССТОЯНИЯ:")
sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}
distances = DistanceCalculator.calculate(sites)
print(f"   Расстояния: {distances}")

print("\n" + "=" * 60)
print("✅ ВСЕ 11 МОДУЛЕЙ ВЫПОЛНЕНЫ!")
print("=" * 60)