# Декоратор принимает функцию func и возвращает обёртку wrapper
def cache_decorator(func):
    cache = {}              

    def wrapper(n):
        if n not in cache:          
            cache[n] = func(n)      
        return cache[n]             

    return wrapper

# Пример 1: декоратор на функции возведения в квадрат
@cache_decorator
def kvadrat(n):
    print(f"  [считаем] {n}^2")   
    return n * n

print(kvadrat(4))
print(kvadrat(3))