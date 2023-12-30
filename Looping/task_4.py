n = int(input("Введите натуральное число n: "))
# Инициализируем переменную для хранения факториала
factorial_result = 1
# Вычисляем факториал числа n
for i in range(1, n + 1):
    factorial_result *= i
# Выводим результат
print("Факториал", n, ":", factorial_result)
