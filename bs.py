from bs4 import BeautifulSoup
import requests

topic = input("Enter topic : ")
response = requests.get("https://en.wikipedia.org/wiki/"+topic)
soup = BeautifulSoup(response.text,"lxml")
t = soup.find_all('h1')

text=""

for i in range(0,len(t)):
    text+=t[i].text
    
print(text)