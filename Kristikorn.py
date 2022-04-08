'''This function is written by Mr.Kristikorn ID:6410505442'''

import re


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

def login():
    fails = 0

    print("||||| --- Login --- |||||")
    username = input("Username: ")
    password = input("Password: ")
    lines = open('register.txt').read().splitlines()
    for line in lines:
        if line.split(',')[0] == username and line.split(',')[1] == password:
            print("Welcome",username)
            return username
    while line.split(',')[0] != username and line.split(',')[1] != password:
        fails += 1
        print(f"Wrong username or password Please try again. You have {3-(fails-1)} tries left.")
        username = input("Username: ")
        password = input("Password: ")
        for line in lines:
            if line.split(',')[0] == username and line.split(',')[1] == password:
                print("Welcome",username)
                return username
            if fails == 3:
                print("Please try again later")
                return False
