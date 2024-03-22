#!/usr/bin/python3

from datetime import datetime

from db_manager_configuration import DBManagerConfiguration
from parse import Parser


def run(parser, date_time):
    console_string = f"[({DBManagerConfiguration.MODE}){date_time}]"
    while True:
        parser.parse(input(console_string))


if __name__ == "__main__":
    print("Starting DB Manager...")
    parser = Parser()
    date_time = datetime.strftime(datetime.now(), '%Y-%m-%d:%H-%M')
    run(parser, date_time)
