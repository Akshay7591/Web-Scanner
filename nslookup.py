import subprocess
import sys

def getDNSInfo(url):
    print('-------------------')
    print("NSLOOKUP-")
    types = ["A", "NS", "CNAME", "AAAA", "MX", "ALIAS", "PTR","SOA"]
    for type in types:
        command = "nslookup -type=" + type + " " + url
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        #print(type)
        
        if(error):
            print(error)
    print(output.decode("utf=8"))
    return(output)

