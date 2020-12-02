import requests
link = 'https://stepic.org/media/attachments/course67/3.6.3/'  # адрес, где располагаются файлы
with open('dataset_3378_3.txt', 'r') as inf:    # из файла извлекаем ссылку на первый файл с названием следующего файла
    flink = inf.readline().strip()    # присваиваем flink значение "ссылка на файл"
r = requests.get(flink)    # присваиваем r значение которое находится в файле по ссылке flink
while "We" not in r.text:    # до тех пор, пока в файле не будет значения 'We'
    r = requests.get(link + r.text)    # мы извлекаем значение из каждого последующего файла
                                       # к которому получаем доступ по ссылке ранее
print(r.text)