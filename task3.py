while True:
    
    print("Виберіть операцію: ")
    print("Додавання - 1 ")
    print("Віднімання - 2 ")
    print("Множення - 3 ")
    print("Ділення - 4 ")
    print("Перетворення типів даних - 5")

    action = int(input())
    match action:
        case 1:
            print("Введіть два числа")
            num1 = int(input())
            num2 = int(input())
            print("Результат: ", num1 + num2)
        case 2:
            print("Введіть два числа")
            num1 = int(input())
            num2 = int(input())
            print("Результат: ", num1 - num2)
        case 3:
            print("Введіть два числа")
            num1 = int(input())
            num2 = int(input())
            print("Результат: ", num1 * num2)
        case 4:
            print("Введіть два числа")
            num1 = int(input())
            num2 = int(input())
            print("Результат: ", num1 / num2)
        case _: exit(0)



