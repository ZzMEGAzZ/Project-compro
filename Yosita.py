'''This function is written by Ms.Yosita ID:6410505817'''


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



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

    health_area = ["area_1", "area_2", "area_3", "area_4", "area_5", "area_6", "area_7", "area_8", "area_9", "area_10", "area_11", "area_12", "area_13"]
    total = [area_1, area_2, area_3, area_4, area_5, area_6, area_7, area_8, area_9, area_10, area_11, area_12, area_13]

    plt.bar(health_area,total)
    plt.show()

        