n = int(input("Введите натуральное число n: "))
# Инициализируем переменную для хранения суммы
sum_cubes = 0
# Вычисляем сумму кубов от 1 до n
for i in range(1, n + 1):
    sum_cubes += i**3
# Выводим результат
print(sum_cubes)
