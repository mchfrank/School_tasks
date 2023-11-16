# Считываем целое число с клавиатуры
number = int(input("Введите целое число: "))

# Вычисляем следующее и предыдущее числа
next_number = number + 1
previous_number = number - 1

# Выводим результат
print(f"Следующее число за числом {number} – {next_number}.")
print(f"Предыдущее число за числом {number} – {previous_number}.")
