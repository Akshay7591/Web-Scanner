echo 'Installing Web Scanner....'
sudo apt-get update -y
sudo apt-get install python3-pip -y
python3 -m pip install -r requirements.txt
sudo apt-get install nikto -y
sudo apt-get install nmap -y
sudo apt-get install whois -y
sudo apt-get install traceroute -y
sudo apt-get install dnsutils -y
