import os

"""
def get_whois(url):
    command="whois "+url
    return str(os.system(command))

print(get_whois('thenewboston.com'))
"""

def get_whois(url):
    command="whois "+url
    process=os.popen(command)
    results=str(process.read())
    return results
#print(get_whois('thenewboston.com'))



