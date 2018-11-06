s1 = 'Я первая строка для теста записи в файл\n'
s2 = 'А я вторая строка для тех же целей\n'

f = open(u'D:/test.txt', 'w')
f.write(s1)
f.write(s2)
f.close()

f = open(u'D:/test.txt', 'a')
f.write('Вот и третья строка нарисовалася\n')
f. close()

f = open(u'D:/test.txt', 'r')
for s in f:
    print(s)
