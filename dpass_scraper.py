#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

"""
url = 'https://www.router-reset.com/default-password-ip-list'
page_data = requests.get(url).text
soup = BeautifulSoup(page_data, 'html.parser')
vendor_table_html = soup.find('table', attrs={'class':'table table-striped table-hover table-bordered'})

router_data = dict()
for row in vendor_table_html.find('tbody').find_all('tr'):
    link = row.find('td').find('a', href=True)['href']
    router_data[link.split('/')[-1]] = dict()

for vendor in router_data.keys():
    page_data = requests.get(url + '/' + vendor).text
    soup = BeautifulSoup(page_data, 'html.parser')
    table = soup.find('table', attrs={'class':'table table-striped table-hover table-bordered'})
    for row in table.find('tbody').find_all('tr'):
        cols = row.find_all('td')

        if len(cols) < 3: continue

        model = cols[0].contents[0].strip()
        router_data[vendor][model] = dict()

        username = cols[1].text.strip()
        router_data[vendor][model]['username'] = None if username == '-' else username

        password = cols[2].text.strip()
        router_data[vendor][model]['password'] = None if password == '-' else password

import pprint
pprint.pprint(router_data)
"""

url = 'https://10-0-0-0-1.com/default-router-passwords-list/'
base_url = 'https://10-0-0-0-1.com/wp-content/plugins/jrouter/brands/%s.htm'
# in javascript so I just grabbed it
vendors = ["2Wire","3COM","3M","3ware","Accelerated Networks","Acconet","ACCTON","accton t-online","Aceex","Actiontec","ADC Kentrox","ADIC","adtran","Advantek Networks","Aethra","Airties","ALAXALA","ALCATEL","Allied","Allied Telesyn","ALLNET","Alteon","AMBIT","Amitech","Andover Controls","AOC","APC","Apple","Areca","Arescom","ARtem","Asante","Ascend","Ascom","asmack","ASMAX","Aspect","ASUS","Atlantis","AVAYA","Axis","AXUS","aztech","Bausch Datacom","Bay Networks","Belkin","Benq","Billion","BinTec","Blue Coat Systems","BMC","BMC Software","Breezecom","Broadlogic","Brocade","Brother","BUFFALO","Cable And Wireless","Cabletron","canyon","Cayman","Celerity","Cellit","Checkpoint","CipherTrust","CISCO","CNET","COM3","Compaq","comtrend","Conexant","Corecess","creative","CTC Union","cyberguard","Cyclades","D-LINK","Dallas Semiconductors","Datacom","Datawizard.net","Davox","DD-WRT","Deerfield","Dell","Demarc","Deutsch Telekomm","Deutsche Telekom","Develcon","Dictaphone","Digicom","Digicorp","Draytek","Dynalink","E-Con","E-Tech","EchoLife","Edimax","Efficient","Efficient Networks","Elsa","Enterasys","Entrust","Ericsson","ESP","EverFocus","Exabyte","Extreme Networks","F5","F5-Networks","Flowpoint","Fortinet","Foundry Networks","Freetech","Fujitsu Siemens","Funk Software","Gericom","giga","GVC","HP","Huawei","iblitzz","IBM","ihoi","IMAI","inchon","Infosmart","Integral Technologies","Intel","Inteno","Interbase","Intermec","Intershop","Intersystems","intex","Inventel","ion","iPSTAR","IronPort","JAHT","JD Edwards","JDE","JDS Microprocessing","Juniper","Kalatel","Konica Minolta","KTI","Kyocera","LANCOM","Lantronics","Lantronix","latis network","LG","Linksys","Livingston","Lockdown Networks","Logitech","longshine","Loopcom","LUCENT","Marconi","maxdata","McAfee","McData","mediatrix 2102","medion","Megastar","Mentec","MERCURY","Meridian","Micronet","Microplex","Microsoft","Mikrotik","Milan","Minolta QMS","Mintel","Mitel","Motorola","mro software","Mutare Software","NAI","NEC","Netcomm","NetGear","NetGenesis","Netopia","Netport","Netscreen","Netstar","Network Appliance","Network Associates","Network Everywhere","Nexxt Solutions","NGSec","Niksun","Nimble","NOKIA","Nortel","NRG or RICOH","Nullsoft","OKI","olitec","olitec (Trendchip)","Omnitronix","OMRON","Onixon","OpenConnect","Openwave","Oracle","Orange","Osicom","ovislink","Pacific Micro Data","Panasonic","penril datability","Pentagram","Pentaoffice","PentaSafe","Perle","Phoenix v1.14","Pirelli","Planet","Polycom","Prestigio","Proxim","Psion Teklogix","Pyramid Computer","Quintum Technologies Inc.","Radware","Raidzone","Ramp Networks","RedHat","Research","Ricoh","RM","RoamAbout","SAGEM","Samsung","Scientific Atlanta","Senao","Server Technology","sharp","SIEMENS","Sigma","Siips","silex technology","sitara","Sitecom","SmartSwitch","SMC","Snapgear","Solution 6","Sonic-X","SonicWALL","SOPHIA (Schweiz) AG","Sorenson","Speedcom","SpeedStream","SpeedXess","Sphairon","Spike","Sun","Sun Microsystems","Sweex","Swissvoice","Sybase","Symbol","T-Comfort","TANDBERG","Tandberg Data","Tandem","Team Xodus","Teklogix","Telco Systems","Teledat","Teletronics","Telewell","Telindus","Tellabs","TENDA","Terayon","Tiara","topsec","TRENDnet","TRICHEER","Troy","TVT System","U.S. Robotics","ubee","UNEX","Uniden","Unisys","US Robotics","us21100060","V-Tech","VASCO","Verifone","Verilink","Virgin Media","Visual Networks","Vodafone","Vonage","VxWorks","Wanadoo","Wang","WatchGuard","Westell","Wyse","X-Micro","Xavi","xd","Xerox","Xylan","Xyplex","Yakumo","Zcom","Zebra","Zonet","ZOOM","ZTE","ZXDSL","ZyXEL"]
for vendor in vendors:
    soup = BeautifulSoup(requests.get(base_url % vendor).text, 'html.parser')
    vendor_table_html = soup.find('table')
    print(vendor_table_html)
    input()
