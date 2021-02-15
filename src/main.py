import pandas as pd
import numpy as np

from src.obj.command import Command


def print_main_menu():
    width = 15
    add_modifier_width = 5
    print(f'\n\nWelcome to CodeDays School-Stack Program.')
    print(f'Each command will display the first 10 rows, you can specify a specific')
    print(f'index of rows by following the command with 101:200 for instance.\n')

    print(f'Please select an option from the list below:')

    print(f'Command syntax: <command> --modifiers... <rows>')
    print(f'{"schools": <{width}} Displays schools with highest number of students.')
    print(f'{"Modifiers:": <{width + add_modifier_width}} --locationZip=num OR --locationState=state --locationCity=city')
    print(f'{"": <{width + add_modifier_width}} --free&reducedLunch=True|False --sex=Male|Female ')
    print(f'{"": <{width + add_modifier_width}} --minority=True|False --hasWebsite=True|False')
    print(f'{"info": <{width}} Displays general information about a particular statistic.')
    print(f'{"Modifiers:": <{width + add_modifier_width}} --minority=True|False --locationState=state --locationCity=city')
    print(f'{"quit": <{width}} Exits out of the program.')


if __name__ == '__main__':

    # Load Excel, Get By Sheet, And Configure DataFrame Output
    df_excel = pd.ExcelFile('../school-info.xlsx')
    df_datafinder: pd.DataFrame = df_excel.parse('ELSI Export')
    pd.set_option('display.width', 500)
    pd.set_option('display.max_columns', 18)
    df_datafinder.rename(columns={'Location Name': 'locationState', 'Location City': 'locationCity'}, inplace=True)
    df_datafinder["locationState"] = df_datafinder["locationState"].str.lower()
    df_datafinder["locationCity"] = df_datafinder["locationCity"].str.lower()

    # Command querying
    command_query = ''
    while command_query != 'quit':
        if command_query != '':
            # Create command object
            c = Command(command_query)

            # Execute command, prints results out to terminal
            c.execute(df_datafinder)
            any_key_continue = input("Press any key to go to the main menu.")

        # Main Menu & Take input
        print_main_menu()
        command_query = input("Enter a command: ")