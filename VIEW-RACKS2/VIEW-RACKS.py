import colorama
from selenium import webdriver
from time import sleep
from colorama import Fore

link = 'https://youtu.be/BFcGwPPQLfw'
time = '3'

print(Fore.RED + '''
██╗   ██╗██╗███████╗██╗    ██╗    ██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║   ██║██║██╔════╝██║    ██║    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚════██╗
██║   ██║██║█████╗  ██║ █╗ ██║    ██████╔╝███████║██║     █████╔╝ ███████╗ █████╔╝
╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    ██╔══██╗██╔══██║██║     ██╔═██╗ ╚════██║██╔═══╝ 
 ╚████╔╝ ██║███████╗╚███╔███╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████║███████╗
  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝'''+ Fore.RESET + Fore.CYAN)
LK = input("Link For Video: ")
link = LK
TM = input("Time For Refresh: ")
time = TM

driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="chromedriver.exe")
driver4 = webdriver.Chrome(executable_path="chromedriver.exe")

driver1.get(link)
driver2.get(link)
driver3.get(link)

while True:
    sleep(time)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()