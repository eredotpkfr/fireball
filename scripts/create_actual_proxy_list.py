#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import time

def catch_Proxy():
    try:
        request = requests.get("https://free-proxy-list.net/")
        soup = BeautifulSoup(request.content,"html.parser")
        table = soup.find_all("tbody")
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Request Not Send !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] This Tool Use Some Web Sites And Your Internet Connection Is Failed !"+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        path = input('\033[94m'+"[+] Please Insert Any Path (File Is Create This Path):\n>> "+'\033[0m')
        detail = open(str(path)+'Detail.txt','w')
        ıpaddress = open(str(path)+'IP Address.txt','w')
        detail.write("IP ADDRESS    |     PORT    |     CODE    |     ANONYMITY    |     GOOGLE    |  HTTPS    |     LAST CHECKED    |    Eredot_PK&FR  0=={::::::::> |\n")
        detail.write("-"*145)
        detail.write("\n")
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Please Chech Your Entered Path !"+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        for catch in table:
            tr = catch.find_all("tr")
            for catch_2 in tr:
                td = catch_2.find_all("td")
                for tx in td:
                    text = tx.text
                    if 'elite proxy' in text:
                        text = '["'+text.upper()+'"]'
                    else:
                        pass
                    detail.write(text)
                    detail.write(" \t ")
                detail.write("\n")
            detail.close()
            for catch_3 in tr:
                td_2 = catch_3.find("td").text
                ıpaddress.write(td_2)
                ıpaddress.write("\n")
            ıpaddress.close()
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        print('\033[92m'+'[+] Created Actual Proxy List With Details This Path ---> ["'+str(path)+'Details.txt'+'"]'+'\033[0m')
        time.sleep(0.8)
        print('\033[92m'+'[+] Created Actual Proxy List Just IP Address This Path ---> ["'+str(path)+'IP Address.txt'+'"]'+'\033[0m')
        time.sleep(0.5)
        print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except Exception:
        time.sleep(0.7)
        fire_Ball.function_Options()
