#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import time

def link_extract():
    take_link = input('\033[94m'+"[+] Please Insert Any Link:\n>> "+'\033[0m')
    PATH = input('\033[94m'+"[+] Please Insert Any Path LINKS Are Write This Path With TXT File:\n>> "+'\033[0m')
    try:
        file_txt = open(PATH+"/Extracted Links.txt","w")
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Path Is Not Found Please Check It !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        send_rq2 = requests.post("https://99webtools.com/link-extractor.php",data={"u":take_link,"type":"all","submit":"Extract"})
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Request Not Send !"+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    soup = BeautifulSoup(send_rq2.content,"html.parser")
    table = soup.find_all("div",{"class":"data"})
    check = False
    for divs in table:
        div = divs.find_all("div")
        for a in div:
            alar = a.find_all("a")
            for text in alar:
                textler = text.text
                check = True
                file_txt.write(textler)
                file_txt.write("\n")
                print('\033[92m'+'[+] '+textler+'\033[0m')
                time.sleep(0.05)
    if (check == True):
        file_txt.close()
        print('\033[94m'+'[+] Writed All Extract Lİnks This Path ---> ["'+PATH+"/Extracted Links.txt"+'"]'+'\033[0m')
        time.sleep(0.5)
        print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        fire_Ball.function_Options()
    if (check == False):
        file_txt.close()
        print('\033[91m'+'[!] This URL ---> ["'+take_link+'"]'+" Not Extract !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    else:
        pass
