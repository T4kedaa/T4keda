
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль невозможно"
    return x / y

while True:
    # Ввод чисел
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введите числа правильно!")
        continue
    
    # Выбор операции
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    choice = input("Ваш выбор (1/2/3/4): ")

    if choice == '1':
        print(f"Результат: {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Результат: {divide(num1, num2)}")
    else:
        print("Ошибка: Неверный выбор операции.")
        continue

    # Повторить или выйти
    again = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
    if again != 'да':
        print("Выход из программы.")
        break