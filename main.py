from general import *
from domain_name import *
from whois import *
from robots_txt import *
from nmap import *
from ip_addr import *
from traceroute import *
from extractPII import *
from webcrawler import *
from nslookup import *
from cms import *
from nikto import *
import os
from art import *

root_dir='Scanned_Websites'
os.system('clear')
os.system('mkdir '+root_dir)

def gather_info(name,url):
    domain_name=get_domain_name(url)
    ip_addr=get_ip_address(domain_name)
    nmap=get_nmap('-F',ip_addr)
    robots_txt=get_robots_txt(url)
    get_cms(url)
    whois=get_whois(domain_name)
    print('------------------------')
    print('Whois Scan of the given URL-')
    print('\n')
    print(whois)
    tracert(domain_name)
    getLinks(url)
    getInfo(url)
    getDNSInfo(domain_name)
    get_nikto('-h',ip_addr)
    print('------------------------')

def create_report(name,full_url,domain_name,nmap,robots_txt,ip_addr):
    project_dir = root_dir + '/' + name
    os.system('mkdir '+project_dir)
    write_file(project_dir + '/full_url.txt' , full_url)
    write_file(project_dir + '/domain_name.txt' , domain_name)
    write_file(project_dir + '/nmap.txt' , nmap)
    write_file(project_dir + '/robots.txt' , robots_txt)
    write_file(project_dir + '/ip_addr.txt' , ip_addr)

tprint('Web Scanner')
a=str(input('Enter project name:'))
print("Enter site in the following format: http://www.<website>")
print("May not work for https websites")
x=str(input('Enter site to scan:'))
gather_info(a,x)
    
