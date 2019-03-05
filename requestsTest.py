import requests

apiLoginUrl = "http://127.0.0.1:8000/api/station/login"
apiUrl = "http://127.0.0.1:8000/api/station/send"

params = {"id": 1}

r = requests.post(apiUrl, data=params)

print("Status code POST 1:", r.status_code)

token = r.json()['token']
print("Token:", token)

head = {"Authorization": "Bearer {}".format(token)} 
data = {
	"temperature": 16,
	"pressure": 1012 
}
print("Header:", head)

rp = requests.post(apiUrl, data=data, headers=head)
print("Status code POST 2:", rp.status_code)