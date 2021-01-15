import csv


def csv_read(filename):
    rows = []
    with open(filename) as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            rows.append(row)
    fields = rows[0]
    data = rows[1:]
    return fields, data


def csv_write(filename, fields, data):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)


def csv_add_row(filename, row, position=-1):
    fields, data = csv_read(filename)
    if position == -1:
        data.append(row)
    else:
        data.insert(position - 1, row)
    csv_write(filename, fields, data)


def csv_pop_row(filename, position=-1):
    fields, data = csv_read(filename)
    if position == -1:
        data.pop()
    else:
        data.pop(position - 1)
    csv_write(filename, fields, data)


def csv_goods_sum(filename):
    fields, data = csv_read(filename)
    goods_sum = 0
    for i in range(len(data)):
        goods_sum += int(data[i][2])
    return goods_sum


def csv_goods_expensive(filename):
    fields, data = csv_read(filename)
    most_expensive = float(data[0][1])
    for i in range(1, len(data)):
        if most_expensive < float(data[i][1]):
            most_expensive = float(data[i][1])
    return most_expensive


def csv_goods_cheapest(filename):
    fields, data = csv_read(filename)
    cheapest = float(data[0][1])
    for i in range(1, len(data)):
        if cheapest > float(data[i][1]):
            cheapest = float(data[i][1])
    return cheapest


def csv_goods_reduce(filename, quantity=1):
    fields, data = csv_read(filename)
    for row in range(len(data)):
        print(f'{row + 1} {data[row][0]}')
    choice = int(input('Выберите номер товара: ')) - 1
    if quantity > int(data[choice][2]):
        print('Ошибка. Указанное кол-во больше, чем кол-во товара.')
    else:
        data[choice][2] = str(int(data[choice][2]) - quantity)
    csv_write(filename, fields, data)


def csv_age_sort(data_input, data_output):
    for i in range(len(data_input)):
        if data_input[i][2] < 13:
            data_output[0][0] += 1
        elif 12 < data_input[i][2] < 19:
            data_output[0][1] += 1
        elif 18 < data_input[i][2] < 26:
            data_output[0][2] += 1
        elif 25 < data_input[i][2] < 41:
            data_output[0][3] += 1
        else:
            data_output[0][4] += 1
    return data_output
