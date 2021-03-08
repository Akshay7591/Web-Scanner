import os


def get_whois(url):
    command="whois "+url
    process=os.popen(command)
    results=str(process.read())
    return results



