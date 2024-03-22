#!/usr/bin/python3

from db_manager_configuration import DBManagerConfiguration


class Parser:

    def __init__(self):
        self.current_user_input = ''

    def refine_input(self, received_input):
        data = received_input.strip()
        data_list = data.split(' ')
        return ' '.join([element.lower() for element in data_list if element])
    
    def parse(self, received_input):
        self.current_user_input = received_input
        data = self.refine_input(received_input=received_input)
        if DBManagerConfiguration.MODE == "mgmt":
            ...
        elif DBManagerConfiguration.MODE == "sql":
            ...

    def sql_parse(self, data):
        if data == 'exit':
            print("Exiting sql mode")
            return None
        else:
            ...