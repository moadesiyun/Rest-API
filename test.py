import requests

from main import Video

BASE = "http://127.0.0.1:5000/"

"""
data =[{"likes": 100, "name": "Jill", "views": 100000},
       {"likes": 5000, "name": "How to Rest", "views": 800000},
       {"likes": 45, "name": "Tim", "views": 2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

"""

response = requests.patch(BASE + "video/2", {})
print(response.json())