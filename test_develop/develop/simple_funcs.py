def func_for_test(a, b):
    return a + b


def get_fizz_buzz(number):
    if number < 1 or number > 100:
        return "Ошибка: число не в диапазоне от 1 до 100"
    elif number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def product_in_range(start, end):
    # Убедимся, что start меньше end
    if start > end:
        start, end = end, start

    # Вычисляем произведение
    product = 1
    for num in range(start, end + 1):
        product *= num

    return product
