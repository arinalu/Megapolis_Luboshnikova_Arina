# импортируем библиотеку для работы с csv файлами
import csv

#открываем файл game.csv и создаем файл game_new.csv
with open('game.csv', encoding='utf-8') as file, open('game_new.csv', 'w',  encoding='utf-8', newline='') as newfile:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(newfile, delimiter=';')
    res.writerow(data[0]) #создаем названия столбцов в game_new.csv
    print(data)
    for s in data[1:]:
        err = s[2]
        if '55' in err: #находим ошибки с содержанием числа 55. После изменяем значение ошибки на “Done”, а в поле дата ставим “0000-00-00”
            print(f'У персонажа {s[1]} в игре {s[0]} нашлась ошибка с кодом: {s[2]}. Дата фиксации: {s[3]}.')
            s[2] = 'Done'
            s[3] = '0000-00-00'
        res.writerow(s) #полученные измененные данные сохраняем в файле game_new.csv.