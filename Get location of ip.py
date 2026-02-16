
import requests
import socket

print("""
  ________             .____                         __           ____   ________ 
 /  _____/  ____  ____ |    |    ____   ____ _____ _/  |_  ____   \   \ /   /_   |
/   \  ____/ __ \/  _ \|    |   /  _ \_/ ___\\__  \\   __\/ __ \   \   Y   / |   |
\    \_\  \  ___(  <_> )    |__(  <_> )  \___ / __ \|  | \  ___/    \     /  |   |
 \______  /\___  >____/|_______ \____/ \___  >____  /__|  \___  >    \___/   |___|
        \/     \/              \/          \/     \/          \/                     
      """)


ui1 = input("Type 1 to locate website ip first, type 2 if ip is already known or not a website ip, Type 3 to only find the ip of a website. ")

#If 1 is typed

if ui1 == ("1"):
    web = input("Enter the url you need the ip of here: ")
    ipforwebtool = socket.gethostbyname(web)

    print("ip addres:", ipforwebtool)

    #Now running the locator

    ip = input("Enter an IP address: ")

    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()

    print(data)

#If 2 is typed

if ui1 == ("2"):
    ip = input("Enter an IP address: ")

    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()

    print(data)

#If 3 is typed

if ui1 == ("3"):
    web = input("Enter the url you need the ip of here: ")
    ipforwebtool = socket.gethostbyname(web)

    print("ip addres:", ipforwebtool)

input("Press Enter to Exit...")

