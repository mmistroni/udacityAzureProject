# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyodbc

def print_hi(name):
    server = 'myudacityserver.database.windows.net'
    database = 'myudacitydb'
    username = 'udacityadmin'
    password = 'M15tr0n1'
    driver_names = [x for x in pyodbc.drivers() if 'SQL Server' in x]
    driver = driver_names[0]
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT id, name, description from dbo.ANIMALS')
    for row in cursor.fetchall():
        print(str(row[0]) + " " + str(row[1]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
