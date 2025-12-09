from Member_Of_Staff import *


def client():
    print('What would you like to do?')
    print()
    print('1. Show Product List')
    print('2. Order Placement')
    print('3. Register Complain')
    print('4. Return to Main Menu')
    print()
    choice = int(input('Enter your choice: '))
    print()

    if choice == 1:
        product_list()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                client()
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
        order_placement()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                client()
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
        register_complain()
        print()
        for x in range(10):
            choice1 = str.upper(input('Would you like to do another task?(Y) or Return to Main Menu?(N) '))
            if choice1 == 'Y':
                print()
                client()
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
        import MainMenu
        MainMenu.main_menu()

    else:
        print('*** Please enter a correct option. ***')
        print()
        client()


def product_list():
    query = 'SELECT DISTINCT PRODUCT FROM SALES_DATA;'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    print(tabulate(df, headers=['PRODUCTS'], tablefmt='rst', showindex=False))


def order_placement():
    cname = str(input('Enter your name : '))
    cmno = int(input('Enter your mobile no. : '))
    product_list()
    product = str(input('Enter the product you want to buy : '))
    quantity = int(input('Enter quantity : '))
    print()
    query = ('INSERT INTO ORDER_MANAGEMENT VALUES(\'' + cname + '\', ' + str(cmno) + ', \'' + product + '\', ' +
             str(quantity) + ');')
    cursor.execute(query)
    sqlcon.commit()
    print('Order placed successfully!')
    print('Thank you for your immense trust for our company.')
    print('Your order will be processed ASAP... ')
    print('Further details will be communicated to you on your specified mobile number.')


def register_complain():
    cname = str(input('Enter your name : '))
    cmno = int(input('Enter your mobile no. : '))
    product = str(input('Enter product you want to register the complain for : '))
    complain = str(input('Enter complain : '))
    print()
    query = ('INSERT INTO COMPLAINS VALUES(\'' + cname + '\', ' + str(cmno) + ', \'' + product + '\', \'' +
             complain + '\');')
    cursor.execute(query)
    sqlcon.commit()
    print('Complain registered successfully.')
    print('We regret the inconvenience.')
    print('Your complain will be resolved by our team ASAP...')
    print('Further details will be messaged to you on your specified number.')
