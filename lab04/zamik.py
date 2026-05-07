# Замыкание (closure) — это внутренняя функция, которая «захватывает» переменные из внешней функции и продолжает к ним доступ даже после её завершения.
def fibonacci_factory():
    memo = {0: 0, 1: 1}   
    def fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    return fib




print("\n-- Числа Фибоначчи --")
get_fib = fibonacci_factory()
print(f"fib(10)  = {get_fib(10)}")
print(f"fib(20)  = {get_fib(20)}")
print(f"fib(35)  = {get_fib(35)}")
print(f"fib(100) = {get_fib(100)}")
