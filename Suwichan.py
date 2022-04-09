'''This function is written by Mr.Suwichan ID:6410505442'''

from multiprocessing.connection import wait
from time import sleep


def symptoms():
    print("--- Screening  questions for COVID-19 ---")
    past_14d = input("Have you had a fever in the past 14 days ? (Y/N): ").upper()
    while past_14d != "Y" and past_14d != "N":
        past_14d = input("Have you had a fever in the past 14 days ? (Y/N): ").upper()
    spreading =input("You travelled from or lived in any country that has continuous spreading of COVID-19 ? (Y/N): ").upper()
    while spreading != "Y" and spreading != "N":
        spreading =input("You travelled from or lived in any country that has continuous spreading of COVID-19 ? (Y/N): ").upper()
    job = input("Your occupation is related to tourists or in contact with many people ? (Y/N): ").upper()
    while job != "Y" and job != "N":
        job = input("Your occupation is related to tourists or in contact with many people ? (Y/N): ").upper()
    positive_covid = input("Have you been in contact with someone who has COVID-19 ? (Y/N): ").upper()
    while positive_covid != "Y" and positive_covid != "N":
        positive_covid = input("Have you been in contact with someone who has COVID-19 ? (Y/N): ").upper()
    print("Do you have any of these symptoms?")
    sleep(1)
    fever = input(" Fever ? (Y/N): ").upper()
    while fever != "Y" and fever != "N":
        fever = input(" Fever ? (Y/N): ").upper()
    dry_cough = input(" Dry Cough ? (Y/N): ").upper()
    while dry_cough != "Y" and dry_cough != "N":
        dry_cough = input(" Dry Cough ? (Y/N): ").upper()
    tiredness = input(" Tiredness ? (Y/N): ").upper()
    while tiredness != "Y" and tiredness != "N":
        tiredness = input(" Tiredness ? (Y/N): ").upper()
    Runny_nose = input(" Runny Nose ? (Y/N): ").upper()
    while Runny_nose != "Y" and Runny_nose != "N":
        Runny_nose = input(" Runny Nose ? (Y/N): ").upper()
    body_ache = input(" Body Ache ? (Y/N): ").upper()
    while body_ache != "Y" and body_ache != "N":
        body_ache = input(" Body Ache ? (Y/N): ").upper()
    sore_throat = input(" Sore Throat ? (Y/N): ").upper()
    while sore_throat != "Y" and sore_throat != "N":
        sore_throat = input(" Sore Throat ? (Y/N): ").upper()
    smell = input(" Loss of sense of smell  ? (Y/N): ").upper()
    while smell != "Y" and smell != "N":
        smell = input(" Loss of sense of smell  ? (Y/N): ").upper()
    breathing = input(" Difficult or short breathing or currently having pneumonia (Y/N): ").upper()
    while breathing != "Y" and breathing != "N":
        breathing = input(" Difficult or short breathing or currently having pneumonia (Y/N): ").upper()
    return fever, dry_cough, tiredness, Runny_nose, body_ache, sore_throat, smell, breathing, positive_covid, past_14d, spreading, job

def covid_checked(fever, dry_cough, tiredness, Runny_nose, body_ache, sore_throat, smell, breathing, positive_covid, past_14d, spreading, job):
    if fever == "Y" or dry_cough == "Y" or tiredness == "Y" or Runny_nose == "Y" or body_ache == "Y" or sore_throat == "Y" or smell == "Y" or breathing == "Y":
        print("You have COVID-19")
    else:
        print("You are safe")


