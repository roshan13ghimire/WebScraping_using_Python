import requests
from bs4 import BeautifulSoup


username = input()

url = "https://github.com/" + username + "?tab=repositories"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
s = soup.find("div", {"class": "BtnGroup"})
final = []
for i in soup.findAll(itemprop='name codeRepository'):
    final.append(''.join(i.get_text())[9:])

if s:
    l = []
    for a in s.find_all('a', href=True):
        l.append(a['href'])
    url = l[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for i in soup.findAll(itemprop='name codeRepository'):
        final.append(''.join(i.get_text())[9:])
    s = soup.find("div", {"class": "BtnGroup"})
    while True:
        l = []
        for a in s.find_all('a', href=True):
            l.append(a['href'])
        if(len(l) == 2):
            url = l[1]
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for i in soup.findAll(itemprop='name codeRepository'):
                final.append(''.join(i.get_text())[9:])
            s = soup.find("div", {"class": "BtnGroup"})
        else:
            break
print(final)