import pandas as pd
import numpy as np

from src.obj.command import Command


def print_main_menu():
    width = 15
    print(f'\n\nWelcome to CodeDays School-Stack Program.')
    print(f'Each command will display the first 10 rows, you can specify a specific')
    print(f'index of rows by following the command with 101-200 for instance.\n')

    print(f'Please select an option from the list below:')

    print(f'Command syntax: <command> --modifiers... <rows>')
    print(f'{"schools": <{width}} Displays schools with highest number of students.')
    print(f'{"Modifiers:": <{width}} --minority=True|False --locationState=state --locationCity=city')
    print(f'{"": <{width}} --freelunch=True|False --sex=Male|Female --hasWebsite=True|False')
    print(f'{"info": <{width}} Displays general information about a student.')
    print(f'{"Modifiers:": <{width}} --minority=True|False --locationState=state --locationCity=city')
    print(f'{"quit": <{width}} Exits out of the program.')


if __name__ == '__main__':

    # Load Excel and Get By Sheet
    df_excel = pd.ExcelFile('../school-info.xlsx')
    df_datafinder: pd.DataFrame = df_excel.parse('ELSI Export')

    # Command querying
    command_query = ''
    while command_query != 'quit':
        if command_query != '':
            # Create command object
            c = Command(command_query)

            # Execute command, prints results out to terminal
            c.execute(df_datafinder)

        # Take input
        command_query = input("Enter a command: ")