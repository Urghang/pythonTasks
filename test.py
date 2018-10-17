characters = {"Сила": 0, "Здоровье": 0, "Мудрость": 0, "Ловкость": 0}
points = 30
selectCharacter = ""
selectPoint = 0
variant = ""

while variant != "0":

    print("Вам доступно", points, "очков! \n \
          Вы можете распределить их между основными характеристиками вашего персонажа\n \
          ваши характеристики:")

    for key in characters:
        print(key, ":", characters[key])

    print(
        """
        Выход 0
        Распределить очки характеристик 1
        Убрать очки характеристик 2

        """
    )

    variant = input("Ваш выбор; ")

    if variant == "1":

        print("Ваши характеристики распределны таким образом",
              "Сила:", characters["Сила"],
              "Здоровье:", characters["Здоровье"],
              "Мудрость:", characters["Мудрость"],
              "Ловкость:", characters["Ловкость"])
        print("Доступно очков для распределения:", points)

        while selectCharacter != "готово":

            print("Для завершения распределения характеристик введите готово")
            selectCharacter = input("Введите характеристику в которую вы хотите добавить очки: ")
            selectPoint = int(input("Введите количество очков: "))

            if selectPoint <= points and points > 0:

                if points == 0:
                    continue

                if selectCharacter == "Сила":

                    characters[selectCharacter] += selectPoint
                    points -= selectPoint
                    print("Вы увеличили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Здоровье":

                    characters[selectCharacter] += selectPoint
                    points -= selectPoint
                    print("Вы увеличили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Мудрость":

                    characters[selectCharacter] += selectPoint
                    points -= selectPoint
                    print("Вы увеличили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Ловкость":

                    characters[selectCharacter] += selectPoint
                    points -= selectPoint
                    print("Вы увеличили характеристику", selectCharacter, "на ", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                else:

                    print("У вас нет характеристики", selectCharacter)
                    print("Ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

            elif points == 0:

                print("У вас закончились свободные очки для распределения")
                selectCharacter = "готово"

            else:

                print("Вам доступно всего", points, "очков для распределения")
                print("Ваши характеристики распределны таким образом",
                      "Сила:", characters["Сила"],
                      "Здоровье:", characters["Здоровье"],
                      "Мудрость:", characters["Мудрость"],
                      "Ловкость:", characters["Ловкость"])
                print("Доступно очков для распределения:", points)

    elif variant == "2":

        print("Ваши характеристики распределны таким образом",
              "Сила:", characters["Сила"],
              "Здоровье:", characters["Здоровье"],
              "Мудрость:", characters["Мудрость"],
              "Ловкость:", characters["Ловкость"])
        print("Доступно очков для распределения:", points)

        while selectCharacter != "Готово":
            selectCharacter = input("Введите характеристику у который вы хотите снять очки: ")
            selectPoint = int(input("Введите количество очков: "))

            if selectPoint <= characters[selectCharacter] and characters[selectCharacter] > 0:

                if selectCharacter == "Сила":

                    characters[selectCharacter] -= selectPoint
                    points += selectPoint
                    print("Вы уменьшили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Здоровье":

                    characters[selectCharacter] -= selectPoint
                    points += selectPoint
                    print("Вы уменьшили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Мудрость":

                    characters[selectCharacter] -= selectPoint
                    points += selectPoint
                    print("Вы уменьшили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                elif selectCharacter == "Ловкость":

                    characters[selectCharacter] -= selectPoint
                    points += selectPoint
                    print("Вы уменьшили характеристику", selectCharacter, "на", selectPoint, "очков")
                    print("Теперь ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

                else:
                    print("У вас нет характеристики", selectCharacter)
                    print("Ваши характеристики распределны таким образом",
                          "Сила:", characters["Сила"],
                          "Здоровье:", characters["Здоровье"],
                          "Мудрость:", characters["Мудрость"],
                          "Ловкость:", characters["Ловкость"])
                    print("Доступно очков для распределения:", points)

            else:

                print("У вас в характеристике", selectCharacter, "не хватает очков")
                print("Ваши характеристики распределны таким образом",
                      "Сила:", characters["Сила"],
                      "Здоровье:", characters["Здоровье"],
                      "Мудрость:", characters["Мудрость"],
                      "Ловкость:", characters["Ловкость"])
                print("Доступно очков для распределения:", points)

            if selectCharacter == "готово":
                continue

    elif variant == "0":

        print("Вы завершили игру.")

    else:

        print(
            """
            Нет такой инструкции, попробуйте еще раз
            
            Выход 0
            Распределить очки характеристик 1
            Убрать очки характеристик 2

            """
        )
