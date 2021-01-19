import requests
import json

payload = json.dumps({'last': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
# print(payload)
r = requests.post('http://127.0.0.1:5000/predict', json=payload)
data = json.loads(r.content)
print(data)

