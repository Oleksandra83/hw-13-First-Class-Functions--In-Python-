def choose_func(nums: list, func1, func2):

    return func1(nums) if all(num > 0 for num in nums) else func2(nums)


def square_nums(nums):
    """Повертає список квадратів чисел."""
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    """Повертає список лише з додатніх чисел."""
    return [num for num in nums if num > 0]


# --- Тести ---
print("--- Перевірка choose_func ---")

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

result1 = choose_func(nums1, square_nums, remove_negatives)
print(f"{nums1} → {result1}")
assert result1 == [1, 4, 9, 16, 25]

print("-" * 20)

result2 = choose_func(nums2, square_nums, remove_negatives)
print(f"{nums2} → {result2}")
assert result2 == [1, 3, 5]

print("\n✅ Всі перевірки пройшли успішно!")