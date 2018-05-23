#!/usr/bin/env python3
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import time
import dryscrape

def check_name():
    try:
        take_Name = input('\033[94m'+"[+] Insert Any Name:\n>> "+'\033[0m')
        take_Surname = input('\033[94m'+"[+] Insert Surname(Compulsory):\n>> "+'\033[0m')
        Path = input('\033[94m'+"[+] Please Insert Any Path Results Are Write This Path With TXT File:\n>> "+'\033[0m')
        file = open(Path+'Results.txt','w')
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Path Is Not Found Please Check It !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:        
        s = dryscrape.Session()
        s.visit('http://www.kiminismi.com/!'+take_Name+'-'+take_Surname)
        body = s.body()
        soup = BeautifulSoup(body,'html.parser')
        center = soup.find_all('center',{'style':'padding:10px'})
        time.sleep(0.5)
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        print('\033[93m'+'\n[ ------------------ NO RESULTS ------------------ ]\n'+'\033[0m')
        for no in center:
            no_res = no.text
            no_res = no_res.replace('Networkünde hiç sonuç bulunamadı.','Network Not Have Any Result')
            print('\033[91m'+no_res+'\033[0m')
            time.sleep(0.25)
        print('\033[94m'+'\n[ ------------------ RESULTS ------------------ ]\n'+'\033[0m')
        time.sleep(0.5)
        tr = soup.find_all('tr',{'style':'cursor:pointer'})
        for td in tr:
            td_find = td.find_all('td')
            td_text = td.text
            td_text.encode('utf-8')
            file.write(td_text)
            for a in td_find:
                a_s = a.find_all('a')
                for href in a_s:
                    hrefs = href.get('href')
                    file.write('\n["'+hrefs+'"]\n')
                    file.write('----------------------------------------\n')
            print('\033[94m'+td_text,'["'+hrefs+'"]'+'\033[0m',sep="\n\n")
            print('\033[93m'+'----------------------------------------\n'+'\033[0m')
            time.sleep(0.25)
        file.close()
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
