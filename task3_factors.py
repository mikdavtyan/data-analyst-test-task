def prime_factors(n: int) -> list[int]:
    factors = []
    
    # Шаг 1: Извлекаем все двойки (единственное четное простое число)
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # Шаг 2: Перебираем нечетные делители от 3 до sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2  # Переходим к следующему нечетному числу
        
    # Шаг 3: Если после всех делений n осталось больше 2, то это число тоже простое
    if n > 2:
        factors.append(n)
        
    return factors

# Пример из условия
if __name__ == "__main__":
    n = 56
    print(prime_factors(n))  # Вывод: [2, 2, 2, 7]
