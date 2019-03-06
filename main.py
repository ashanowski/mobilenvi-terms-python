from MobileTerminal import MobileTerminal
import time
import schedule
import requests

if __name__ == "__main__":

	apiGetIdUrl = "http://127.0.0.1:8000/api/station/list"
	
	id_request = requests.get(apiGetIdUrl)
	idList = id_request.json()["stations"]

	stations = {id: MobileTerminal(id) for id in idList}

	def job():
		for id in stations:
			stations[id].get_data()
			stations[id].send_data()
	

	schedule.every(5).seconds.do(job)

	while True:
		schedule.run_pending()
