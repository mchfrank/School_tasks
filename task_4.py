def arithmetic(num1, num2, operation):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # Добавим проверку на деление на 0
        if num2 != 0:
            result = num1 / num2
        else:
            return "Деление на ноль невозможно"
    else:
        return "Неизвестная операция"

    return result


# Пример использования функции
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

result = arithmetic(num1, num2, operation)
print(f"Результат: {result}")
