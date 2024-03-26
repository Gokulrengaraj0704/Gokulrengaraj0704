import requests

json_file = {"name": "morpheus", "job":"leader"}

res = requests.post(url="https://reqres.in/api/users", json=json_file)

print(res)
print(res.json)

