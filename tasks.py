import random

# Функция для генерации массива случайных чисел
generate = lambda length: [random.randint(1, 100) for _ in range(length)]  # Включение в последовательность

# Преобразование строки в список целых чисел
parse_input = lambda input_str: list(map(int, input_str.split()))

# Задание 1: Сумма и сортировка массивов
def task_1():
    while True:
        print("\nЗадание 1\nНахождение суммы чисел из массивов, сортировка массивов")
        v = input("1. Ввод массивов вручную\n"
                  "2. Генерация массивов автоматически\n"
                  "Выберите действие: ")
        if v == '1':
            arr1 = parse_input(input("Введите первый массив чисел через пробел: "))
            arr2 = parse_input(input("Введите второй массив чисел через пробел: "))
            if len(arr1) != len(arr2):
                print("Массивы разной длины. Введите массивы одной длины.")
                continue
            break
        elif v == '2':
            n = int(input('Введите количество элементов массива: '))
            # Генерация данных
            arr1 = generate(n)
            arr2 = generate(n)
            print('Массив 1:\n', arr1, '\nМассив 2:\n', arr2)
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню 1 или 2.")

    result = [arr1[i] + arr2[i] if arr1[i] != arr2[i] else 0 for i in range(len(arr1))]
    print("Результат:\n", sorted(result), "\nПервый массив, отсортированный по убыванию: \n",
          sorted(arr1, reverse=True),
          "\nВторой массив, отсортированный по возрастанию: \n", sorted(arr2))


# Задание 2: Проверка и возведение в степень
def task_2():
    while True:
        print("\nЗадание 2\nМогут ли два числа под одним и тем же номером в сумме давать третье число. "
              "\nЕсли могут, то сумма трех чисел возводится в степень наименьшего числа.")
        v = input("1. Ввод массивов вручную\n"
                  "2. Генерация массивов автоматически\n"
                  "Выберите действие: ")
        if v == '1':
            arr1 = parse_input(input("Введите первый массив чисел через пробел: "))
            arr2 = parse_input(input("Введите второй массив чисел через пробел: "))
            arr3 = parse_input(input("Введите третий массив чисел через пробел: "))
            if len(arr1) != len(arr2) or len(arr1) != len(arr3):
                print("Массивы разной длины. Введите массивы одной длины.")
                continue
            break
        elif v == '2':
            n = int(input('Введите количество элементов массива: '))
            # Генерация данных
            arr1 = generate(n)
            arr2 = generate(n)
            arr3 = generate(n)
            print('Массив 1:\n', arr1, '\nМассив 2:\n', arr2, '\nМассив 3:\n', arr3)
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню 1 или 2.")

    for i in range(len(arr1)):
        if arr1[i] + arr2[i] == arr3[i]:
            min_num = min(arr1[i], arr2[i])
            result = (arr1[i] + arr2[i] + arr3[i]) ** min_num
            print(f"Для чисел {arr1[i]} и {arr2[i]} сумма возводится в степень {min_num}: {result}")
        else:
            print(f"Для чисел {arr1[i]} и {arr2[i]} сумма не равна {arr3[i]}")

# Задание 3: Арифметические преобразования
def task_3():
    while True:
        print("\nЗадание 3\nМожно ли получить число из 3 массива, арифметическими преобразованиями с числами"
              "\nиз двух других массивов.Числа проверяются последовательно ")
        v = input("1. Ввод массивов вручную\n"
                  "2. Генерация массивов автоматически\n"
                  "Выберите действие: ")
        if v == '1':
            arr1 = parse_input(input("Введите первый массив чисел через пробел: "))
            arr2 = parse_input(input("Введите второй массив чисел через пробел: "))
            arr3 = parse_input(input("Введите третий массив чисел через пробел: "))
            if len(arr1) != len(arr2) or len(arr1) != len(arr3):
                print("Массивы разной длины. Введите массивы одной длины.")
                continue
            break
        elif v == '2':
            n = int(input('Введите количество элементов массива: '))
            # Генерация данных
            arr1 = generate(n)
            arr2 = generate(n)
            arr3 = generate(n)
            print('Массив 1:\n', arr1, '\nМассив 2:\n', arr2, '\nМассив 3:\n', arr3)
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню 1 или 2.")

    for i in range(len(arr1)):
        if arr1[i] == arr2[i] + arr3[i] or arr2[i] == arr1[i] + arr3[i] or arr3[i] == arr1[i] + arr2[i]:
            print(f"Можно получить {arr3[i]} из {arr2[i]} и {arr1[i]} арифметическими преобразованиями")
        else:
            print(f"Нельзя получить {arr3[i]} из {arr2[i]} и {arr1[i]} арифметическими преобразованиями")