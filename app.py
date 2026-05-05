def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

if __name__ == "__main__":
    print("--- Математичний модуль готовий ---")
    print(f"1 + 1 = {add(1, 1)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"20 / 4 = {divide(20, 4)}")
