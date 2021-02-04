import pandas as pd
import numpy as np


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





if __name__ == '__main__':
    df_excel = pd.ExcelFile('../school-info.xls')
    df_datafinder = df_excel.parse('ELSI Export')
    print_main_menu()
    print(df_datafinder.columns)
    print(df_datafinder.info())
    print(df_datafinder.describe())
    command = ''


