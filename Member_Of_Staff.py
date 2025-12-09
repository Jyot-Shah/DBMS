from CEO_CTO import *


def member_of_staff():
    print('What would you like to do?')
    print()
    print('1. Tasks Status')
    print('2. Order Management')
    print('3. Attendance Details')
    print('4. Complains')
    print('5. Return to Main Menu')
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
                member_of_staff()
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
        order_management()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                member_of_staff()
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
        attendance_details()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                member_of_staff()
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
        complains()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                member_of_staff()
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
        import MainMenu
        MainMenu.main_menu()

    else:
        print('*** Please enter a correct option. ***')
        print()
        member_of_staff()


def order_management():
    query = 'SELECT * FROM ORDER_MANAGEMENT;'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['CUSTOMER NAME', 'MOBILE NO.', 'PRODUCT', 'QUANTITY'], tablefmt='rst', showindex=False))


def attendance_details():
    empid = int(input('Enter your employee ID : '))
    print()
    query = 'SELECT EMPID, EMPNAME, MONTH, WORKING_DAYS, PRESENT FROM SALARY_DETAILS WHERE EMPID = ' + str(empid) + ';'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['EMPID', 'EMPNAME', 'MONTH', 'TOTAL WORKING DAYS', 'NO. OF DAYS PRESENT'],
                   tablefmt='rst', showindex=False))
