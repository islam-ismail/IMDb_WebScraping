from bs4 import BeautifulSoup
import requests

# custom colors for output
blue = '\033[0;34m'
reset = '\033[0;37m'

# website Url
url = 'https://www.imdb.com/find?'
 
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'} 

mySession = requests.Session()
mySession.headers.update(headers)

movieNameQuery = input('What is the movie name: ')
print('\n')

query = {'ref_':'nv_sr_sm','q':movieNameQuery,'s':'all'}


result = mySession.get(url, params = query)

finalResult = BeautifulSoup(result.content,'lxml')

for x in finalResult.findAll('div',{'class':'findSection'}):
    for title in x.findAll('h3',{'class':'findSectionHeader'}):
        if title.text == 'Titles':
            for names in x.findAll('td',{'class':'result_text'}):
                print ('Result found: ' + blue + names.text + reset)
       
