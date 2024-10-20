"""Завдання 2. 
1. Обчислити значення визначеного інтеграла функції методом Монте-Карло.
2. Перевірити правильність розрахунків, щоб підтвердити точність методу Монте-Карло, порівнявши 
отриманий результат з аналітичними розрахунками або результатом виконання функції quad. Зробити висновки.
(Для перевірки обчислення визначеного інтеграла можна використовувати бібліотеку SciPy, зокрема її функцію quad 
з підмодуля integrate). """
import random
import numpy as np
import scipy.integrate as spi


def func(x):
    """Функція, для якої потрібно обчислити інтеграл"""
    return -x**2+10*x

def integral(rounds, s, bottom, top):
    """Функція для обчислення інтеграла методом Монте-Карло"""
    vals = []
    for _ in range(rounds):
        sums = 0
        for _ in range(s):       
            X = random.uniform(bottom, top)
            sums+= func(X)
            samples = sums * ((top - bottom)/ s)
        vals.append(samples)
    return np.average(vals), vals


iterations = 100
size = 100000
a, b = 0, 10

mc, all_vals = integral(iterations, size, a, b)


#порівнюємо результат з результатом функції quad модуля Scipy
result, error = spi.quad(func, a, b)
print("Монте Карло Інтеграл: ", mc) 
print("Scipy quad Інтеграл: ", result)







