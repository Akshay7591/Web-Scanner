import os 

def get_nmap(options,ip):
	print('-------------------------------------')
	print('Nmap Scan Results-')
	command="nmap " + options + " " + ip
	process=os.popen(command)
	results=str(process.read())
	print(results)
	return results


