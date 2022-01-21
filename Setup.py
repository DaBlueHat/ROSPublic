import time
import os

with open('OS/user/info/pass.ROS', 'r+') as pas:
    passwordSet = input("Enter a password you want to use: ")
    pas.writelines(passwordSet)
    
with open('OS/user/info/name.ROS', 'r+') as name:
    nameSet = input("Enter a name you want to use: ")
    name.writelines(nameSet)

print("Setup complete!")

with open('boot.ROS' ,'r+') as finishSetup:
    finishSetup.writelines('1')
    os.startfile('bootloader.py')
