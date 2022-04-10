'''This function is written by Ms.Yosita ID:6410505817'''


from cProfile import label
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def statistics():
    print("statistics function")
    while True:
        show_menu()
        if select_menu() == False:
            break

def show_menu():
    print("\n")
    print("----- Menu -----")
    print("1. total_vaccination in each health area")
    print("2. percentage of vaccination by type")
    print("3. Exit")
    print("----------------")

def select_menu():
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("total_vaccination in each health area")
            statistics_total_health_area()
        elif choice == 2:
            print("percentage of vaccination by type")
            statics_type_of_vaccine()
        elif choice == 3:
            print("Exit")
            return False
        else:
            print("Please enter a valid choice")
    except ValueError:
        print("Please enter a valid choice")

def statistics_total_health_area():
    data = pd.read_csv('data.csv')
    area = data.health_area 
    area_1 = 0
    area_2 = 0
    area_3 = 0
    area_4 = 0
    area_5 = 0
    area_6 = 0
    area_7 = 0
    area_8 = 0
    area_9 = 0
    area_10 = 0
    area_11 = 0
    area_12 = 0
    area_13 = 0
    for i in range(len(area)):
        if area[i] == 1:
            area_1 += eval(str(data.total[i]))
        elif area[i] == 2:
            area_2 += eval(str(data.total[i]))
        elif area[i] == 3:
            area_3 += eval(str(data.total[i]))
        elif area[i] == 4:
            area_4 += eval(str(data.total[i]))
        elif area[i] == 5:
            area_5 += eval(str(data.total[i]))
        elif area[i] == 6:
            area_6 += eval(str(data.total[i]))
        elif area[i] == 7:
            area_7 += eval(str(data.total[i]))
        elif area[i] == 8:
            area_8 += eval(str(data.total[i]))
        elif area[i] == 9:
            area_9 += eval(str(data.total[i]))
        elif area[i] == 10:
            area_10 += eval(str(data.total[i]))
        elif area[i] == 11:
            area_11 += eval(str(data.total[i]))
        elif area[i] == 12:
            area_12 += eval(str(data.total[i]))
        elif area[i] == 13:
            area_13 += eval(str(data.total[i]))

    health_area = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    total = [area_1, area_2, area_3, area_4, area_5, area_6, area_7, area_8, area_9, area_10, area_11, area_12, area_13]

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    sns.barplot(x=health_area, y=total, ax=axes[0, 0])
    axes[0, 0].set_title("Total Vaccination in each health area")
    axes[0, 0].set_xlabel("Health Area")
    axes[0, 0].set_ylabel("Total Vaccination * 10 Million")
    sns.lineplot(x=health_area, y=total, ax=axes[0, 1])
    axes[0, 1].set_title("Total Vaccination in each health area")
    axes[0, 1].set_xlabel("Health Area")
    axes[0, 1].set_ylabel("Total Vaccination * 10 Million")
    sns.stripplot(x=health_area, y=total, ax=axes[1, 0])
    axes[1, 0].set_title("Total Vaccination in each health area")
    axes[1, 0].set_xlabel("Health Area")
    axes[1, 0].set_ylabel("Total Vaccination * 10 Million")
    sns.barplot(x=total, y=health_area, ax=axes[1, 1])
    axes[1, 1].set_title("Total Vaccination in each health area")
    axes[1, 1].set_xlabel("Total Vaccination * 10 Million")
    axes[1, 1].set_ylabel("Health Area")
    plt.tight_layout()
    plt.show()

def statics_type_of_vaccine():
    data = pd.read_csv('data.csv')
    sinovac = sum(data.Sinovac)
    astraZeneca = sum(data.AstraZeneca)
    sinopharm = sum(data.Sinopharm)
    pfizer = sum(data.Pfizer)

    type = ["Sinovac", "AstraZeneca", "Sinopharm", "Pfizer"]
    total = [sinovac, astraZeneca, sinopharm, pfizer]

    colors = sns.color_palette("pastel", n_colors=4)
    plt.pie(total, labels=type, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Average Vaccination by type")
    plt.show()

        