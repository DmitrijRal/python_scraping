import requests
import json

url = 'https://api.vk.com/method/users.get?user_ids=dmitriyral&fields=bdate&access_token=7986f3fa7986f3fa7986f3fa4a79f11ebf779867986f3fa19208d579dc9af6b96da5cf9&v=5.130'
r = requests.get(url)
with open('vk.json', 'w') as f:
    json.dump(r.json(), f)