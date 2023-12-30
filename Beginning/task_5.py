# def is_year_leap(year):
#     # Год является високосным, если он делится на 4, но не делится на 100, за исключением случаев, когда он делится на 400.
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# # Пример использования функции
# year = int(input("Введите год: "))
#
# if is_year_leap(year):
#     print(f"{year} год является високосным.")
# else:
#     print(f"{year} год не является високосным.")

def is_leap_year(year):
    if year % 400 == 0:
        return "YES"
    elif year % 4 == 0 and year % 100 != 0:
        return "YES"
    else:
        return "NO"

# Ввод года с клавиатуры
year = int(input("Введите год: "))
result = is_leap_year(year)
print(result)

