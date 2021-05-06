#traceroute.py

import os

def tracert(x):
    print('-------------------')
    print('Traceroute-')
    os.system('traceroute '+x)
    '''
    command='traceroute '+x
    process=os.popen(command)
    results=str(process.read())
    print(results)
    return results
    '''

#x=str(input("Enter website:"))
#tracert(x)
