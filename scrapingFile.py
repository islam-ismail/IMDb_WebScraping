from bs4 import BeautifulSoup
import requests

blue = '\033[0;34m'
reset = '\033[0;37m'


url = 'https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd'
 
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'} 

mySession = requests.Session()
mySession.headers.update(headers)
result = mySession.get(url)

finalResult = BeautifulSoup(result.content,'lxml')

for x in finalResult.findAll('h3',{'class':'lister-item-header'}):
    for title in x.findAll('a'):
        print('Movie Found: ' + blue + title.text + reset)
    

#print(finalResult.text)