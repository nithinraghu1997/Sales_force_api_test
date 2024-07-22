import requests
import json

params = {
    "grant_type": "password",
    "client_id": "3MVG9q4K8Dm94dAytBhE98w_LgcUTAdzMtqqWw.QRJ7HCcaMfvzRpiK5j0OeaUIWYPdx6g3TESIj6lT2ADPLO",
    "client_secret": "C21F791263875B90431AFF0CB93866B57D3EE9F4C982CBBFB4D1FADA60478604",
    "username": "amarnathmahato109-f1hl@force.com",
    "password": "salesforce1wxZfnGQnsDilwzeWbzw4UStm"
}

r = requests.post("https://login.salesforce.com/services/oauth2/token", data=params)

if r.status_code == 200:
    response_data = r.json()
    access_token = response_data.get("access_token")
    instance_url = response_data.get("instance_url")

    print("Access Token:", access_token)
    print("Instance URL:", instance_url)

    def sf_Call(action, parameters={}, method='get', data={}):
        headers = {
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Bearer ' + access_token
        }

        if method == 'get':
            r = requests.request(method, instance_url + action, headers=headers, params=parameters, timeout=30)
            return r.json()
        else:
            raise ValueError("Method should be GET")

    
    SQLdata = json.dumps(sf_Call('/services/data/v42.0/query/', {'q': 'SELECT Name, Phone FROM Account'}))
    print(SQLdata)

else:
    print("Failed to obtain access token:", r.text)
