def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите арифметический знак (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                return
            result = num1 / num2
        else:
            print("Ошибка: неверный арифметический знак!")
            return

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введено некорректное значение!")


calculator()