# Вводим два целых числа
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

# Используем условный оператор для определения наименьшего числа
if number1 < number2:
    print(f"Наименьшее число: {number1}")
elif number2 < number1:
    print(f"Наименьшее число: {number2}")
else:
    print("Числа равны")
