import pyperclip

s = pyperclip.paste()
s = s.lower()
s = s.replace(".", " ")
s = s.replace(",", " ")
s = s.replace("!", " ")
s = s.replace(":", " ")
s = s.replace(";", " ")
s = s.replace("?", " ")
s = s.replace("-", " ")
s = s.replace("\r", " ")
s = s.replace("\n", " ")
mas = s.split(" ")
dic = {}

for word in mas:
    if len(word) > 3:
        dic[word] = s.count(word)
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

q = 1
for z in dic:
    if q > 5:
        break
    q += 1
    print(z)
