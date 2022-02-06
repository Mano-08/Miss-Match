import json

# file read
with open("BCHacks.json") as f:
    data = json.load(f)

for hacker in data["hackers"]:
    print(hacker) 