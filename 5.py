# импортируем библиотеку для работы с csv файлами
import csv

alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:-'
d_for_hash = {alf[i]: i + 1 for i in range(64)}

#функция делает хэширование строки, поданной на вход
def hash(stroke):
    p = 65
    m = 10**9 + 9
    value = 0
    i = 0
    for c in stroke:
        value += d_for_hash[c] * p**i
        i += 1
    return value % m


#открываем файл game.txt и создаем файл game_with_hash.csv
with open('game.txt', encoding='utf-8') as file, open('game_with_hash.csv', 'w',  encoding='utf-8', newline='') as newfile:
    data = list(csv.reader(file, delimiter='$'))
    res = csv.writer(newfile, delimiter='$')
    res.writerow(data[0])  # создаем названия столбцов в game_new.csv
    for s in data[1:]: #хэшируем строку
        gamename = s[0].replace(' ', '').replace("'", "").replace('.', '')
        name = s[1]
        h = hash(gamename + name)
        temp = [h, s[0], s[1], s[2], s[3]]
        res.writerow(temp) #записываем результат в новый файл