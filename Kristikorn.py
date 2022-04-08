'''This function is written by Mr.Kristikorn ID:6410505442'''


def register():
    print("||||| Adding New User |||||")
    first = input("First Name: ")
    last = input("Last name: ")
    username = first+' '+last
    age = input("Enter your age: ")
    password = input("Password: ")
    vac = input("Have you vaccinated ? (Y/N): ").upper()
    while vac != "Y" and vac != "N":
        vac = input("Have you vaccinated ? (Y/N): ").upper()
    vac_booster = input("Have you got a booster ? (Y/N): ").upper()
    while vac_booster != "Y" and vac_booster != "N":
        vac_booster = input("Have you got a booster ? (Y/N): ").upper()
    line = username+','+password+','+age+','+vac+','+vac_booster
    lines = open('register.txt').read().splitlines()
    lines.append(line)
    lines = map(lambda x:x+'\n',lines)
    f = open('register.txt','w')
    f.writelines(lines)
    f.close()
    return username

def login():
    global status
    fails = 0

    print("||||| --- Login --- |||||")
    username = input("Username: ")
    password = input("Password: ")
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[0] == username and line.split(',')[1] == password:
            print("Welcome",username)
            return True
    while line.split(',')[0] != username and line.split(',')[1] != password:
        fails += 1
        print(f"Wrong username or password Please try again. You have {3-(fails-1)} tries left.")
        username = input("Username: ")
        password = input("Password: ")
        for line in lines:
            if line.split(',')[0] == username and line.split(',')[1] == password:
                print("Welcome",username)
                return True
            if fails == 3:
                return False
    return True
    
def show_menu():
    print("||||| --- Menu --- |||||")
    print("1. Vaccination")
    print("2. Symptoms")
    print("3. Statistics")
    print("4. Exit")

