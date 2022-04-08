'''This function is written by Mr.Kristikorn ID:6410505442'''

def register():
    print("||||| Adding New User |||||")
    first = input("First Name: ")
    last = input("Last name: ")
    username = first+' '+last
    age = input("Enter your age: ")
    password = input("Password: ")
    vac = input("Have you vaccinated ? (Yes or No): ").lower()
    while vac != "yes" and vac != "no":
        vac = input("Have you vaccinated ? (Yes or No): ").lower()
    vac_booster = input("Have you got a booster ? (Yes or No): ")
    while vac_booster != "yes" and vac_booster != "no":
        vac_booster = input("Have you got a booster ? (Yes or No): ")
    line = username+','+password+','+age+','+vac+','+vac_booster
    lines = open('register.txt').read().splitlines()
    lines.append(line)
    lines = map(lambda x:x+'\n',lines)
    f = open('register.txt','w')
    f.writelines(lines)
    f.close()
    return username