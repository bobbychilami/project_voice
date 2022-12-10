
try:
    from googlesearch import search
except ImportError:
    print("No module")

import urllib

import xarray as xr

from gtts import gTTS

from playsound import playsound

from bs4 import BeautifulSoup as soup

# import io

import os

file = open("output.txt","r")

myText = file.read()

language = 'en'


for link in search(myText + " wikipedia", tld = "co.in", num = 5, stop = 5, pause = 2):
    print(link)

    if "wikipedia" in link:
        data = urllib.request.urlopen(link)
        
        urlData = data.read()

        data.close()
        
        page = soup(urlData,"html.parser")

        temp = page.find('div',{ "class" : "mw-body"})

        printData = temp.p.text

        print(printData)
        if(len(printData)>1):
            print(len(printData))
            obj = gTTS(text=printData, lang = language, slow=False)

            obj.save('welcome.mp3')

            playsound("welcome.mp3",True)

            os.remove('welcome.mp3')
