#!/usr/bin/python3

from datetime import datetime

from db_manager_configuration import DBManagerConfiguration


class Session:

    def run(self):
        console_string = f"[({DBManagerConfiguration.MODE})\
            {datetime.strftime(datetime.now(), '%Y-%m-%d:%H-%M')}]"
        print("Starting DB Manager 3000...")
        while True:
            user_input = input(console_string)
