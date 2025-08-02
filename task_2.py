def create_multiplier(factor):
    if not isinstance(factor, (int, float)):
        raise TypeError(f"'factor' має бути int або float, а не {type(factor).__name__}")

    def multiplier(number):
        if not isinstance(number, (int, float)):
            raise TypeError(f"'number' має бути int або float, а не {type(number).__name__}")
        return number * factor
    return multiplier

# --- Демонстрація ---
print("--- Демонстрація замикання ---")

# Функція, що множить на 2
double = create_multiplier(2)
print("double(5):", double(5))   # → 10
print("double(10):", double(10)) # → 20

print("-" * 20)

# Функція, що множить на 3
triple = create_multiplier(3)
print("triple(5):", triple(5))   # → 15

print("-" * 20)

# Вкладене використання без збереження змінної
print("create_multiplier(4)(10):", create_multiplier('2.1')(0.5)) # → 40