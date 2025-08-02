def example_function(a, b, c):
    """Функція з 5 локальними змінними: a, b, c, temp_value, result."""
    temp_value = a + b
    result = temp_value * c
    return result

def example_function_simple(x, y):
    """Функція з 3 локальними змінними: x, y, z."""
    z = x + y
    return z

def count_local_variables(func):
    """Повертає кількість локальних змінних у функції (включаючи параметри)."""
    return func.__code__.co_nlocals

def demo():
    print("--- Підрахунок локальних змінних ---")

    funcs = [
        ("example_function", example_function, 5),
        ("example_function_simple", example_function_simple, 3),
        ("count_local_variables", count_local_variables, 1)
    ]

    for name, fn, expected in funcs:
        actual = count_local_variables(fn)
        print(f"{name}: {actual} локальних змінних (очікується: {expected})")
        print("-" * 20)

    print("Програму завершено.")

# Запуск демонстрації
demo()