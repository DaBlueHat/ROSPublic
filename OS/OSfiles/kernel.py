import time
import os

def kernel():
    kernelConnection =input("Enter a command to execute! ")

    if kernelConnection == "exit":
        exit()
    
    if kernelConnection == "help":
        print("help - displays a list of commands")
        print("exit - exits the program")
        kernel()

    # invalid command line arguments
    
    if kernelConnection != "exit":
        if kernelConnection != "help":
            print("Invalid command")




kernel():