#/usr/bin/python3

import wget
import os

path = os.getcwd()+"/maps"
maps = open(os.getcwd()+"/allbhopmaps.txt", "r")
maplines = maps.read().split("\n")
while True:
    user = input(">>")
    try:
        user = int(user)
        print(maplines[user])
    except ValueError:
        if user == "scrape":
            for i in range(0,len(maplines)):
                wget.download("http://main.fastdl.me/maps/"+maplines[i]+".bsp.bz2",out=path)
                print("\n")
                i+=1
            break
        else:
            print("Invalid selection, exiting..")
            break


