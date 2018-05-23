#!/usr/bin/env python3
#-*-coding:utf-8-*-

import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
import getpass

def info_mail():
    try:
        global sender_email
        global sender_pass
        global receiver_email
        global Subject
        global Preamble
        global Message
        sender_email = input('\033[94m'+"[+] Please Insert E-mail Sender's E-mail:\n>> "+'\033[0m')
        sender_pass = getpass.getpass('\033[94m'+"[+] Please Insert E-mail Sender's Password:\n>> "+'\033[0m')
        receiver_email = input('\033[94m'+"[+] Please Insert E-mail Receiver's E-mail:\n>> "+'\033[0m')
        Subject = input('\033[94m'+"[+] Insert Any Subject:\n>> "+'\033[0m')
        Preamble = input('\033[94m'+"[+] Insert Any Preamble:\n>> "+'\033[0m')
        Message = input('\033[94m'+"[+] Insert Any Message:\n>> "+'\033[0m')
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Please Check You Entered Informations !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
def e_mail_bombard():
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Subject 
        msg.preamble = Preamble  
        mesaj = msg.as_string()
        body = mesaj
        msg.attach(MIMEText(body))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_pass)
        text = Message
        server.sendmail(sender_email, receiver_email, text)
        print('\033[93m'+"[+] Send One E-mail To  --->  ",'["'+receiver_email+'"]'+'\033[0m')
    except Exception:
        print('\033[91m'+"[!] An Unexpected Error Was Encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Please Check You Entered Informations !"+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options() 
def start_bombard():
    try:
        info_mail()
        try:
            number_mail = int(input('\033[94m'+"[+] How Many Send E-mail ?\n>> "+'\033[0m'))
            count = 1
            while count <= number_mail:
                e_mail_bombard()
                count +=1
        except Exception:
            print('\033[91m'+"[!] Please Check Your Internet Connection !"+'\033[0m')
            time.sleep(0.5)
            print('\033[91m'+"[!] Please Check You Entered Informations !"+'\033[0m')
            time.sleep(0.3)
            print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
            time.sleep(0.7)
            fire_Ball.function_Options() 
        print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
        time.sleep(0.7)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except Exception:
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.3)
        fire_Ball.function_Options()
