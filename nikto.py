import os 

def get_nikto(options,ip):
    print('-------------------------------------')
    x=str(input("Would you like to perform a Nikto Scan-(y/n)?"))
    if x=="y":
        print('Nikto Scan Results-')
        os.system('nikto -h '+ip)
    else:
        print("Not perfoming nikto scan")
