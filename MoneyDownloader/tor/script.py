#C:\MyProjects\GetMoney\tor\Tor\tor.exe -f C:\MyProjects\GetMoney\tor\Data\Tor\torrc
'''
from stem import Signal
from stem.control import Controller


with Controller.from_port(port=9051) as controller:
	controller.authenticate()
	controller.signal(Signal.NEWNYM)


try:
	request = session.get('http://icanhazip.com/', proxies={'http//': '127.0.0.1:9051'}, headers=useragent, timeout=5)
	if request.status_code == 200:
		print(request.content)
except requests.exceptions.ConnectionError:
	print('error')
except:
	print('fatal')
'''

import requests
from stem import Signal
from stem.control import Controller
from stem import CircStatus
useragent = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def getIP():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		for circ in controller.get_circuits():
			if circ.status != CircStatus.BUILT:
				continue



			exit_fp, exit_nickname = circ.path[-1]


			exit_desc = controller.get_network_status(exit_fp, None)
			exit_address = exit_desc.address if exit_desc else 'unknown'



			print ("Exit relay")
			print ("  fingerprint: %s" % exit_fp)
			print ("  nickname: %s" % exit_nickname)
			print ("  address: %s" % exit_address)
			
			session = requests.Session()
			request = session.get('http://icanhazip.com/', proxies={'http://': '127.0.0.1:9051'}, headers=useragent, timeout=5)
			if request.status_code == 200:
				print(request.content)


def newIP():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
		print("\n\nNEW IP, NEW IP\n\n")



getIP()
newIP()
getIP()
