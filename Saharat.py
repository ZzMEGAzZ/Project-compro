'''This function is written by Mr.Saharat ID:6410505914'''

def vaccination():
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[7] == "Y" and line.split(',')[8] == "Y":
            print(f"You are fully vaccinated.")
        elif line.split(',')[7] == "N" and line.split(',')[8] == "N":
          if line.split(',')[4] < 18:
            "We advice Pfizer for your first dose as it's the only vaccine authorized for younger age groups."
          else:
            "We advice Moderna for your first dose."
        elif line.split(',')[7] == "Y" and line.split(',')[8] == "N":
          vaccine_menu1()
          first = input("Which vaccine is your first dose?: ")
          while first != "1" and first != "2" and first != "3" and first != "4" and first != "5" :
            print("Please enter a valid choice.")
            first = input("Which vaccine is your first dose?: ")
          vaccine_menu2()
          second = input("Which vaccine is your second dose?: ")
          while second != "1" and second != "2" and second != "3" and second != "4" and second != "5" and second != "6":
            print("Please enter a valid choice.")
            second = input("Which vaccine is your first dose?: ")
          return first, second
            
        
          
        
def vaccine_menu1():
    print("----------------")
    print("1.Sinovac")
    print("2.AstraZeneca")
    print("3.Sinopharm")
    print("4.Pfizer")
    print("5.etc.")
    print("----------------")
def vaccine_menu2():
    print("----------------")
    print("1.Sinovac")
    print("2.AstraZeneca")
    print("3.Sinopharm")
    print("4.Pfizer")
    print("5.etc.")
    print("6.-")
    print("----------------")
  
def vac_choice(first, second):
    if first == "1" or first == "3":
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
