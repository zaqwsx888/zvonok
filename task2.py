import os
from sys import argv

try:
    script, file_name = argv
except ValueError as error:
    file_name = 'hours_worked.txt'

file_path = os.path.abspath(file_name)
if not os.path.exists(file_path):
    print('Указанного файла не существует')
else:
    result = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            hours = line[-1]
            username = ' '.join(line[:-1])
            if not result.get(username):
                result[username] = [hours]
            else:
                result[username].append(hours)
    if result:
        for name, hours in result.items():
            try:
                print(name, ', '.join(hours), 'sum:', sum(map(float, hours)))
            except ValueError:
                print('Ошибка при преобразовании часов работника:', name)
