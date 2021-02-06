from __future__ import annotations
from src.obj.modifier import Modifier

import pandas as pd
from uszipcode import SearchEngine


class Command:
    valid_commands = ("schools", "info", "quit")

    def __init__(self, command: str):
        self.split_command = command.split(" ")
        if self.is_valid():
            self.command = self.split_command[0]
            self.modifiers = Modifier.create_list_from_input(self.split_command)
            print(self.modifiers[0].name, self.modifiers[0].value)

    def is_valid(self) -> bool:
        if self.split_command[0].startswith(Command.valid_commands):
            return True
        return False

    def execute(self, data: pd.DataFrame):
        if self.command == 'schools':
            query = ''
            for item in self.modifiers:
                if item.name == 'minority':
                    
                query += f'{item.name} == {item.value} and'

            data.query(query, inplace=True)
            print(data)
