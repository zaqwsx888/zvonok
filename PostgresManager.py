import os
import psycopg2
from psycopg2 import Error
from psycopg2 import extras


class PostgresManager:
    """Класс для работы с СУБД PostgreSQL"""
    __instance = None
    __host = None
    __user = None
    __password = None
    __database = None
    __cursor = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
            cls.__instance = super(
                PostgresManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(
            self, host='localhost', user='postgres', password='postgres',
            database='postgres', port=5432
    ):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__port = port

    def __open(self):
        """Метод подключения к PostgreSQL"""
        try:
            self.__connection = psycopg2.connect(
                host=self.__host, user=self.__user, password=self.__password,
                database=self.__database, port=self.__port
            )
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor(
                cursor_factory=extras.RealDictCursor)
        except (Exception, Error) as error:
            if self.__connection:
                self.__connection.rollback()
            print('Ошибка при работе с PostgreSQL:', error)

    def __close(self):
        """Метод закрытия соединения с PostgreSQL"""
        self.__connection.close()

    def query(
            self, query=None, file_name=None, executescript=False,
            fetchone=False, fetchall=False
    ):
        """Метод выполнения запросов в базу данных"""
        try:
            data = False
            if query or executescript:
                self.__open()
                data = True
                if query:
                    self.__cursor.execute(query)
                elif file_name and executescript:
                    file_path = os.path.abspath(file_name)
                    if not os.path.exists(file_path):
                        self.__cursor.close()
                        print('Указанного файла не существует')
                        return False
                    self.__cursor.execute(
                        open(os.path.abspath('sql_query.sql'), 'r').read())
                if fetchone:
                    data = self.__cursor.fetchall()
                elif fetchall:
                    data = self.__cursor.fetchall()
                self.__cursor.close()
            return data
        except (Exception, Error) as error:
            self.__cursor.close()
            print('Ошибка при работе с PostgreSQL', error)
            return False
