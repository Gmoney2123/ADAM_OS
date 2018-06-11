#This code is purely for fun, and not intended for anykind of actual OS.
#And considering this is in Python and not C or C++...
#I would be impressed if you could get it to run as one.

import os
import sys
import time
import random
from tqdm import *

### VARIABLES, DICTIONARIES, ETC.###
mainloop = True
userloop = True
First_Run = True
Administrators = ["Michael", "Pixel", "Tiffany", "Garrett", "Chris"]
#This function is used for timing etc.
def pause():
    time.sleep(1.5)


# This function clears the screen when nesseary.
def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# Makes the main menu... Duh.
def make_main_menu():
    print(30 * "-", "Menu", 30 * "-")
    print("1.) Initialize Systems")
    print("2.) Run Diagnostics")
    print("3.) User Management")
    print("4.) Systems File Management")
    print("5.) Add/Remove Protocols")
    print("6.) Shutdown System")
    print(67 * "-")

# start the system
def Initialize_Systems():
    First_Run = False
    clear()
    print("\nLoading, Please wait...\n")

    for i in tqdm(range(100)):
        time.sleep(0.2)

    pause()
    print("\n\nInitialization Successful!")

    if First_Run:
        print("\nIt has been 794 days since last diagnostic test was run...")
        print("Initializing mandatory Diagnostic tests of all Systems...\n\n")
        run_diagnostic()
        First_Run = False

def user_management_menu():
    print(30 * "-", "User Management", 30 * "-")
    print("1.) List Current Administrators")
    print("2.) Add or Remove Administrator")
    print("3.) Return To Main Menu")
    print(75 * "-")

def user_management():
    while userloop:
        user_management_menu()
        userchoice = input("Select Option: ")

        if userchoice == "1":
            clear()
            print("Current Administrators are:" + str(Administrators))
            print("\n\n")
        elif userchoice == "2":
            clear()
            userchange = True
            while userchange:
                print("\n\nTo Add a User, type \'-a \"Username\"\', to remove a user, type \'-r \"Username\"\'")
                print("To return to the Menu, type \'quit\'")
                ar_user = input("ROOT$> ")
                clear()
                Parsed_ARUser = ar_user.split()
                if Parsed_ARUser[0] == "-a":
                    if Parsed_ARUser[1] in Administrators:
                        print("UserName is taken.\n\n")
                    else:
                        Administrators.append(str(Parsed_ARUser[1]))
                elif Parsed_ARUser[0] == "-r":
                    if Parsed_ARUser[1] not in Administrators:
                        print("Cannot remove \'" + Parsed_ARUser[1] + "\', does not exist!\n\n")
                    else:
                        Administrators.remove(Parsed_ARUser[1])
                        print("User has been deleted from registry.")
                elif Parsed_ARUser[0] == "quit":
                    userchange = False
                    break
                else:
                    print("Command not recognized, try again.")
        elif userchoice == "3":
            print("Returning to Main Menu...")
            time.sleep(3)
            clear()
            break
        else:
            print("Error, entry not valid.")

def run_diagnostic():
    if First_Run == False:
        print("Now Running Diagnostics...")

    for i in tqdm(range(100), desc="Benchmarking CPU"):
        time.sleep(random.uniform(0,1.5))

    pause()
    print("\nCPU's 1 & 2 operating at factory specifications of 8.7GHz\n")
    time.sleep(5)
    clear()
    print("Now testing RAM for faults or flipped bit vulnerabilities...\n")
    pause()
    for i in tqdm(range(25), desc="RAM CARD 1"):
        time.sleep(random.uniform(0,1))

    for i in tqdm(range(25), desc="RAM CARD 2"):
        time.sleep(random.uniform(0,1))

    for i in tqdm(range(25), desc="RAM CARD 3"):
        time.sleep(random.uniform(0,1))

    for i in tqdm(range(30), desc="RAM CARD 4"):
        time.sleep(random.uniform(0,1))

    print("RAM check successful: Validated integrity of RAM CARDs 1-3\n")
    pause()
    print("WARNING: RAM CARD 4 - multiple faults found at:")
    pause()
    print("0x0000883A: 0x44, 0xE2\n")
    pause()
    print("0x0000884E: 0x00\n")
    pause()
    print("0x00006634: 0xA3\n")
    pause()
    print("\nNOTE: RAM slot will be disabled until next diagnostic is run.\n User must revalidate replacement RAM CARD for integrity.")
    time.sleep(5)
    clear()
    print("\nContinuing Diagnostic...\n\n")
    pause()
    print("Validating Solid State Integrity")
    for i in tqdm(range(100), desc="SSD Integrity check"):
        time.sleep(random.uniform(0,2))
    pause
    print("\nNow validating all operational routines...")

    for i in tqdm(range(100), desc="A.I. intregrity validation"):
        time.sleep(random.uniform(0,1.5))

    print("Check Complete.")
    pause()
    print("Now returning to Menu")
    clear()
    
# Run the Code

print("Initializing A.D.A.M. Operation and Control Architecture...")
pause()

while mainloop:
    make_main_menu()
    MainMenuChoice = input("Select Option: ")

    if MainMenuChoice == "1":
        Initialize_Systems()
    elif MainMenuChoice == "2":
        run_diagnostic()
    elif MainMenuChoice == "3":
        user_management()
    elif MainMenuChoice == "4":
        print("not implimented")
    elif MainMenuChoice == "5":
        print("not implimented")
    elif MainMenuChoice =="6":
        print("Terminating system now")
        time.sleep(3)
        break
    else:
        print("Invalid Entry, Try again.")
