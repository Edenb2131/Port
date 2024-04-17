# Dependencies to install:
# $ python -m pip install requests

import requests

CLIENT_ID = 'WL92dw5KSobwoBwLOa7UTgMob8gBgB8G'
CLIENT_SECRET = 'lBbnVGRDRejTA3p0yLrHEYxROSuSaheqvJORZPj2duPkDruIIsqpo6fN273oFx4o'

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']
# print(access_token)
# You can now use the value in access_token when making further requests
