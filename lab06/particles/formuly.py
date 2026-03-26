# formuly.py — формулы для расчётов

from .chasticy import h, c   # берём константы из файла chasticy.py


def udelny_zaryad(charge, mass):
    # Удельный заряд = заряд / масса
    # Для нейтрона заряд = 0, поэтому результат тоже 0
    if charge == 0:
        return 0.0
    return charge / mass


def kompton(mass):
    # Комптоновская длина волны = h / (m * c)
    return h / (mass * c)
