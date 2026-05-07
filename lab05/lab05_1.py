#6. Генератор, создающий пароли по определённым правилам. Инвертируйте регистр букв в выводе генератора.
import random
import string
from functools import reduce

# Настройки пароля
LENGTH = 12          
USE_DIGITS = True   
USE_SYMBOLS = True   

# Генератор символов 
def password_generator(length, use_digits, use_symbols):
    #Генератор: выдаёт по одному символу пароля.

    
    chars = list(string.ascii_letters)          # буквы a-z, A-Z

    if use_digits:
        chars += list(string.digits)            # добавляем 0-9

    if use_symbols:
        chars += list(string.punctuation)       # добавляем !@#$...

    while True:        
        normpassword = ''.join(random.choices(chars, k=length))
        yield normpassword


# 1. map — инвертируем регистр каждой буквы
#    swapcase(): 'a' → 'A', 'A' → 'a', '1' → '1' (без изменений)
gen = password_generator(LENGTH, USE_DIGITS, USE_SYMBOLS)
raw_password = next(gen)                    # получаем первый пароль из генератора
print(raw_password)
inverted = map(lambda ch: ch.swapcase(), raw_password)

# 2. filter — убираем пробелы (на всякий случай)
filtered = filter(lambda ch: ch != ' ', inverted)

# 3. reduce — собираем список символов в одну строку
password = reduce(lambda acc, ch: acc + ch, filtered)

print("Сгенерированный пароль:", password)

# Пример: получить несколько паролей подряд
for i in range(3):
    pwd = next(gen)
    print(f"  Пароль {i+1}: {pwd}")  

# lambda ch: ch.swapcase()
# это анонимная функция, которая принимает символ ch и возвращает его с инвертированным регистром. Например, 'a' станет 'A', 'A' станет 'a',
# а цифры и символы останутся без изменений.
# lambda ch: ch != ' '
# это анонимная функция, которая проверяет, является ли символ ch пробелом. Если не является, то символ проходит фильтрацию.
# как работает lambda acc: acc + ch
# Эта анонимная функция принимает два аргумента: acc (аккумулятор) и ch (текущий символ). Она объединяет их, добавляя текущий символ к аккумулятору. 
# В результате reduce собирает все символы в одну строку.


# Какие особенности у map, filter и reduce
# map, filter и reduce — это функции высшего порядка, которые применяют заданную функцию к каждому элементу последовательности. 
# map преобразует каждый элемент, filter отбирает элементы по условию, а reduce сводит последовательность к одному результату, используя аккумулятор. 
# Они позволяют писать более выразительный и функциональный код, избегая явных циклов и мутабельного состояния.