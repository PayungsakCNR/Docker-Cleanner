import os
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()

encoding = 'utf-8'
url = 'https://notify-api.line.me/api/notify'
token = os.getenv('LINE_NOTIFY_TOKEN')
headers = {'content-type':'application/x-www-form-urlencoded',
           'Authorization':'Bearer '+token}

try:
	getHostname = subprocess.check_output("hostname", shell=True)
	img_pr_output = subprocess.check_output("docker image prune -f", shell=True)
	print('OK-Remove Prune Image')
	con_pr_output = subprocess.check_output("docker container prune -f",shell=True)
	print('OK-Remove container prune')
	vol_output = subprocess.check_output("docker volume prune -f",shell=True)
	print('OK-Remove Prune Vol')
	network_output = subprocess.check_output("docker network prune -f",shell=True)
	print('OK-Remove Network Prune')
except subprocess.CalledProcessError as e:
	print(e.output)

#os.system("docker image prune -f")
#print('OK-Remove Prune Image')

#os.system('docker container prune -f')
#print('OK-Remove container prune')

#os.system('docker volume prune -f')
#print('OK-Remove Prune Vol')

#os.system('docker network prune -f')
#print('OK-Remove Network Prune')
print('*********************')

msg = 'Docker-Cleanner Report\n\n' + 'Hostname: ' + getHostname.decode(encoding) + '\nRemove Prune Image:\n' + img_pr_output.decode(encoding) + 'Remove container prune:\n' + con_pr_output.decode(encoding) + 'Remove Prune Vol:\n' + vol_output.decode(encoding) + 'Remove Network Prune:OK\n' + network_output.decode(encoding)

r = requests.post(url, headers=headers , data = {'message':msg})
jsonRes = r.json()

if r.status_code == 200:
	print('Alert to Line Notify: OK')
	print(jsonRes)
else:
	print('Error!!')
	print(jsonRes)



	
