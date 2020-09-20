# Coded By: Rizky | Aprilia
# github: https://github.com/hekelpro
# Team: XIUZCODE | OPEN SOURCE TEAM

import os
from requests import *
from bs4 import BeautifulSoup as par

os.system('clear')
link = 'https://createssh.com/'
a = get(link).content
b = par(a,"html.parser")
no = 0
print("""
\x1b[1;92m     ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦ ╦
     ║  ╠╦╝║╣ ╠═╣ ║ ║╣   ╚═╗╚═╗╠═╣
     ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝  ╚═╝╚═╝╩ ╩
\x1b[1;91m----------------------------------------""")
for cen in b.find_all('h2'):
	no += 1
	print('\x1b[1;97m[\x1b[1;92m0'+str(no)+'\x1b[1;97m]=| '+cen.text)
print("\x1b[1;91m-"*40)
pil = input('\x1b[1;97m[\x1b[1;96m+\x1b[1;97m] PILIH:\x1b[1;92m ')
if pil == "":
	exit("\x1b[1;97m[\x1b[1;91m×\x1b[1;97m] Mohon Jangan Kosong\n")
elif pil in ("1","01"):
	server = "server/tokyo.html"
elif pil in ("2","02"):
	server = "server/paris.html"
elif pil in ("3","03"):
	server = "server/singapore-1.html"
elif pil in ("4","04"):
	server = "server/sydney.html"
elif pil in ("5","05"):
	server = "server/london.html"
elif pil in ("6","06"):
	server = "server/united-states-1.html"
elif pil in ("7","07"):
	server = "server/united-states-2.html"
elif pil in ("8","08"):
	server = "server/singapore-2.html"
else:
	exit("\x1b[1;97m[\x1b[1;91m×\x1b[1;97m] Mohon Isi Yang Bener\n")
c = get(link+server).content
d = par(c,"html.parser")
e = d.find("input", attrs={"name":"type"})
f = d.find("input", attrs={"name":"code"})
user = input("\x1b[1;97m[\x1b[1;96m*\x1b[1;97m] SET USERNAME:\x1b[1;92m ")
pasw = input("\x1b[1;97m[\x1b[1;96m*\x1b[1;97m] SET PASSWORD:\x1b[1;92m ")
if user == "" and pasw == "":
	exit("\x1b[1;97m[\x1b[1;91m×\x1b[1;97m] Mohon Jangan Kosong\n")
print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Tunggu Sebentar\x1b[1;91m...")
data = {
	"username":user,
	"password":pasw,
	"type":e.get("value"),
	"code":f.get("value")
	}
print("\x1b[1;91m-"*40)
requ = post("https://createssh.com/server/new/create/index.php", headers={"user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36"}, data=data).text
bs = par(requ,"html.parser")
if "SSH Account Successfull Created!" in requ:
	for h3 in bs.find_all('h3'):
		h3 = (h3.text).replace("		:"," :").replace("Server Status :","Server Status    :").replace("Request Server","SSL/TLS          : 443\nSquid Proxy	 : 8080\nDropbear	 : 442, 109, 3128\nStatus Result    : Successfull Created!\n\x1b[1;91m----------------------------------------\n").replace(": Join Group Facebook","\n")
		print("\x1b[1;97m"+h3)
else:
	exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Terjadi Kesalahan\n")

"""sejelek jelek karya orang hargain gan walaupun itu yaa gak berguna"""
