import tasks

def main():
    while True:
        print("\nГлавное меню:")
        print("\n1.Выбор задания\n2.Завершить программу")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            print("\n1. Задание 1")
            print("2. Задание 2")
            print("3. Задание 3")

            second_choice = input("Выберите пункт меню: ")
            if second_choice == '1':
                tasks.task_1()
            elif second_choice == '2':
                tasks.task_2()
            elif second_choice == '3':
                tasks.task_3()
            else:
                print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 3.")
        elif choice == '2':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню 1 или 2.")