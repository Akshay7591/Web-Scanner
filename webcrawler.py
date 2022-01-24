from requests_html import HTMLSession
from bs4 import BeautifulSoup

def getLinks(url):
    links = []
    session = HTMLSession()
    response = session.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    for link in soup.find_all('a',href=True):
        if(link['href'].startswith('./')):
            link['href'] = url + link['href']
        if(link['href'].startswith('/')):
            link['href'] = url + link['href']
        if(link['href'].startswith('#')):
            continue
        if(link['href'].startswith('http')):
            links.append(link['href'])
    print('-------------------------------------')
    print("Crawling the target website.....")
    print("Links presesnt on this website-")
    i=0
    for link in links:
        print(link)
    return links


