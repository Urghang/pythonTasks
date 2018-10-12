def showHelp():
    # показываем справку
    print("В качестве ответа на вопрос компьютера используйте символы < (меньше), > (больше) и = (равно).")

numBegin = 0
numEnd = 100

# создаем список
listNum = [i for i in range(numBegin, numEnd + 1)]

print("Задумайте число от", numBegin, "до", numEnd)
showHelp()

answer = ""
while answer != "=":
    # попытка компьютера
    res = (min(listNum) + max(listNum)) // 2
    print("Компьютер: Вы задумали ", res, "?", sep="")
    answer = input("Вы: ")

    if answer ==">":
        # генерируем список
        listNum = [i for i in listNum if i > res]
    elif answer == "<":
        listNum = [i for i in listNum if i < res]
    elif answer == "=":
        print("Компьютер: Ура! Я отгадал задуманное Вами число!")
    else:
        showHelp()

input("Нажмите enter для выхода")
