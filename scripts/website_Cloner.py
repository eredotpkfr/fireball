#!/usr/bin/env python3
#-*-coding:utf-8-*-

import time
import sys                
from bs4 import BeautifulSoup
import requests
import os
import urllib3

def send_Request():
    try:
        rquest_Send = requests.get(str(URL))
        if not (rquest_Send.encoding == 'utf-8'):
      	    rquest_Send.encoding = 'utf-8'
        else:
            pass
        contents = rquest_Send.content
        soup = BeautifulSoup(contents,'html.parser')
        links = soup.find_all("a")
        time.sleep(1)
        def catch_another_Files():
            print('\033[93m'+"\n[ ========== Downloading Another Files ========== ]"+'\033[0m')
            files = []
            Other = soup.find_all('link')
            Other_2 = soup.find_all('meta')
            Other_3 = soup.find_all('script')
            Other_4 = soup.find_all('video')
            for css in Other:
                files.append(css.get('href'))
            for js in Other_2:
                files.append(js.get('content'))
            for js_2 in Other_3:
                files.append(js_2.get('src'))
            for videos in Other_4:
                files.append(videos.get('src'))
            for catch in files:
                if ('.png' in catch or '.ico' in catch or '.img' in catch or '.jpeg' in catch or '.jpg' in catch or '.psd' in catch):
                    fullname = str(PATH) + '/Copied/'+ str(catch)
                    path,basename = os.path.split(fullname)
                    segments = catch.rpartition('/')
                    if not os.path.exists(path):
                        os.makedirs(path)
                        try:
                            url_img = str(URL)+str(catch)
                            img_open = urllib.request.urlopen(url_img)
                            file_open = open(PATH+'/Copied'+segments[0]+'/'+segments[2],'wb')
                            file_open.write(img_open.read())
                            file_open.close()
                            img_open.close()
                            print('\033[94m'+"[+] Downloaded one image ---> "+'"'+str(URL)+str(catch)+'"'+'\033[0m')
                        except Exception:
                            print('\033[91m'+'[!] One image not downloaded ! ---> ["'+str(URL)+str(catch)+'"]\033[0m')
                if ('.css' in catch or '.js' in catch or '.json' in catch or '.aspx' in catch):
                    fullname = str(PATH) + '/Copied/' + str(catch)
                    path,basename = os.path.split(fullname)
                    segments = catch.rpartition('/')
                    get_files = str(URL) + str(catch)
                    if not os.path.exists(path):
                        os.makedirs(path)
                        try:
                            request_css = requests.get(get_files)
                            contents_css = request_css.content
                            file_CSS_JS = open(str(PATH)+'/Copied/'+segments[0]+'/'+segments[2],'wb')
                            file_CSS_JS.write(contents_css)
                            file_CSS_JS.close()
                            print('\033[94m'+"[+] Downloaded one file ---> "+'"'+str(URL)+str(catch)+'"'+'\033[0m')
                        except Exception:
                            print('\033[91m'+'[!] One file not downloaded ! ---> ["'+str(URL)+str(catch)+'"]\033[0m')
                else:
                    pass
    except requests.RequestException:
        print('\033[91m'+"[!] There was an ambiguous exception that occurred while handling your request."+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Request not sent !"+'\033[0m')
        time.sleep(1)
        print('\033[91m'+"[!] Please Check Your Internet Connection !"+'\033[0m')
        time.sleep(1)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.ConnectionError:
        print('\033[91m'+"[!] A Connection error occurred."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.HTTPError:
        print('\033[91m'+"[!] An HTTP error occurred."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.URLRequired:
        print('\033[91m'+"[!] A valid URL is required to make a request."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.TooManyRedirects:
        print('\033[91m'+"[!] Too many redirects."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.ConnectTimeout:
        print('\033[91m'+"[!] The request timed out while trying to connect to the remote server."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.ReadTimeout:
        print('\033[91m'+"[!] The server did not send any data in the allotted amount of time."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except requests.Timeout:
        print('\033[91m'+"[!] The request timed out."+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    except Exception:
        print('\033[91m'+"[!] An unknown error was encountered !"+'\033[0m')
        time.sleep(0.5)
        print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
        time.sleep(0.7)
        fire_Ball.function_Options()
    try:
        os.mkdir(PATH+'/Copied')
        file_2 = open(PATH+'/Copied/all links.txt','w')
    except Exception:
        print('\033[91m'+"[!] Check your path."+'\033[0m')
        time.sleep(0.5)
        print('\033[91m'+"[!] Path is not found."+'\033[0m')
        time.sleep(1)
        print('\033[91m'+"[!] Maybe '../Copied' is already created. Please check it."+'\033[0m')
        time.sleep(1)
        fire_Ball.function_Options()
    for links_2 in links:
        file_2.write(str(links_2.get('href')))
        file_2.write("\n")
    file_2.close()
    try:
        file_1 = open(PATH+'/Copied/'+str(file_Name)+'.html','wb')
        file_1.write(contents)
        file_1.close()
        print('\033[92m'+"[+] Copied URL this path "+str(PATH)+'/Copied/'+str(file_Name)+'.html'+'\033[0m')
        time.sleep(1)
        print('\033[92m'+"[+] All links extract in "+str(PATH)+'/Copied/'+"all links.txt"+'\033[0m')
        time.sleep(0.7)
        print('\033[92m'+"[+] Completed."+'\033[0m')
        time.sleep(1)
        print('\033[92m'+"[+] Catching another files ..."+'\033[0m')
        time.sleep(0.5)
        try:
            catch_another_Files()
        except Exception:
            time.sleep(0.5)
            print('\033[92m'+"[+] Operation completed successfully..."+'\033[0m')
            time.sleep(3)
    except Exception:
        print('\033[91m'+"[!] Check your path"+'\033[0m')
        time.sleep(0.6)
        print('\033[91m'+"[!] Path is not found."+'\033[0m')
        time.sleep(0.6)
        print('\033[91m'+"[!] Maybe '../Copied' is already created. Please check it."+'\033[0m')
        fire_Ball.function_Options()
    print('\033[93m'+"[+] Returning to the options..."+'\033[0m')
    time.sleep(1)
    fire_Ball.function_Options()    
def take_info():
    time.sleep(0.2)
    global URL,PATH,file_Name
    URL = str(input('\033[94m'+"[+] Entry any URL or WebSite('Please insert with HTTP or HTTPS'):\n>> "+'\033[0m'))
    time.sleep(0.1)
    PATH = str(input('\033[94m'+"[+] Entry any path ('Files created this path.If don't entry path, path is ---> /var/www/html/'):\n>> "+'\033[0m'))
    time.sleep(0.1)
    file_Name = str(input('\033[94m'+"[+] Entry any file name (If don't entry file name, file name is ---> Copied):\n>> "+'\033[0m'))
    if str(PATH) == "" or str(PATH).isspace() == True:
        PATH = "/var/www/html/"
    else:
        pass
    if str(file_Name) == "" or str(file_Name).isspace() == True:
        file_Name = "Copied"
    else:
        pass
    if "https://" not in str(URL) and "http://" not in str(URL):
        URL = 'https://'+str(URL)+'/'
        send_Request()
    else:
        send_Request()
