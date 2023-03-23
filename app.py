import os 

flag = True
print("Для работы достаточно ввсети цифру действия.")
while (flag != False):
    menu_key = str(input('Возможные действия:\n 1)Создать 2 множества\n 2)Вывести множество\n 3)Удалить элемент из множества\n 4)Добавить элимент во множество\n'))
    os.system('CLS')
    match menu_key:
        case "1":
            FirstSet = set(input("Вводите элементы множества через пробел  для первого множества\n").split(" "))
            SecondSet = set(input("Вводите элементы множества через пробел для второго множества\n").split(" "))
            os.system('CLS')
        case "2":
            print("Ваше первое множество ", FirstSet)
            print("Ваше второе множество ", SecondSet)
        case "3": 
            match_key = str(input("В каком множестве вы хотите удалить элемент?(1, 2)\n"))
            os.system('CLS')
            match match_key:
                case "1":
                    print("Ваше множество:", FirstSet)
                    value = input("Какой элемент вас не устраивает?\n")
                    FirstSet.discard(value)
                    os.system('CLS')
                case "2":
                    print("Ваше множество:", SecondSet)
                    value = input("Какой элемент вас не устраивает?\n")
                    SecondSet.discard(value)
                    os.system('CLS')
        case "4":
            match_key = str(input("В какое множество вы хотите добавить элемент?(1, 2)\n"))
            os.system('CLS')
            match match_key:
                case "1":
                    print("Ваше множество:", FirstSet)
                    value = input("Какой элемент вы хотите добавить?\n")
                    FirstSet.add(value)
                    os.system('CLS')
                case "2":
                    print("Ваше множество:", SecondSet)
                    value = input("Какой элемент вы хотите добавить?\n")
                    SecondSet.add(value)
                    os.system('CLS')
        case _:
            print("Вы не ввели предложенное вам действие, поэтому программа завершила работу.")
            print("Выши множества были сохранены в файле 'Sets.txt'")
            with open("Sets.txt", "w+") as file:
                file.write(str(FirstSet))
                file.write(str(SecondSet))
            flag = False
             


