from CEO_CTO import ceo_cto
from Member_Of_Staff import member_of_staff
from Client import client
from Exit import Exit


def main_menu():

    print()
    print('********************************')
    print('||||||||||||||||||||||||||||||||')
    print('HOLA AMIGO!')
    print('WELCOME TO JS INFO-TECH Pvt. Ltd.')
    print('||||||||||||||||||||||||||||||||')
    print('********************************')

    for x in range(5, -1, -1):
        print()
        print('What would you like to do?')
        print()
        print('1. Login as CEO/CTO')
        print('2. Login as Member of Staff')
        print('3. Login as Client')
        print('4. Exit')
        print()
        choice = int(input('Enter the adjacent number of your desired choice : '))

        if choice == 1:
            for i in range(3, -1, -1):
                passwd = int(input('Enter the numeric password : '))
                if passwd == 150905:
                    print()
                    print('Welcome Boss!')
                    ceo_cto()
                    break
                else:
                    print()
                    print('*** Incorrect password!', i, 'tries left. ***')
                    print()
            break

        elif choice == 2:
            for j in range(3, -1, -1):
                passwd = int(input('Enter the numeric password : '))
                if passwd == 123456:
                    print()
                    print('Welcome!')
                    member_of_staff()
                    break
                else:
                    print()
                    print('*** Incorrect password!', j, 'tries left. ***')
                    print()
            break

        elif choice == 3:
            print()
            print('Welcome!')
            client()
            break

        elif choice == 4:
            Exit()
            break

        else:
            print()
            if x != 0:
                print('*** Enter a valid option.', x, 'tries remaining... ***')
            else:
                print('You failed to enter any correct value. Try again later.')
