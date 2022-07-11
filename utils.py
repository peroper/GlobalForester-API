import sys
sys.path.insert(1, 'Swagger')

import json
import requests
import swagger_client

def get_access_token():
    token_url = 'https://auth2.globalforester.com/oauth2/token'
    grant_type='client_credentials'
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Authorization': 'Basic ZTg5ZXFrZ3Q0amxtODdwZGY4NGprcWpzNTo1cHVjZ3UzYTFvc3RvdGNoYmlpcGxiZnRxb2k2NjFzdGd2c2xta2ZqNzlqY2U3YTB0N2o='}

    response = requests.post(token_url, params={'grant_type':grant_type}, headers = headers)
    resp_json = json.loads(response.text)
    access_token=resp_json['access_token']
    return access_token

def configure_swagger_client():
    configuration = swagger_client.Configuration()
    configuration.access_token = get_access_token()
    configuration.host = "https://api.test.globalforester.com"
    return configuration
