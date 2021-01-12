import csv


def csv_read(filename):
    rows = []
    with open(filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        for row in csvreader:
            rows.append(row)
        fields = rows[0]
        data = rows[1:]
    return fields, data


def csv_write(filename, fields, data):
    with open(filename, 'w') as my_file:
        csvwriter = csv.writer(my_file)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)


def csv_insert(filename, new_row, place=-1):
    fields, data = csv_read(filename)
    if place == -1:
        data.append(new_row)
    else:
        data.insert(place-1, new_row)
    csv_write(filename, fields, data)


def csv_pop(filename, place=-1):
    fields, data = csv_read(filename)
    if place == -1:
        data.pop()
    else:
        data.pop(place-1)
    csv_write(filename, fields, data)


def main():
    csv_insert('12312.txt', ['Andrei', 'GAGA'], 1)
    csv_pop('12312.txt', 1)


if __name__ == '__main__':
    main()
