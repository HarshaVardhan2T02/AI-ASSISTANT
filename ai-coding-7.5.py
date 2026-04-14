def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))

def check_sum():
    return abs((0.1 + 0.2) - 0.3) < 1e-9

print(check_sum())

def countdown(n):
    if n == 0:
        print(0)
        return
    print(n)
    countdown(n - 1)

countdown(5)

def get_value():
    data = {"a": 1, "b": 2}
    try:
        return data["c"]
    except KeyError:
        return "Key not found"

print(get_value())

def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1

loop_example()

a, b, _ = (1, 2, 3)
print(a, b)

def func():
    x = 5
    y = 10
    return x + y

print(func())

import math
print(math.sqrt(16))

def total(numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total([1, 2, 3]))

def calculate_area(length, width):
    return length * width

assert calculate_area(5, 4) == 20
assert calculate_area(10, 2) == 20
assert calculate_area(3, 3) == 9

print("All test cases passed")

def add_values():
    return 5 + int("10")

assert add_values() == 15
assert 3 + int("7") == 10
assert int("4") + 6 == 10

print("All test cases passed")

def combine():
    return "Numbers: " + str([1, 2, 3])

assert combine() == "Numbers: [1, 2, 3]"
assert "A" + str([1]) == "A[1]"
assert "List: " + str([]) == "List: []"

print("All test cases passed")

def repeat_text():
    return "Hello" * int(2.5)

assert repeat_text() == "HelloHello"
assert "A" * int(3.9) == "AAA"
assert "Hi" * int(1.1) == "Hi"

print("All test cases passed")

def compute():
    value = 0
    return value + 10

assert compute() == 10
assert 0 + 5 == 5
assert (0 + 0) == 0

print("All test cases passed")


def sum_two_numbers(a, b):
    return int(a) + int(b)

assert sum_two_numbers("2", "3") == 5
assert sum_two_numbers("10", "20") == 30
assert sum_two_numbers("0", "5") == 5

print("All test cases passed")
