import requests

BASE = "http://0.0.0.0:80"

response = requests.put(BASE + "/patientinfo/4", {"name": "Geo", "age": 18, "gender": "male", "bloodtype": "O", "height": 175, "weight": "77kg"})
input()
response = requests.get(BASE + "/patientinfo/4")
print(response.json())
input()
response = requests.delete(BASE + "/patientinfo/4")
print(response)