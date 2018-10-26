# -*- coding: utf-8 -*-
"""
@author: https://github.com/fabrajah
"""

import adal
import requests
import getpass
import config

if __name__ == '__main__':
    
    # Get user credentials and consent to permissions
    config.username = getpass.getpass("Please enter your username: ")
    config.password = getpass.getpass("Please enter your password: ")
    
    # Request OAuth bearer token providing an access token
    context = adal.AuthenticationContext(config.authority_url, validate_authority=True, api_version=None)  
    token = context.acquire_token_with_username_password(config.resource, config.username, config.password, config.client_id)
    access_token = token['accessToken']
    print("Token ready.")

    # Call EDP via API URL with the valid access token in Authorization header
    endpoint = config.resource + '/api/' + config.api_data       
    bearer_token = access_token
    r = requests.get(endpoint,headers={"Authorization":"Bearer " + bearer_token})
    
    # Verify call status
    print(endpoint)
    print(r.status_code)
    print(r.text)

    # Fetch API data from  Azure application    
    print(r.content)
    input("\n\nPress the enter key to exit.")  

