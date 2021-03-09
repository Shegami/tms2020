lst = []
sr1, sr2, sr3 = (0 for i in range(3))
with open('dataset_3363_4.txt', 'r') as inf:
    lst += (i.strip().split(';') for i in inf) # в список lst добавляем строки из файла удаляя сл. символы, с разделителем ;
[lst.remove(['']) for i in lst if [''] in lst] # если в файле была пустая строка - убираем её
x = len(lst)
with open('Marks.txt', 'w') as mar: # создаём новый файл в который записываем нужные значения
    lst0 = [(mar.write(str(((int(b) + int(c) + int(d)) / 3))), mar.write('\n')) for a, b, c, d in lst] # используем кортеж
    # каждый элемент каждого подсписка lst именуем, как a, b, c, d. С помощью list comprehension сумируем оценки
    # и сразу записываем их построчно в файл
    sr1 = [int(lst[i][1]) for i in range(x)] # высчитыем сумму оценок по первому предмету среди всех учеников
    mar.write(str(sum(sr1) / len(sr1))) # записываем среднее
    sr2 = [int(lst[i][2]) for i in range(x)] # по второму
    (mar.write(' '), mar.write(str(sum(sr2) / len(sr2))))
    sr3 = [int(lst[i][3]) for i in range(x)] # по третьему
    (mar.write(' '), mar.write(str(sum(sr3) / len(sr3))))