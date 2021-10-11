import requests , sys , time

from multiprocessing.dummy import Pool


def import_proxies(path):
	proxies = open(path , "r").read().splitlines()
	print (f"{P}[+] Proxies Count : {len(proxies)}{N}")
	proxies = list(set(proxies))
	print (f"{P}[+] Proxies After Removing Duplicates : {len(proxies)}{N}")
	print(P+"="*54+N+"\n")
	return proxies


def checker(proxy):
	url = "http://google.com"
	proxies = {"http" : proxy , "https" : proxy}
	headers = {"User-agent" : "Mozilla/5.0"}
	try:
		requests.get(url , proxies = proxies , headers = headers , timeout = 10)
		alive.append(proxy)
		save_file.write(proxy+"\n")
		print(f"{G}[+] Success\t: {proxy} {N}")
	except:
		dead.append(proxy)
		print(f"{R}[+] Failure\t: {proxy} {N}")
	prx.remove(proxy)
	


if __name__ == "__main__":
	
	R = "\033[1;31m"
	P = "\033[1;35m"
	G = "\033[1;32m"
	Y = "\033[1;33m"
	N = "\033[m"
	
	alive = []
	dead = []
	
	mp = Pool(300)
	
	path = "/sdcard/all_proxies.txt"
	path = input(f"{P}[+] Entre Proxies File Path : ") or path
	print("="*54+N)
	save_file = open("/sdcard/alive_proxies.txt" , "a")
	
	prx = import_proxies(path)

while len(prx) > 0:
	mp.map(checker , prx)
	
print(f"\n{Y}[+] All Proxies Checked!")
print("="*54+N)
print(f"{G}[×] Alive\t: {len(alive)}{N}")
print(f"{R}[×] Dead\t: {len(dead)}{N}")