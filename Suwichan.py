'''This function is written by Mr.Suwichan ID:6410505442'''

from time import sleep

def symptoms_analysis():
    count = 0
    print("--- Screening  questions for COVID-19 ---")
    past_14d = input("Have you had a fever in the past 14 days ? (Y/N): ").upper()
    if past_14d == "Y":
      count+=1
    while past_14d != "Y" and past_14d != "N":
      past_14d = input("Have you had a fever in the past 14 days ? (Y/N): ").upper()
      if past_14d == "Y":
        count+=1
    spreading =input("You travelled from or lived in any country that has continuous spreading of COVID-19 ? (Y/N): ").upper()
    if spreading == "Y":
        count+=2
    while spreading != "Y" and spreading != "N":
        spreading =input("You travelled from or lived in any country that has continuous spreading of COVID-19 ? (Y/N): ").upper()
        if spreading == "Y":
          count+=2
    job = input("Your occupation is related to tourists or in contact with many people ? (Y/N): ").upper()
    if job == "Y":
      count+=2
    while job != "Y" and job != "N":
        job = input("Your occupation is related to tourists or in contact with many people ? (Y/N): ").upper()
        if job == "Y":
          count+=2
    positive_covid = input("Have you been in contact with someone who has COVID-19 ? (Y/N): ").upper()
    if positive_covid == "Y":
        count+=1
    while positive_covid != "Y" and positive_covid != "N":
        positive_covid = input("Have you been in contact with someone who has COVID-19 ? (Y/N): ").upper()
        if positive_covid == "Y":
          count+=1
    print("Do you have any of these symptoms?")
    sleep(1)
    fever = input(" Fever ? (Y/N): ").upper()
    if fever == "Y":
        count+=1
    while fever != "Y" and fever != "N":
        fever = input(" Fever ? (Y/N): ").upper()
        if fever == "Y":
          count+=1
    dry_cough = input(" Dry Cough ? (Y/N): ").upper()
    if dry_cough == "Y":
        count+=1
    while dry_cough != "Y" and dry_cough != "N":
        dry_cough = input(" Dry Cough ? (Y/N): ").upper()
        if dry_cough == "Y":
          count+=1
    tiredness = input(" Tiredness ? (Y/N): ").upper()
    if tiredness == "Y":
        count+=1
    while tiredness != "Y" and tiredness != "N":
        tiredness = input(" Tiredness ? (Y/N): ").upper()
        if tiredness == "Y":
          count+=1
    Runny_nose = input(" Runny Nose ? (Y/N): ").upper()
    if Runny_nose == "Y":
        count+=1
    while Runny_nose != "Y" and Runny_nose != "N":
        Runny_nose = input(" Runny Nose ? (Y/N): ").upper()
        if Runny_nose == "Y":
          count+=1
    body_ache = input(" Body Ache ? (Y/N): ").upper()
    if body_ache == "Y":
        count+=1
    while body_ache != "Y" and body_ache != "N":
        body_ache = input(" Body Ache ? (Y/N): ").upper()
        if body_ache == "Y":
          count+=1
    sore_throat = input(" Sore Throat ? (Y/N): ").upper()
    if sore_throat == "Y":
        count+=1
    while sore_throat != "Y" and sore_throat != "N":
        sore_throat = input(" Sore Throat ? (Y/N): ").upper()
        if sore_throat == "Y":
          count+=1
    smell = input(" Loss of sense of smell  ? (Y/N): ").upper()
    if smell == "Y":
        count+=1
    while smell != "Y" and smell != "N":
        smell = input(" Loss of sense of smell  ? (Y/N): ").upper()
        if smell == "Y":
          count+=1
    breathing = input(" Difficult or short breathing or currently having pneumonia (Y/N): ").upper()
    if breathing == "Y":
        count+=1
    while breathing != "Y" and breathing != "N":
        breathing = input(" Difficult or short breathing or currently having pneumonia (Y/N): ").upper()
        if breathing == "Y":
          count+=1
    return count

def covid_checked(count):
    if count >= 7 :
      print("You are at high risk of getting seriously ill from COVID-19.")
      print("***Advice for people at high risk from coronavirus***")
      print("-get vaccinated against COVID-19")
      print("-wait for at least 14 days after you've had your 2nd dose of a COVID-19 vaccine before meeting with people")
      print("-limit the number of people you meet and avoid crowded places")
      print("-wear a face covering in shops, on public transport and when it's hard to stay away from other people (particularly indoors or in crowded places)")
      print("wash your hands with soap and water or use hand sanitiser regularly throughout the day")
    elif count>0 and count <7 :
      print("You may be risk of getting COVID-19")
      print("***Advice for people maybe risk from coronavirus***")
      print("-The standard recommendation is to self-quarantine for 14 days")
      print("-Follow your community guidelines for staying home.")
      print("Don’t leave your house if you don’t feel well.")
    else:
        print(' \"Great! You are safe.\" ')

