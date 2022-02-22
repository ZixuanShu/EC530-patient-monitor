import requests

BASE = "http://127.0.0.1:5000"

#response = requests.put(BASE + "/patientinfo/4", {"name": "Geo", "age": 18, "gender": "male", "bloodtype": "O", "height": 175, "weight": "77kg"})
#input()
response = requests.get(BASE + "/patientinfo/6")
print(response.json())