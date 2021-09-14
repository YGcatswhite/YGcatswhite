import requests
import json

r = requests.get("https://api.github.com/users/YGcatswhite/repos")
data = json.loads(r.text)
repo = data[0]
owner = repo['owner']
commits = repo['url'] + '/commits'
l  = []


for _ in data:
    if _['fork'] == True:
        continue
    commits = requests.get(_['url']+'/commits').text
    commits = json.loads(commits)
    l.append([_, len(commits)])


l = sorted(l, key=lambda x: x[1])
l.reverse()
for _ in l[:5]:
    repo = _[0]
    commits = repo['url']+'/commits'
    print(commits)
