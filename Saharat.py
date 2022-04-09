'''This function is written by Mr.Saharat ID:6410505914'''

def vaccination():
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[7] == "Y" and line.split(',')[8] == "Y":
            print(f"You are fully vaccinated.")
            return True
        elif line.split(',')[7] == "N" and line.split(',')[8] == "N":
          if line.split(',')[4] < 18:
            "We advice Pfizer for your first dose as it's the only vaccine authorized for younger age groups."
          else:
            "We advice Moderna for your first dose."
        elif line.split(',')[7] == "Y" and line.split(',')[8] == "N":
          first = input("Which vaccine is your first dose?: ")
          vaccine_menu1()
          second = input("Which vaccine is your second dose?: ")
          vaccine_menu2()
        
          
        
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