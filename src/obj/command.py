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
            # Doing a query is for filtering based on row values like location
            query = ''

            # Doing a group by is for filtering based on a column heading like # of male students
            group_by = []
            for item in self.modifiers:
                if isinstance(item.value, str):
                    query += f'{item.name} == {item.value} and'
                elif item.name == 'minority':
                    # Add up all minorities
                    group_by.extend(["Female Students", "American Indian/Alaska Native Students",
                                     "Asian or Asian/Pacific Islander Students", "Hispanic Students",
                                     "Black Students", "Hawaiian Nat./Pacific Isl. Students",
                                     "Free & Reduced Lunch Students"])
                elif item.name == 'sex':
                    if item.value == 'Male':
                        group_by += 'Male'
                    else:
                        group_by += 'Female'
                elif item.name == 'free&reducedLunch':
                    group_by += "Free & Reduced Lunch Students" if item.value else item.value
                if item.name == "hasWebsite":
                    pass

            if len(query) > 5:
                query.removesuffix(" and")
                data.query(query, inplace=True)

            data.sort_values(group_by, ascending=False, inplace=True)
            print(data)
