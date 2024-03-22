#!/usr/bin/python3

from datetime import datetime

from db_manager_configuration import DBManagerConfiguration
from parse import Parser


def run(parser):
    console_string = f"[({DBManagerConfiguration.MODE}){
        datetime.strftime(datetime.now(), '%Y-%m-%d:%H-%M')}]"
    while True:
        parser.parse(input(console_string))


if __name__ == "__main__":
    print("Starting DB Manager...")
    parser = Parser()
    run(parser)
