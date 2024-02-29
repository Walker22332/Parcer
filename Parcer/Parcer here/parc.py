import requests
from bs4 import BeautifulSoup


f = open('parc.txt','w')

def Parser(url):

    res = requests.get(url = url)
    soup = BeautifulSoup(res.text,'lxml')
    
    products = soup.find_all('div',{"class": 'anonse'})

    try:

        for pro in products:
            title = pro.find('h2').text
            desc = pro.find('p').text
            links = pro.find('div', {'class': 'anonse_footer'})
            link =links.find('a').get('href')

            f.write(title+'\n'+desc+'\n'+link +'\n')

    except AttributeError:

        print('Ошибка сайта')

if __name__ == '__main__':

    for i in range(0,10):
        Parser(f'http://griffiny.ru/sezon-0{i}/')
        
    for i in range(10,24):
        Parser(f'http://griffiny.ru/season-{i}/')
    