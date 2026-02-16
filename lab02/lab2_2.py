#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def task2_count_digit_4():
    value = 5**36 + 5**24 - 25
    count = 0
    n = value
    
    while n > 0:
        if n % 5 == 4:
            count += 1
        n //= 5
    
    return count

def task2_with_conversion():
    value = 5**36 + 5**24 - 25
    digits = []
    n = value
    while n > 0:
        digits.append(n % 5)
        n //= 5
    digits.reverse()
    
    count = digits.count(4)
    
    return count, digits

print("\nЗадача 2:")
print(f"Количество цифр 4: {task2_count_digit_4()}")