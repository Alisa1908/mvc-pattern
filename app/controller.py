#!/usr/bin/env python

from model import Client
from view import View


class Controller:

    def show_clients(self):
        clients = Client.get_clients()
        return View.show_clients()

    def add_client(self):
        number = View.get_data('number')
        firstname = View.get_data('firstname')
        lastname = View.get_data('lastname')
        birthday = View.get_data('birthday')
        client = Client.add_client(number, firstname, lastname, birthday)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.show_clients(),
            2: lambda: self.add_client()
        }
        while choice != 3:
            View.show_menu()
            choice = int(View.get_data('choice option'))
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    Controller().run()