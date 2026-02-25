import math

# ==========================================
# ЗАДАНИЕ 1: Вычисление вложенных корней x_n
# ==========================================

# 1. Рекурсивный способ
def get_root_recursive(n):
    if n == 1:
        return math.sqrt(3)
    else:
        return math.sqrt(3 + get_root_recursive(n - 1))

# 2. Итеративный способ (через цикл)
def get_root_iterative(n):
    result = 0
    for i in range(n):
        result = math.sqrt(3 + result)
    return result

# ==========================================
# ЗАДАНИЕ 2: Пересечение двух списков
# ==========================================

# 1. Рекурсивный способ
def intersect_recursive(list1, list2):
    if not list1:
        return []
    
    first = list1[0]
    rest = list1[1:]
    
    if first in list2:
        return [first] + intersect_recursive(rest, list2)
    else:
        return intersect_recursive(rest, list2)

# 2. Итеративный способ (через цикл)
def intersect_iterative(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            if item not in result:
                result.append(item)
    return result



print("--- Задание 1: Корни ---")
n = 3
print(f"n = {n}")
print(f"Рекурсия: {get_root_recursive(n)}")
print(f"Цикл:     {get_root_iterative(n)}")

print("\n--- Задание 2: Пересечение списков ---")
a = [1, 2, 3, 4]
b = [2, 3, 4, 6, 8]

print(f"Список 1: {a}")
print(f"Список 2: {b}")
print(f"Результат (рекурсия): {intersect_recursive(a, b)}")
print(f"Результат (цикл):     {intersect_iterative(a, b)}")

# доп тесты
print(f"Тест [5, 8, 2] и [2, 9, 1]: {intersect_iterative([5, 8, 2], [2, 9, 1])}")
print(f"Тест [5, 8, 2] и [7, 4]:    {intersect_iterative([5, 8, 2], [7, 4])}")