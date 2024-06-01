# -*- coding: utf-8 -*-
'''
Created on Thu May 30 18:50:23 2024

@author: Mattias Herrfurth
'''

import os
import json
import tableauserverclient as TSC
from getpass import getpass

# storing the key in a separate file outside of any cloud file syncing
# using this function to simply get the key from the file
def getSecret(name):
    secrets_filename = name
    api_keys = {}
    with open(secrets_filename, 'r') as f:
        api_keys = json.loads(f.read())
    return api_keys['tab_key']

# collecting the cert chain from a pem file
def getCertChain():
    return os.path.join(os.path.expanduser('~'), r'C:\path\to\certchain.pem')

# getting current username and asking for password
user = os.environ['USERNAME']
pswd = getpass()

# other variables
url = 'https://my.tableau.domain.com'
site = 'mysite'
name = r'C:\path\to\key.json'
token_name = 'token_name'
token_value = getSecret(name)

# creating empty URLs list
all_urls = []

# get authorization and secure connection
tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token_value, site)
server = TSC.Server(url, use_server_version=True)
server.add_http_options({'verify': getCertChain()})

# populate the list with all URLs
with server.auth.sign_in(tableau_auth):
    for view in TSC.Pager(server.views):
        all_urls += [f'''{url}/#/site/{site}/views/{view.content_url.replace('sheets/','')}''']

# print all URLs
for url in all_urls:
    print(url)