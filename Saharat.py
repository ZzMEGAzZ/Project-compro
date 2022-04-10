'''This function is written by Mr.Saharat ID:6410505914'''

def vaccination(username):
    first = ""
    second = ""
    lines = open('register.txt').read().splitlines()
    data = open('register.txt').read().splitlines()
    x = 0
    for line in lines:
        user_login = []
        if line.split(',')[0] == username:
            user_login.append(data[x])
            break
        else:
            x += 1
    if user_login[0].split(',')[7] == "N" and user_login[0].split(',')[8] == "N":
        if int(user_login[0].split(',')[4]) < 18:
            print("We advice Pfizer for your first dose as it's the only vaccine authorized for younger age groups.")
        else:
            print("We advice Moderna for your first dose.")
    elif user_login[0].split(',')[7] == "Y" and user_login[0].split(',')[8] == "N":
        vaccine_menu1()
        first = input(str("Which vaccine is your first dose?: "))
        while first != "1" and first != "2" and first != "3" and first != "4" and first != "5" :
            vaccine_menu1()
            print("Please enter a valid choice.")
            first = input(str("Which vaccine is your first dose?: "))
        vaccine_menu2()
        second = input("Which vaccine is your second dose?: ")
        while second != "1" and second != "2" and second != "3" and second != "4" and second != "5" and second != "6":
            vaccine_menu2()
            print("Please enter a valid choice.")
            second = input("Which vaccine is your first dose?: ")
    else:
        print(f"You are fully vaccinated.")

    
    if first == "1" or first == "3" or first == "5":
        if second != "6":
            print("You booster dose is pfiizer or moderna.")
        else:
            print("A second dose is Sinovac or Sinnpharm or AstraZeneca")
    elif first == "2":
        if second != "6":
            print("You booster dose is pfiizer or moderna.")
        else:
            print("A second dose is AstraZeneca")
    elif first == "4":
        if second != "6":
            print("You booster dose is pfiizer or moderna.")
        else:
            print("A second dose is pfiizer or moderna.")
            
def vaccine_menu1():
    print("---- First dose ----")
    print("1.Sinovac")
    print("2.AstraZeneca")
    print("3.Sinopharm")
    print("4.Pfizer")
    print("5.etc.")
    print("--------------------")
def vaccine_menu2():
    print("--- Second dose ---")
    print("1.Sinovac")
    print("2.AstraZeneca")
    print("3.Sinopharm")
    print("4.Pfizer")
    print("5.etc.")
    print("6.-")
    print("-------------------")
  