# 1. Декоратор для кэширования
def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

# 2. Замыкание для Фибоначчи
def fibonacci_factory():
    @cache_decorator
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    return fib

print("Программа запущена...")

# Создаем нашу функцию
get_fib = fibonacci_factory()

# Печатаем результаты
print(f"Фибоначчи(10) = {get_fib(10)}")
print(f"Фибоначчи(35) = {get_fib(35)}")
print(f"Фибоначчи(100) = {get_fib(100)}")

