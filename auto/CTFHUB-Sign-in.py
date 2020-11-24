# -*- coding: utf-8 -*-
# @Author  : Zoey Zhao
# @Time    : 2020/11/20 11:40
# @Function: CTFHUB自动签到

import requests

url = "https://api.ctfhub.com/User_API/User/checkIn"

payload = "{}"
headers = {
  'Authorization': 'ctfhub_sessid=<your sessid>',
  'Content-Type': 'application/json;charset=UTF-8',
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


