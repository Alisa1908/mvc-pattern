#!/usr/bin/env python

class View:

    @staticmethod
    def show_clients(list):
        print(f'There are {len(list)} clients in the database: ')
        for item in list:
            print(item.info)

    @staticmethod
    def get_data(text):
        return input(f'Enter {text}:')

    @staticmethod
    def show_menu():
        print('What do you want:\n' +
              '\t (1) Show clients\n'
              '\t (2) Add client\n'
              '\t (3) Exit\n'
        )
