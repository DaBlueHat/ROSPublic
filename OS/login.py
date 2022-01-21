import os 
import time

while True:
    with open('user/info/pass.ROS') as f:
        rightpassword = f.read()
        password = input("Type the password you set : ")

        if password == rightpassword:
            print("Logged in")
            os.startfile('OS/OSfiles/kernel.py')
        else:
            print("Invalid password! Please enter your password again!")

    