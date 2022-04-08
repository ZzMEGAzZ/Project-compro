'''Group No.
Project title: Covid-19
Subject: 1204111
Semester: 02-2564
Section: 6/16
Project Members:
1.Mr.Kristikorn ID:6410505442
2.Mr.Saharat ID:6410505914
3.Mr.Suwichan ID:6410505442
4.Ms.Yosita ID:6410505817
'''

import Kristikorn as reg
import Saharat as vac
import Suwichan as sym
import Yosita as stat

def main():
    while True:
        login = input("Do you want to register or login ? (R/L): ").upper()
        if login == "R":
            username = reg.register()
            print("Your username is: ", username)
        else:
            if reg.login() == True:
                reg.show_menu()
                while True:
                    try:
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            print("Vaccination")
                            vac.vaccination()
                        elif choice == 2:
                            print("Symptoms")
                            sym.symptoms()
                        elif choice == 3:
                            print("Statistics")
                            stat.statistics()
                        elif choice == 4:
                            print("Exit")
                            return False
                        else:
                            print("Please enter a valid choice")
                    except ValueError:
                        print("Please enter a valid choice")
            else:
                print("Please try again later")
                return False


main()
