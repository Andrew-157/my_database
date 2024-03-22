#!/usr/bin/python3

from common.utilities import raise_error
from db_manager_configuration import DBManagerConfiguration
from mgmt_operations.mgmt_operation_configuration import MGMTOperationsConfiguration


class Parser:

    def __init__(self):
        self.current_user_input = ''

    def refine_input(self, received_input):
        data = received_input.strip()
        data_list = data.split(' ')
        return ' '.join([element.lower() for element in data_list if element])

    def parse(self, received_input, date_time):
        self.current_user_input = received_input
        data = self.refine_input(received_input=received_input)
        if DBManagerConfiguration.MODE == "mgmt":
            ...
        elif DBManagerConfiguration.MODE == "sql":
            ...

    def sql_parse(self, data):
        ...

    def mgmt_parse(self, data, date_time):
        supposed_command = data.split(' ')[0]
        if supposed_command not in MGMTOperationsConfiguration.COMMANDS_MAPPING.keys():
            error_reason = f"Command you provided: {
                supposed_command} is not supported."
            raise_error(mode='mgmt', user_input=self.current_user_input,
                        time_of_error=date_time, error_reason=error_reason)
            return None
        else:
            ...
