#This code is purely for fun, and not intended for anykind of actual OS.
#And considering this is in Python and not C or C++...
#I would be impressed if you could get it to run as one.

import os
import sys
import time
import random
from tqdm import *

#This function is used for timing etc.
def pause():
    time.sleep(1.5)


#This function clears the screen when nesseary.
def cls():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


print("Initializing A.D.A.M. Operation and Control Architecture...")
pause()
print("\nLoading, Please wait...\n")

for i in tqdm(range(100)):
    time.sleep(0.2)

pause()

print("\n\nInitialization Successful!")
pause()
print("\nIt has been 794 days since last diagnostic test was run...")
print("Initializing mandatory Diagnostic tests of all Systems...\n\n")

for i in tqdm(range(100), desc="Benchmarking CPU"):
    time.sleep(random.uniform(0,1.5))

pause()
print("\nCPU's 1 & 2 operating at factory specifications of 8.7GHz\n")
time.sleep(5)
cls()
print("Now testing RAM for faults or flipped bit vulnerability...\n")
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
print("\nNOTE: RAM slot will be disabled until next diagnostic is run.\n User must revalidate replacement RAM CARD integrity.")
time.sleep(5)
cls()
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


time.sleep(5)
