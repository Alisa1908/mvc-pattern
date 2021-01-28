#!/usr/bin/env python

import mysql.connector
import unittest
from datetime import date
from model import Client
from settings import USERNAME, PASSWORD, HOST, DATABASE


class TestClient(unittest.TestCase):

    def check_count(self):
        conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
        cur = conn.cursor()
        cur.execute('select count(*) from Client')
        res = cur.fetchone()
        cur.close()
        conn.close()
        return res[0]

    def get_last_number(self):
        return max(Client.get_clients(), key=lambda client: client.number).number

    def test_get_clients(self):
        self.assertEqual(self.check_count(), len(Client.get_clients()))

    def test_add_client(self):
        count = self.check_count()
        number = self.get_last_number() + 1
        Client.add_client(number, 'First', 'Last', '2020-02-02')
        self.assertEqual(self.check_count(), count + 1)
        for client in Client.get_clients():
            if client.number == number:
                self.assertEqual(client.firstname, 'First')
                self.assertEqual(client.lastname, 'Last')
                self.assertEqual(client.birthday, date.fromisoformat('2020-02-02'))

    def test_update_client(self):
        number = self.get_last_number() + 1
        Client.add_client(number, 'Abc', 'Def', '2000-01-01')
        count = self.check_count()
        Client.update_client(number, 'Abb', 'Dee', '2001-02-03')
        self.assertEqual(self.check_count(), count)
        for client in Client.get_clients():
            if client.number == number:
                self.assertEqual(client.firstname, 'Abb')
                self.assertEqual(client.lastname, 'Dee')
                self.assertEqual(client.birthday, date.fromisoformat('2001-02-03'))

    def test_delete_client(self):
        number = self.get_last_number() + 1
        Client.add_client(number, 'A', 'B', '2000-01-01')
        count = self.check_count()
        Client.delete_client(number)
        self.assertEqual(self.check_count(), count - 1)
        for client in Client.get_clients():
            if client.number == number:
                self.assertFalse('Client was not deleted')


