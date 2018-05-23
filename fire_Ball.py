#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
sys.path.append(r'../fire_Ball/scripts')
import time
import progressbar
from bs4 import BeautifulSoup
import requests
import os
import website_Cloner
import create_actual_proxy_list 
import E_mail_bomber 
import ıp_lookup 
import md5_cracker 
import link_extractor
import name_Query
import exploit_db

def function_MainMenu():
    print('\033[94m'+""" 
 ✄╭━━━╮╱╱╱╱╱╭━━╮╱╱╱╭╮╭╮
 ✄┃╭━━╯╱╱╱╱╱┃╭╮┃╱╱╱┃┃┃┃
 ✄┃╰━━┳┳━┳━━┫╰╯╰┳━━┫┃┃┃
 ✄┃╭━━╋┫╭┫┃━┫╭━╮┃╭╮┃┃┃┃
 ✄┃┃╱╱┃┃┃┃┃━┫╰━╯┃╭╮┃╰┫╰╮
 ✄╰╯╱╱╰┻╯╰━━┻━━━┻╯╰┻━┻━╯"""+'\033[0m')
    print("\n"+'\033[95m'+"[*] Version ........... 1.0"+'\033[0m')
    print('\033[95m'+"[*] Author  ........... Eredot_PK&FR"+'\033[0m')
    print('\033[95m'+"[*] Twitter ........... @YoksulErdogan"+'\033[0m')
    print('\033[95m'+"[*] GitHub  ........... @eredotpkfr"+'\033[0m')
    print('\033[95m'+"[*] Linkedin........... @ErdoğanYoksul"+'\033[0m')
    print('\033[95m'+"[*] Note !  ........... 0=={::::::::::::>\n"+'\033[0m')
    print('\033[92m'+"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"+'\033[0m')
    while True:
        selection = input('\033[94m'+"[+] You can use 'help' command for access help section.\n[+] You can use 'exit' command for exit from program\n>> "+'\033[0m')
        if (selection == 'exit' or selection == 'Exit'):
            sys.exit()
        elif (selection == "help" or selection == "Help"): 
            time.sleep(0.3)
            def function_Options():              
                print('\033[92m'+"\n# ----- OPTİONS ----- # \n[1] Basic WebSite Cloner \n[2] Create Actual Proxy List [ONLINE] \n[3] E-mail Bomber [GMAİL] \n[4] Who Is IP LookUP [ONLINE] \n[5] MD5 Cracker [ONLINE] \n[6] Link Extractor [ONLINE] \n[7] Name Query [ONLINE] \n[8] Exploit-DB Exploits And Details [ONLINE] \n[9] Back to main menu\n[0] Exit from program \n"+'\033[0m') 
                while True:
                    selection_Two = input('\033[94m'+"[+] Make your choice.\n[+] You can use 'options' command for see all options.\n>> "+'\033[0m')
                    if (selection_Two == 'options' or selection_Two == 'Options'):
                        function_Options()
                    elif (selection_Two == '1'):
                        try:
                            website_Cloner.take_info()
                        except Exception:
                            pass
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '2'):
                        try:
                            create_actual_proxy_list.catch_Proxy()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '3'):
                        try:
                            E_mail_bomber.start_bombard()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '4'):
                        try:
                            ıp_lookup.take_ip()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '5'):
                        try:
                            md5_cracker.cracker()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '6'):
                        try:
                            link_extractor.link_extract()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '7'):
                        try:
                            name_Query.check_name()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '8'):
                        try:
                            exploit_db.exploit_db()
                        except Exception:
                            time.sleep(2)
                            function_Options()
                    elif (selection_Two == '9'):
                        function_MainMenu()
                    elif (selection_Two == '0'):
                        sys.exit()
                    else:
                        print('\033[91m'+"[!]'"+selection_Two+"'"+" Command not found."+'\033[0m')
            function_Options()
        else:
            print('\033[91m'+"[!]'"+selection+"'"+" Command not found.\n[!] Please insert 'help' command."+'\033[0m')
try:
    print("[***] STARTING PROGRAM.")
    time.sleep(0.3)
    print("[***] STARTING PROGRAM..")
    time.sleep(0.2)
    print("[***] STARTING PROGRAM...")
    time.sleep(0.5)
    print('\033[92m'+"[***] ALL SETTINGS .......... [ OK ]"+'\033[0m')
    time.sleep(0.6)
    bar = progressbar.ProgressBar()
    for i in bar(range(100)):
        time.sleep(0.01)
    function_MainMenu()
except KeyboardInterrupt or SystemExit:
    sys.exit()
