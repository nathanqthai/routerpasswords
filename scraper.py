#!/usr/bin/env python3

import ast
from bs4 import BeautifulSoup
import requests

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
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
js = soup.find_all('script')[-1]['src']
vendors = None
for line in requests.get(js).text.split('\n'):
    if line.find('2Wire') != -1:
        vendors = ast.literal_eval(line[line.index('['):line.index(']')+1])
vendors = [vendor.lower() for vendor in vendors]

router_data = dict()
base_url = 'https://10-0-0-0-1.com/wp-content/plugins/jrouter/brands/%s.htm'
for vendor in vendors:
    soup = BeautifulSoup(requests.get(base_url % vendor).text, 'html.parser')
    table = soup.find('table', attrs={'class':'table table-bordered table-striped'})
    if table is None:
        continue

    try:
        router_data[vendor] = dict()
        for row in table.find('tbody').find_all('tr'):
            cols = row.find_all('td')

            model = cols[1].text.strip()
            if model == '':
                model == 'default'
            model = model.lower()
            router_data[vendor][model] = dict()

            username = cols[3].text.strip()
            router_data[vendor][model]['username'] = None if username in ['(blank)', '(none)', '-', 'n/a'] else username

            password = cols[4].text.strip()
            router_data[vendor][model]['password'] = None if password in ['(blank)', '(none)', '-', 'n/a'] else password
    except:
        import pdb
        pdb.set_trace()

import pprint
pprint.pprint(router_data)

