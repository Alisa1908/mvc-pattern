#!/usr/bin/env python

from model import Client
from view import View


class Controller:

    def show_clients(self):
        clients = Client.get_clients()
        View.show_clients(clients)

    def add_client(self):
        number = View.get_data('number')
        firstname = View.get_data('firstname').capitalize()
        lastname = View.get_data('lastname').capitalize()
        birthday = View.get_data('birthday')
        Client.add_client(number, firstname, lastname, birthday)

    def update_client(self):
        number = View.get_data('number of client to update')
        firstname = View.get_data('firstname').capitalize()
        lastname = View.get_data('lastname').capitalize()
        birthday = View.get_data('birthday')
        Client.update_client(number, firstname, lastname, birthday)

    def delete_client(self):
        number = View.get_data('number of client to delete')
        Client.delete_client(number)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.show_clients(),
            2: lambda: self.add_client(),
            3: lambda: self.update_client(),
            4: lambda: self.delete_client()
        }
        while choice != 5:
            View.show_menu()
            choice = int(View.get_data('choice option'))
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    Controller().run()
