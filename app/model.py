#!/usr/bin/env python
import mysql.connector
from datetime import date

# MySQL Server
USERNAME = 'u01'
PASSWORD = 'u01'
HOST = 'nix'
DATABASE = 'db01'


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
    def get_clients():
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        result = []
        for row in cur.execute('select * from client'):
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
            'insert into client values(%s, %s, %s, %s)' %
            (int(number), firstname, lastname, date.fromisoformat(birthday))
        )
        conn.commit()
        cur.close()
        conn.close()
