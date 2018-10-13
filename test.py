characters = {"Сила": 0, "Здоровье": 0, "Мудрость": 0, "Ловкость": 0}
points = 30

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
    selectCharacter = ""
    selectPoint = 0
    while selectCharacter != "готово":
        selectCharacter = input("Введите характеристику в которую вы хотите добавить очки: ")
        selectPoint = int(input("Введите количество очков: "))
        if selectCharacter == "Сила":
            characters[selectCharacter] += selectPoint
            points -= selectPoint
        elif selectCharacter == "Здоровье":
            characters[selectCharacter] += selectPoint
            points -= selectPoint
