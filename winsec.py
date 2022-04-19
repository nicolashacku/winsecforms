#!/user/bin/python3
import requests
import os 
from colorama import Fore,init
import json
init()
os.system("clear")
v = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
c = Fore.LIGHTCYAN_EX
print(f'''{r}
        .__                             
__  _  _|__| ____   ______ ____   ____  
\ \/ \/ /  |/    \ /  ___// __ \_/ ___\ 
 \     /|  |   |  \\___ \\  ___/\  \___ 
  \/\_/ |__|___|  /____  >\___  >\___  >
                \/     \/     \/     \/ 

 {v}Herramienta desarrollada por nicolas.$ | Discord:nicolas.$#4882\n 
 ''')

url_e = str(input(f"{c}Digite el url del examen entre forms/ hasta /formResponse: "))
url_f= f'https://docs.google.com/forms/{url_e}/formResponse'

entry = str(input(f"{c}\nDigite el entry de la respuesta: "))
rta = str(input(f"{c}\nDigite la respuesta que quiere ganar: "))
payload = f'{entry}={rta}'

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
cantidad = int(input("\nDigite la cantidad de veces a spamear: "))
for n in range (cantidad):
    r = requests.post(url_f, data=payload, headers=headers)
