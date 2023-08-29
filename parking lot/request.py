import requests

url = "my-cat-api/endpoint"
data = {"cat": 1, "doc": "no"}
headers = {"authorization": "Bearer eyHoLetsgo", "X-User-Id": "123321"}
receba = requests.get(url=url, headers=headers)
print(receba.text)
print(receba.json())
