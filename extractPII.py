
import re
from requests_html import HTMLSession
import ssl
from bs4 import BeautifulSoup


def getInfo(url):
    global emails, numbers
    session = HTMLSession()
    ssl._create_default_https_context = ssl._create_unverified_context
    html = session.get(url)
    html_source_code = html.text
    numbers = (re.findall(r"tel:[0-9]{10}",html_source_code))
    emails = (re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",html_source_code))   
    i=0
    print('-------------------------------------')
    print("Emails found on this website-")
    for name in emails:
        print(emails[i])
        i+=1
    print('-------------------------------------')
    j=0
    print("Phone numbers found on this website-")
    for name in numbers:
        print(numbers[i])
        j+=1
    return 1


