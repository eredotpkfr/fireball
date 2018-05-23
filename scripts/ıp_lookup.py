#!/usr/bin/env python3
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import time

def take_ip():
    try:
        try:
            ıp_address = input('\033[94m'+"[+] Insert Any IP Address:\n>> "+'\033[0m')
            rq = requests.post("https://www.ultratools.com/tools/ipWhoisLookupResult",data = {"ipAddress":ıp_address})
            soup = BeautifulSoup(rq.content,"html.parser")
            pre = soup.find("pre").text
            print('\033[93m'+pre+'\033[0m')
        except Exception:
            try:
                div = soup.find_all("div",{"class":"tool-results"})
                for divs in div:
                    divler = divs.find_all("div")
                    for span in divler:
                        spantag = span.find_all("span")
                        for textspan in spantag:
                            textspantag = textspan.text
                            print('\033[93m'+textspantag+'\033[0m',end="")
                        print("\n")
            except Exception:
                print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
                time.sleep(0.5)
                print('\033[91m'+"[!] Request Not Send !"+'\033[0m')
                time.sleep(0.5)
                print('\033[91m'+"[!] Please Check You Entered IP Address, Maybe It's Not A IP Address Or Wrong IP Address !"+'\033[0m')
                time.sleep(0.5)
                print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
                time.sleep(0.7)
                fire_Ball.function_Options()
        print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except Exception:
        fire_Ball.function_Options()
