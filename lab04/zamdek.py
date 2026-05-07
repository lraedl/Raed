# Декоратор применяется к внутренней функции замыкания — она одновременно и замыкает memo, и кэшируется декоратором.
def cache_decorator(func):
    cache = {}              

    def wrapper(n):
        if n not in cache:          
            cache[n] = func(n)      
        return cache[n]             

    return wrapper

def fibonacci_factory():
    memo = {0: 0, 1: 1}   

    @cache_decorator      
    def fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    return fib


print("Декоратор + Замыкание вместе")

print("\n-- Числа Фибоначчи --")
get_fib = fibonacci_factory()
print(f"fib(10)  = {get_fib(10)}")
print(f"fib(20)  = {get_fib(20)}")
print(f"fib(35)  = {get_fib(35)}")
print(f"fib(100) = {get_fib(100)}")