Для запуска проекта необходимо наличие docker и docker-compose

Порядок запуска:

1. Установите зависимости:
```commandline
pip install -r requirements.txt
```
2. Запустите СУБД PostgreSQL в docker контейнере:
```commandline
docker-compose up
```
3. Запустите скрипт, выполнив команду:
```commandline
python3 task1.py
```
4. Запустите скрипт, выполнив команду:
```commandline
python3 task2.py hours_worked.txt
```
Так же можно ввести и без имени файла:
```commandline
python3 task2.py
```
