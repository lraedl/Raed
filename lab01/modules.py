#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GeometryCalculator:
    PI = 3.1415926
    
    @staticmethod
    def circle_area(radius):
        return round(GeometryCalculator.PI * radius ** 2, 4)
    
    @staticmethod
    def is_point_in_circle(point, radius=42):
        x, y = point
        return (x**2 + y**2) ** 0.5 <= radius


class MathPuzzle:
    @staticmethod
    def solve():
        return (1 + 2) * 3 + 4 * 5


class MovieProcessor:
    @staticmethod
    def extract(movies_string):
        commas = [i for i, char in enumerate(movies_string) if char == ',']
        return {
            'first': movies_string[:commas[0]],
            'last': movies_string[commas[-1] + 2:],
            'second': movies_string[commas[0] + 2:commas[1]],
            'second_from_end': movies_string[commas[-2] + 2:commas[-1]]
        }


class FamilyAnalyzer:
    @staticmethod
    def get_stats():
        heights = [['Отец', 185], ['Мать', 165], ['Дедушка', 175]]
        father = next(h for name, h in heights if name == 'Отец')
        total = sum(h for _, h in heights)
        return father, total


class ZooManager:
    @staticmethod
    def manage(zoo, birds):
        zoo_copy = zoo.copy()
        zoo_copy.insert(1, 'bear')
        zoo_copy.extend(birds)
        if 'elephant' in zoo_copy:
            zoo_copy.remove('elephant')
        return zoo_copy, zoo_copy.index('lion') + 1, zoo_copy.index('lark') + 1


class MusicCalculatorList:
    @staticmethod
    def calculate(songs_list, names):
        songs_dict = {song[0]: song[1] for song in songs_list}
        return round(sum(songs_dict.get(name, 0) for name in names), 2)


class MusicCalculatorDict:
    @staticmethod
    def calculate(songs_dict, names):
        return round(sum(songs_dict.get(name, 0) for name in names), 2)


class MessageDecryptor:
    @staticmethod
    def decrypt(secret_message):
        words = []
        words.append(secret_message[0][3])
        words.append(secret_message[1][9:13])
        words.append(secret_message[2][5:15:2])
        words.append(secret_message[3][12:7:-1])
        words.append(secret_message[4][20:15:-1])
        return ' '.join(words)


class FlowerAnalyzer:
    @staticmethod
    def analyze(garden, meadow):
        g_set, m_set = set(garden), set(meadow)
        return {
            'all': sorted(g_set.union(m_set)),
            'common': sorted(g_set.intersection(m_set)),
            'only_garden': sorted(g_set.difference(m_set)),
            'only_meadow': sorted(m_set.difference(g_set))
        }


class ShopAnalyzer:
    @staticmethod
    def analyze(shops):
        sweets = {}
        for shop_name, items in shops.items():
            for item in items:
                name = item['name']
                if name not in sweets:
                    sweets[name] = []
                sweets[name].append({'shop': shop_name, 'price': item['price']})
        return sweets


class StoreCalculator:
    @staticmethod
    def calculate(goods, store):
        results = {}
        for name, code in goods.items():
            if code in store:
                items = store[code]
                total_qty = sum(item['quantity'] for item in items)
                total_cost = sum(item['quantity'] * item['price'] for item in items)
                results[name] = {'quantity': total_qty, 'cost': total_cost}
        return results


class DistanceCalculator:
    @staticmethod
    def calculate(sites):
        distances = {}
        for city1, (x1, y1) in sites.items():
            distances[city1] = {}
            for city2, (x2, y2) in sites.items():
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(dist, 2)
        return distances