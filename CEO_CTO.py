from dotenv import load_dotenv
load_dotenv()

import os
from tabulate import tabulate
import pandas as pd
from mysql.connector import connect

sqlcon = connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
    charset='utf8'
)
cursor = sqlcon.cursor()


def ceo_cto():
    print('What would you like to do?')
    print()
    print('1. Tasks Status')
    print('2. Sales Data')
    print('3. Company Branches\' Status')
    print('4. Salary and Attendance Details')
    print('5. Complains')
    print('6. Return to Main Menu')
    print()
    choice = int(input('Enter your choice: '))
    print()

    if choice == 1:
        tasks_status()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                ceo_cto()
                break
            elif choice1 == 'N':
                import MainMenu
                MainMenu.main_menu()
                break
            else:
                print()
                print('*** Enter a valid option. ***')
                print()

    elif choice == 2:
        sales_data()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                ceo_cto()
                break
            elif choice1 == 'N':
                import MainMenu
                MainMenu.main_menu()
                break
            else:
                print()
                print('*** Enter a valid option. ***')
                print()

    elif choice == 3:
        company_branches_status()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                ceo_cto()
                break
            elif choice1 == 'N':
                import MainMenu
                MainMenu.main_menu()
                break
            else:
                print()
                print('*** Enter a valid option. ***')
                print()

    elif choice == 4:
        salary_details()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                ceo_cto()
                break
            elif choice1 == 'N':
                import MainMenu
                MainMenu.main_menu()
                break
            else:
                print()
                print('*** Enter a valid option. ***')
                print()

    elif choice == 5:
        complains()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                ceo_cto()
                break
            elif choice1 == 'N':
                import MainMenu
                MainMenu.main_menu()
                break
            else:
                print()
                print('*** Enter a valid option. ***')
                print()

    elif choice == 6:
        import MainMenu
        MainMenu.main_menu()

    else:
        print('*** Please enter a correct option. ***')
        print()
        ceo_cto()


def tasks_status():
    query = 'SELECT * FROM TASKS_STATUS;'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['TASK', 'STATUS', 'COMMENT'], tablefmt='rst', showindex=False))


def sales_data():
    month = str.upper(input('Enter month for which you want to see the sales (jan/feb/mar/apr/may) : '))
    print()
    query = 'SELECT PRODUCT, QUANTITY FROM SALES_DATA WHERE MONTH = \'' + month + '\'; '
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['PRODUCT', 'QUANTITY'], tablefmt='rst', showindex=False))


def company_branches_status():
    query = 'SELECT * FROM COMPANY_BRANCHES_STATUS;'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['BRANCH', 'STATUS', 'COMMENT'], tablefmt='rst', showindex=False))


def salary_details():
    month = str.upper(input('Enter month (jan/feb) :'))
    print()
    query = 'SELECT EMPID, EMPNAME, WORKING_DAYS, PRESENT, SALARY FROM SALARY_DETAILS WHERE MONTH = \'' + month + '\'; '
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['EMPID', 'EMPNAME', 'TOTAL WORKING DAYS', 'NO. OF DAYS PRESENT', 'SALARY'],
                   tablefmt='rst', showindex=False))


def complains():
    query = 'SELECT * FROM COMPLAINS;'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['CUSTOMER NAME', 'MOBILE NO.', 'PRODUCT', 'COMPLAIN'], tablefmt='rst', showindex=False))
