# This file scraps info required for the desktop app
from bs4 import BeautifulSoup
import requests
url = "https://www.hamropatro.com/rashifal"

page = requests.get(url)
doc = BeautifulSoup(page.text, "html.parser")
rasifal_container = doc.find_all("div", {"id": "rashifal"})[0]
your_rasifal = input("Enter your rasifal: ")

#values were assigned by multiple testing from the web page
rasifal_dict = {
"mesh"       :0,    
"mithun"     :2,
"singha"     :4, 
"tula"       :6, 
"dhanu"      :8,
"khumba"     :10,
"brish"      :1,
"karkat"     :3, 
"kanya"      :5, 
"brishchik"  :7,     
"makar"      :9,
"meen"       :11
}

index = rasifal_dict[your_rasifal] if your_rasifal in rasifal_dict else print("\nInvalid")

rasifal_class = rasifal_container.find_all("div", {"class": "desc"})[index]
rasifal = rasifal_class.p

print(rasifal.string)

#incase i need  to write/read using flies
'''
string = str(rasifal.string).encode()
f = open ("test.txt", "wb")
f.write
f.write(string)
f.close()

f = open ("test.txt", "r",encoding="utf-8")
lines = f.readlines()
for line in lines:
    print (line)
'''
