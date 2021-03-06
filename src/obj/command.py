from __future__ import annotations
from src.obj.modifier import Modifier

import pandas as pd
from uszipcode import SearchEngine


class Command:
    valid_commands = ('schools', 'info')

    def __init__(self, command: str):
        self.split_command = command.split(" ")
        if self.is_valid():
            self.command = self.split_command[0]
            self.row_start = 0
            self.row_end = 10
            if ':' in self.split_command[len(self.split_command) - 1]:
                # Last argument is a row specifier
                rows = self.split_command[len(self.split_command) - 1].split(':')
                self.row_start = int(rows[0])
                self.row_end = int(rows[1])
                print(self.split_command)
                self.split_command.pop()
                print(self.split_command)
            self.modifiers = Modifier.create_list_from_input(self.split_command)

    def is_valid(self) -> bool:
        if self.split_command[0].startswith(Command.valid_commands):
            return True
        return False

    def execute(self, data: pd.DataFrame):
        if self.command in self.valid_commands:
            organized_dataframe: pd.DataFrame = data
            # Doing a query is for filtering based on row values like location
            query = ""
            searched_by_zip = False
            # Doing a group by is for filtering based on a column heading like # of male students
            sort_by = []
            for item in self.modifiers:
                # All modifiers below are for the query function
                if item.name == 'locationZip':
                    search = SearchEngine(simple_zipcode=True)
                    zipcode = search.by_zipcode(item.value)
                    query += f'locationState == "{zipcode.state_long.lower()}" and ' \
                             f'locationCity == "{zipcode.major_city.lower()}"'
                    searched_by_zip = True
                elif item.name == 'locationCity' or item.name == 'locationState':
                    query += f'{item.name} == "{item.value}" and '
                    print(query)
                # All modifiers below are for the sort_values function
                elif item.name == 'minority':
                    sort_by.extend(['American Indian/Alaska Native Students',
                                    'Asian or Asian/Pacific Islander Students', 'Hispanic Students',
                                    'Black Students', 'Hawaiian Nat./Pacific Isl. Students',
                                    'Free & Reduced Lunch Students'])
                elif item.name == 'sex':
                    if item.value == 'Male':
                        sort_by.extend(['Male Students'])
                    else:
                        sort_by.extend(['Female Students'])
                elif item.name == 'free&reducedLunch':
                    sort_by.extend(['Free & Reduced Lunch Students']) if item.value else item.value
                if item.name == 'hasWebsite':
                    if item.value == 'true':
                        organized_dataframe = organized_dataframe.dropna(subset=['Web Site URL'])
                    else:
                        organized_dataframe = organized_dataframe[organized_dataframe['Web Site URL'].isnull()]

            # Only query if there are actual modifiers given by user
            if len(query) >= 1:
                new_query = query
                if not searched_by_zip:
                    new_query = query[:len(query) - 5]
                print(new_query)
                organized_dataframe = organized_dataframe.query(new_query)
                if len(sort_by) >= 1:
                    organized_dataframe = organized_dataframe.sort_values(by=sort_by, ascending=False,
                                                                          ignore_index=True)
            # Only sort_values if there are actual modifier values given by user
            elif len(sort_by) >= 1:
                organized_dataframe = organized_dataframe.sort_values(by=sort_by, ascending=False, ignore_index=True)

            print(organized_dataframe.iloc[self.row_start:self.row_end, :])
