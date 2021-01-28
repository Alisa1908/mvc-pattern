#!/usr/bin/env python
import mysql.connector
from datetime import date

# MySQL Server
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
DATABASE = 'db'


class Client:

    def __init__(self, number=0, firstname=None, lastname=None, birthday=None):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

    @property
    def info(self):
        return f'{self.number} | {self.firstname} | {self.lastname} | {self.birthday}'

    @staticmethod
    def get_column_names():
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        cur.execute('show columns from client;')
        result = []
        for row in cur.fetchall():
            result.append(row[0])
        cur.close()
        conn.close()
        return result

    @staticmethod
    def get_clients():
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        cur.execute('select * from client')
        result = []
        for row in cur.fetchall():
            client = Client(*row)
            result.append(client)
        cur.close()
        conn.close()
        return result

    @staticmethod
    def add_client(number, firstname, lastname, birthday):
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        cur.execute(
            "insert into client values(%s, '%s', '%s', '%s')" %
            (int(number), firstname, lastname, date.fromisoformat(birthday))
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_client(number, firstname, lastname, birthday):
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        columns = Client.get_column_names()
        cur.execute(
            f"update client "
            f"set {columns[1]} = '{firstname}', "
            f"{columns[2]} = '{lastname}', "
            f"{columns[3]} = '{date.fromisoformat(birthday)}' "
            f"where {columns[0]} = {int(number)}"
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_client(number):
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        columns = Client.get_column_names()
        cur.execute(
            f"delete from client "
            f"where {columns[0]} = {int(number)}"
        )
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    # Client.update_client('1', 'gjhir', 'grwt', '2000-01-01')
    # print(Client.get_column_names())