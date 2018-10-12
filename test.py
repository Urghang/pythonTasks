scores = []
choice = None

while choice != "0":
    print(
        """
        
        Рекорды 2.0
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        """
    )

    choice = input("Ваш выбор: ")
    print()
    # выход
    if choice == "0":
        print("До свидания.")
    # вывод рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t\t", score)
    # ввод рекорда
    elif choice == "2":
        name = input("Введите имя игрока: ")
        score = int(input("Введите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Извините, в меню нет пункта", choice)
