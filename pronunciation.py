import requests
from bs4 import BeautifulSoup

def DownloadWord(word):
    URL = 'https://www.lexico.com/en/definition/' + word
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    parents = soup.find_all('h3', class_='pronunciations')

    for element in parents:
        link = element.find('audio')['src']
        audio = requests.get(link, allow_redirects=True)
        open(word + '.mp3', 'wb').write(audio.content) #no type safety here, hopefully it's always mp3

inputFile = 'input.txt'
with open(inputFile) as fp:
    line = fp.readline()
    while line:
        DownloadWord(line.strip())
        line = fp.readline()

#keeps terminal open at the end
input()