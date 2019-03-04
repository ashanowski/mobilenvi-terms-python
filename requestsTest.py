import requests

apiUrl = 'localhost:8000/api/terminal'
headers={'Authorization':'Basic elo:melo'}
r = requests.get('https://httpbin.org/basic-auth/elo/melo', auth=("elo", "melo"))

print(r.status_code)
print(r.headers)
print(r.text)