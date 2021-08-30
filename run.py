#!/bin/python3
#MasterBurnt 
#t.me/TheBurnt 
import os
from concurrent.futures import ThreadPoolExecutor
#Colors
c1 = '\033[0m' #white
c2 = '\033[92m' #green
c3 = '\033[96m' #cyan
c4 = '\033[91m' #red
c5 = '\033[93m' #yellow 
c6 = '\033[94m' #blue

os.system('clear')

print(c4+f"""
     MᵃˢᵗᵉʳBᵘʳⁿᵗ{c2}     __        __  ___     __
     _______  __ _  / /  ___  /  |/  /__ _/ /_____ ____
    / __/ _ \/  ' \/ _ \/ _ \/ /|_/ / _ `/  '_/ -_) __/
    \__/\___/_/_/_/_.__/\___/_/  /_/\_,_/_/\_\\__/_/ 
                      
                        """)
username_file = input(c2+f'[+]{c6} Please enter the username file :{c1} ')
password_file = input(c2+f'[+]{c6} Please enter the password file :{c1} ')
file_name = input(c2+f'[+]{c6} Please select a file name to save :{c1} ')
if file_name == "":
    file_name = "combo"
else:
    pass

       

combo = []
try:
    username = open(username_file, "r").read().splitlines()
except IOError as e:
    print(c4+"Username file not found! =( ")
    exit(1)
try:
    password = open(password_file, "r").read().splitlines()
except IOError as e:
    print(c4+"password list file not found! =( ")
    exit(2)
    
def task():
    for user in set(username):
        for passs in set(password):
            if user == "" or passs == "":
                pass
            else:
                combo.append(f"{str(user)}:{str(passs)}\n")



def main():
 with ThreadPoolExecutor(max_workers=5) as executor:
   future = executor.submit(task) 
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   
os.system('clear') 
print(c2+f' P{c1}l{c3}e{c4}ase{c5} w{c2}a{c6}i{c1}t... ')  
main()  

out = open(f"{file_name}.txt","a")
for w in set(combo):    
    out.write(w+"\n")
size = out.seek(0, 2)
out.close()
os.system('clear')
print(c2+f"Combo number :{c1} {len(combo)}{c2} \nSaved :{c1} {file_name}.txt\n{c2}File Size :{c1} {size // 1000 / 1000}")     
