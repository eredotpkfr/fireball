#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import time

def cracker():
    md5 = input('\033[94m'+"[+] Please Insert Any MD5 Hash:\n>> "+'\033[0m')
    try:
        send_rq = requests.post("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",data={"md5":md5})
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.7)
        print('\033[91m'+"[!] Request Not Send !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Check Your Internet Connection !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    soup = BeautifulSoup(send_rq.content,"html.parser")
    div = soup.find_all("div",{"class":"white_bg_title"})
    print('\033[95m'+"-"*50+'\033[0m')
    check = False
    for div_2 in div:
        divs = div_2.text
        print('\033[93m'+'[+] '+divs+'\033[0m')
        time.sleep(0.7)
        if (divs.isspace() == False):
            check = True
        else:
            pass
    print('\033[95m'+"-"*50+'\033[0m')
    if (check == True):
        print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    else:
        pass
    print('\033[95m'+"-"*50+'\033[0m')
    er = soup.find_all("div",{"class":"error_title"})
    for er_2 in er:
        error = er_2.text
        print('\033[91m'+"[-] Operation completed unsuccessfully..."+'\033[0m')
        time.sleep(1)
        print('\033[91m'+'[!] '+error+' !'+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    
