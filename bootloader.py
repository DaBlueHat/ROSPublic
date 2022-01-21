import os 
import time

with open('boot.ROS') as bootloader:
    print("Checking boot.ROS...")
    bootload = bootloader.read()

    if bootload == "0":
        print("Loading setup")
        os.startfile('Setup.py')

    if bootload == "01":
        print("Loading login page")
        os.startfile('OS/login.py')


    if bootload != "0":
        if bootload != "01":
            print("System error")
            exit()