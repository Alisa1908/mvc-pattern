#!/usr/bin/env python

import mysql.connector
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io
from datetime import date
from model import Client
from view import View
from controller import Controller
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


class TestView(unittest.TestCase):

    def test_show_clients(self):
        client1 = Client(123, 'Aaaaa', 'Bbbbb', '2001-01-01')
        client2 = Client(456, 'Ccccc', 'Ddddd', '2002-02-02')
        clients = [client1, client2]
        f = io.StringIO()
        with redirect_stdout(f):
            View.show_clients(clients)
        s = f.getvalue()
        self.assertIn('2 client', s)
        self.assertIn('123', s)
        self.assertIn('456', s)
        self.assertIn('Aaaaa', s)
        self.assertIn('Bbbbb', s)
        self.assertIn('Ccccc', s)
        self.assertIn('Ddddd', s)
        self.assertIn('2001-01-01', s)
        self.assertIn('2002-02-02', s)

    @patch('builtins.input', return_value='entered')
    def test_get_data(self, input):
        self.assertEqual(View.get_data('something'), 'entered')

    def test_show_menu(self):
        f = io.StringIO()
        with redirect_stdout(f):
            View.show_menu()
        s = f.getvalue()
        self.assertIn('Show', s)
        self.assertIn('Add', s)
        self.assertIn('Update', s)
        self.assertIn('Delete', s)
        self.assertIn('Exit', s)


class TestController(unittest.TestCase):

    def get_last_number(self):
        return max(Client.get_clients(), key=lambda client: client.number).number

    def test_show_clients(self):
        number = self.get_last_number() + 1
        Client.add_client(number, 'Testing', 'Controller', '2003-11-11')
        f = io.StringIO()
        with redirect_stdout(f):
            Controller().show_clients()
        s = f.getvalue()
        self.assertIn('Testing', s)
        self.assertIn('Controller', s)
        self.assertIn('2003-11-11', s)

    @patch('builtins.input', return_value='')
    def test_add_client(self, input):
        f = io.StringIO()
        with redirect_stdout(f):
            with self.assertRaises(ValueError):
                Controller().add_client()

    @patch('builtins.input', return_value='')
    def test_update_client(self, input):
        f = io.StringIO()
        with redirect_stdout(f):
            with self.assertRaises(ValueError):
                Controller().update_client()

    @patch('builtins.input', return_value='')
    def test_delete_client(self, input):
        f = io.StringIO()
        with redirect_stdout(f):
            with self.assertRaises(ValueError):
                Controller().delete_client()

    @patch('builtins.input', return_value='5')
    def test_run(self, input):
        f = io.StringIO()
        with redirect_stdout(f):
            Controller().run()
        self.assertTrue(True)