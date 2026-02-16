#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def task3():
    results = []
    num = 500001
    
    while len(results) < 5:
        divisors = []
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                if i % 10 == 8 and i != 8:
                    divisors.append(i)
                j = num // i
                if j % 10 == 8 and j != 8 and j != num:
                    divisors.append(j)
        
        if divisors:
            results.append((num, min(divisors)))
        num += 1
    
    return results
print(" Задача 3:\n" , '=' * 70)

for num, div in task3():
    print(num, div)