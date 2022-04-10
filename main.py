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
        lines = open('register.txt').read().splitlines()
        if lines == "" or lines == []:
            print("--- Registering new user ---")
            username = reg.register()
            print(f"Your username is: {username}")
        else:
            login = input("Do you want to register or login ? (R/L): ").upper()
            if login == "R":
                username = reg.register()
                if username == False:
                    print("You have failed to register please try again")
                else:
                    print(f"Your username is: {username}")
            else:
                if reg.login() == True:
                    while True:
                        show_menu()
                        if select_menu() == False:
                            break
                    break
                else:
                    print("Please try again later")
                    return False

def show_menu():
    print("\n")
    print("----- Menu -----")
    print("1. Vaccination")
    print("2. Symptoms Check")
    print("3. Statistics")
    print("4. Exit")
    print("----------------")

def select_menu():
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Vaccination")
            first, second = vac.vaccination()
            vac.vac_choice(first, second)
        elif choice == 2:
            print("Symptoms")
            count = sym.symptoms_analysis()
            print("\n")
            sym.covid_checked(count)
        elif choice == 3:
            print("Statistics")
            stat.statistics_total_health_area()
        elif choice == 4:
            print("Exit")
            return False
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid choice")
        


main()
