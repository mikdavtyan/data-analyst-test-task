def missing_number(nums: list[int]) -> int:
    # Так как одного числа не хватает, полное значение n равно длине списка + 1
    n = len(nums) + 1
    
    # Формула суммы Гаусса для вычисления суммы чисел от 1 до n
    expected_sum = n * (n + 1) // 2
    
    # Фактическая сумма элементов в массиве
    actual_sum = sum(nums)
    
    # Разница и есть пропущенное число
    return expected_sum - actual_sum

# Пример из условия
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
    print(missing_number(nums))  # Вывод: 7
