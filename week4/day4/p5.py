import os
import datetime

def sys_info():
    print("System Informantion")
    print("Operating System:",os.name)
    print("Current Working Directory:",os.getcwd())
    print("Current Date and Time:",datetime.datetime.now())
sys_info()