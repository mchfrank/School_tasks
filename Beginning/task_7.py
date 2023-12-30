def get_season(month):
    if 1 <= month <= 2 or month == 12:
        return "зима"
    elif 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    else:
        return "Неверный номер месяца"

# Пример использования функции
month_number = int(input("Введите номер месяца (от 1 до 12): "))
result = get_season(month_number)

print(f"Этот месяц относится к времени года: {result}")
