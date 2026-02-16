#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
comma1 = my_favorite_movies.find(',')
comma2 = my_favorite_movies.find(',', comma1 + 1)
comma3 = my_favorite_movies.find(',', comma2 + 1)
comma4 = my_favorite_movies.find(',', comma3 + 1)

first_movie = my_favorite_movies[:comma1]
last_movie = my_favorite_movies[comma4 + 2:]
second_movie = my_favorite_movies[comma1 + 2:comma2]
second_from_end = my_favorite_movies[comma3 + 2:comma4]

print(first_movie)
print(last_movie)
print(second_movie)
print(second_from_end)