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

mode = input("Do you want to register or login ? (R/L): ").upper()
if mode == "R":
    username = reg.register()
    print("Your username is: ",username)
else:
    reg.login()






