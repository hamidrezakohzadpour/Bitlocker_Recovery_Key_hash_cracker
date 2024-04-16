import os
import random
import subprocess
from colorama import Fore
from datetime import datetime

def str_date_time():
    now = datetime.now()
    str_date = now.strftime("%Y%m%d")
    str_time = now.strftime("%H%M%S")
    return str_date + "_" + str_time

def exiting():
    print("Exiting...")
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    exit()

def key_generator(file_name, Count_of_keys):
    now = datetime.now()
    str_now = now.strftime("%d/%m/%Y %H:%M:%S")
    print("")
    print ("Starting at " + str_now)
    with open(file_name, "w") as file_object:
        for j in range(Count_of_keys + 1): 
            rcv_key = ""
            for i in range(8):
                if i != 7:
                    rcv_key += '{:06}'.format(random.randrange(000000, 999999)) + "-"
                else:
                    rcv_key += '{:06}'.format(random.randrange(000000, 999999)) + "\n"
            file_object.write(rcv_key)
            if j%10000000 == 0 and j > 0:
                j_Separated = '{:,}'.format(j)
                print(f'{"[+]..":5} {j_Separated:8} {"Recovery Keys Generated...":0}')
    print("Ending at " + str_now )

def execute_john(Recovery_keys_file_name,hash_file_name):
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    print(Fore.YELLOW + "Requirements for executing john-the-ripper..."+ Fore.RESET)
    print("1-File contain recovery keys:[" + file_name + "]")
    print("2-File contain recovery Key hash:[" + hash_file_name + "]")
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    print(Fore.YELLOW + "Step 2: Run the john-the-ripper..." + Fore.RESET)
    print("This program want execute john-the-ripper and find correct recovery key." )
    user_input = input("Do you want to continue? (yes/no): " )
    if user_input.lower() in ["yes", "y"]:
        if not os.path.exists("john.exe"):
            print(Fore.RED + "John.exe not found!, please copy this script to inside of john directory and run again." + Fore.RESET)
            exiting()
        elif not os.path.exists("bitlocker_recovery_key_hash.txt"):
            print(Fore.RED + "bitlocker_recovery_key_hash.txt not found!" + Fore.RESET)
            exiting()    
        else:
            print("")
            wordlist = "--wordlist=" + Recovery_keys_file_name
            subprocess.call(["john", "--format=bitlocker-opencl", wordlist, hash_file_name, "--progress-every=60"])
    else:
        exiting()
#Start of script
try:
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    print("# Bitlocker Recovery Key hash cracker Ver 1.4")
    print("# Writen by: HamidReza Kohzadpour")
    print("# e-mail:    Kohzadpour@Gmail.com")
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    print(Fore.YELLOW + "Step 1: Generating keys..."+ Fore.RESET)
    print("1. 20.000.000 Keys")
    print("2. 50.000.000 Keys")
    print("3. 99.999.000 Keys")
    print("4. Exit")
    choice = int(input("Type your choice then press ENTER: "))
except:
    print(Fore.BLUE + "======================================================================================" + Fore.RESET)
    print(Fore.RED + "Wrong number!, try again." + Fore.RESET)
    exiting()

if choice == 1:
    file_name = "bitlocker_recovery_key_" + str_date_time() + "_20.000.000.txt"
    key_generator(file_name, 20000000)
    execute_john(file_name,"bitlocker_recovery_key_hash.txt")
elif choice == 2:
    file_name = "bitlocker_recovery_key_" + str_date_time() + "_50.000.000.txt"
    key_generator(file_name, 50000001)
    execute_john(file_name,"bitlocker_recovery_key_hash.txt")
elif choice == 3:
    file_name = "bitlocker_recovery_key_" + str_date_time() + "_99.000.000.txt"
    key_generator(file_name, 99999001)
    execute_john(file_name,"bitlocker_recovery_key_hash.txt")
elif choice == 4:
    exiting()
else:
    print (Fore.RED + "Wrong number!, try again." + Fore.RESET)
    exiting()