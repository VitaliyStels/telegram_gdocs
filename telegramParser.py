import json

usersData = []
with open('data/usersData.json', 'r') as file:
    usersData = json.load(file)

print(usersData)
