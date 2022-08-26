import sys
sys.path.insert(1, 'Swagger')

import json
import requests
import swagger_client

CLIENT_ID = 'clientId'
CLIENT_SECRET = 'clientSecret'
HOST = "https://api.globalforester.com"


def get_access_token():
    token_url = 'https://auth2.globalforester.com/oauth2/token'
    grant_type='client_credentials'
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    basic_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    response = requests.post(token_url, params={'grant_type':grant_type}, headers = headers, auth=basic_auth)
    resp_json = json.loads(response.text)
    access_token=resp_json['access_token']
    return access_token

def configure_swagger_client():
    configuration = swagger_client.Configuration()
    configuration.access_token = get_access_token()
    configuration.host = HOST
    return configuration
