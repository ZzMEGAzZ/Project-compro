'''This function is written by Ms.Yosita ID:6410505442'''

def register():
    print("||||| --- Adding New User --- |||||")
    first = input("First Name: ")
    last = input("Last name: ")
    age = input("Enter your age: ")
    username = input("Username: ")
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[0] == username:
            print("Username already exists")
            return False
    password = input('Password: ')
    email = input("Email: ")
    phone = input("Phone: ")
    vac = input("Have you vaccinated ? (Y/N): ").upper()
    while vac != "Y" and vac != "N":
        vac = input("Have you vaccinated ? (Y/N): ").upper()
    if vac == "N":
        vac_booster = "N"
    else:
        vac_booster = input("Have you got a booster ? (Y/N): ").upper()
        while vac_booster != "Y" and vac_booster != "N":
            vac_booster = input("Have you got a booster ? (Y/N): ").upper()
    line = username+','+password+','+first+','+last+','+age+','+email+','+phone+','+vac+','+vac_booster
    lines = open('register.txt').read().splitlines()
    lines.append(line)
    lines = map(lambda x:x+'\n',lines)
    f = open('register.txt','w')
    f.writelines(lines)
    f.close()
    return username

def login():
    fails = 0

    print("||||| --- Login --- |||||")
    username = input("Username: ")
    password = input("Password: ")
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[0] == username and line.split(',')[1] == password:
            print("\n")
            print("Welcome",line.split(',')[2]+' '+line.split(',')[3])
            print("\n")
            return username
        elif line.split(',')[0] != username or line.split(',')[1] != password:
            while fails <3:
                fails += 1
                print(f"Wrong username or password Please try again. You have {3-(fails-1)} tries left.")
                username = input("Username: ")
                password = input("Password: ")
                for line in lines:
                    if line.split(',')[0] == username and line.split(',')[1] == password:
                        print("Welcome",line.split(',')[2]+' '+line.split(',')[3])
                        print("\n")
                        return username
            return False

def modified_data(username):
    lines = open('register.txt').read().splitlines()
    x = 0
    for line in lines:
        if line.split(',')[0] == username:
            break
        else:
            x += 1
    with open('register.txt','r') as fr:
        data_lines = fr.readlines()
        ptr = 0
        with open("register.txt", "w") as fw:
            for line in data_lines:
                if ptr != x:
                    fw.write(line)
                ptr += 1
    return True