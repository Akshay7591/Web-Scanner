from urllib.request import urlopen
import io



def get_robots_txt(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'
    html=urlopen(path+"robots.txt")
    print('-------------------------------------')
    print('robots.txt of the following site has the following data:')
    print(html.read().decode('utf-8'))
    return(html.read().decode('utf-8'))



