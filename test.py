import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 78, "name": "Joe", "views": 10000},
#         {"likes": 48, "name": "Mahsa", "views": 25000},
#         {"likes": 30, "name": "Tim", "views": 5800}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
response = requests.get(BASE + "video/2")
print(response.json())