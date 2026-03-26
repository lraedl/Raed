import random
import string
from functools import reduce

# ─── Настройки пароля ───────────────────────────────────────────
LENGTH = 12          # длина пароля
USE_DIGITS = True    # использовать цифры
USE_SYMBOLS = True   # использовать спецсимволы

# ─── Генератор символов ─────────────────────────────────────────
def password_generator(length, use_digits, use_symbols):
    """Генератор: выдаёт по одному символу пароля."""

    # Собираем набор допустимых символов
    chars = list(string.ascii_letters)          # буквы a-z, A-Z

    if use_digits:
        chars += list(string.digits)            # добавляем 0-9

    if use_symbols:
        chars += list(string.punctuation)       # добавляем !@#$...

    for _ in range(length):
        yield random.choice(chars)              # выдаём случайный символ

# ─── Применение функций map / filter / reduce ───────────────────

# 1. map — инвертируем регистр каждой буквы
#    swapcase(): 'a' → 'A', 'A' → 'a', '1' → '1' (без изменений)
inverted = map(lambda ch: ch.swapcase(), password_generator(LENGTH, USE_DIGITS, USE_SYMBOLS))

# 2. filter — убираем пробелы (на всякий случай)
filtered = filter(lambda ch: ch != ' ', inverted)

# 3. reduce — собираем список символов в одну строку
password = reduce(lambda acc, ch: acc + ch, filtered)

# ─── Вывод результата ───────────────────────────────────────────
print("Сгенерированный пароль:", password)
