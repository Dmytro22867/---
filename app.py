import re

def calculate(expression):
    """
    Обчислює математичний вираз.
    Підтримує +, -, *, /, (, ), числа з плаваючою комою.
    """
    try:
        # Перевіряємо, чи вираз містить тільки дозволені символи
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return "Помилка: недозволені символи у виразі"
        
        # Обчислюємо вираз
        result = eval(expression)
        
        # Перевіряємо, чи результат є числом
        if not isinstance(result, (int, float)):
            return "Помилка: вираз не повертає число"
        
        return result
    except ZeroDivisionError:
        return "Помилка: ділення на нуль"
    except Exception as e:
        return f"Помилка: {str(e)}"

if __name__ == "__main__":
    print("Ласкаво просимо до калькулятора!")
    print("Введіть математичний вираз (наприклад, 2 + 3 * 4) або 'exit' для виходу.")
    
    while True:
        expression = input("Введіть вираз: ").strip()
        if expression.lower() == 'exit':
            print("Дякуємо за використання калькулятора!")
            break
        result = calculate(expression)
        print(f"Результат: {result}")
