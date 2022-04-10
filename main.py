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
from pickle import FALSE
import time
import Kristikorn as reg
import Saharat as vac
import Suwichan as sym
import Yosita as stat


def main():
    username = ""
    print("\n")
    print("\n")
    print("-----wellcome to Covid-19 Project-----")
    while True:
        lines = open('register.txt').read().splitlines()
        if lines == [] or lines == [''] or lines == ['\n']:
            username = reg.register()
            print(f"Your username is: {username}")
        else:
            print("Do you want to register or login or modified account ? (R/L/M)")
            login = input("Enter your answer: ").upper()
            if login == "R":
                username = reg.register()
                if username == False:
                    print("You have failed to register please try again")
                else:
                    print(f"Your username is: {username}")
            elif login == "L":
                username = reg.login()
                if username == False :
                    print("You have failed to login 3 times. Please try again later.")
                    break
                while True:
                    show_menu()
                    if select_menu(username) == False:
                        break
                break
            elif login == "M":
                print("***Modified account***")
                delete = input("Modified account must be delete your data and register again do you want to modified account ? (Y/N): ").upper()
                if delete == "Y":
                    delete_user()
                    

def show_menu():
    print("\n")
    print("----- Menu -----")
    print("1. Vaccination")
    print("2. Symptoms Check")
    print("3. Statistics")
    print("0. Exit")
    print("----------------")

def select_menu(username):
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Vaccination")
            vac.vaccination(username)
        elif choice == 2:
            print("Symptoms")
            count = sym.symptoms_analysis()
            print("\n")
            sym.covid_checked(count)
        elif choice == 3:
            print("Statistics")
            stat.statistics()
        elif choice == 0:
            print("Exit")
            return False
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid choice")

def delete_user():
    print("Please login")
    username = reg.login()
    time.sleep(3)
    print("...")
    time.sleep(3)
    reg.modified_data(username)
    print("Modified account successfully")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Please register again")
    time.sleep(2)
    reg.register()
        
main()


