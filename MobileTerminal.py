import random
import requests

class MobileTerminal:
	
	def __init__(self, id: int):
		self.id = id

	def get_data(self):
		""" Gather data from a station """

		self.temp = int(random.normalvariate(16, 5))
		self.pressure = int(random.normalvariate(1011, 15))

	def info(self):
		""" Print info about station """
		print("======================")
		print("Stacja {} melduje się!".format(self.id))
		print("Atrybuty stacji: {}".format(vars(self)))
		print("Aktualna temperatura: {} C".format(self.temp))
		print("Aktualne ciśnienie: {} hPa".format(self.pressure))
		print("======================")

	def send_data(self, show_info=False):
		"""	Send data gathered by simulated station 
			
			Args:
				show_info : Boolean
					Print station's info to console
		"""

		if show_info:
			self.info()

		# data gathered by station
		measurements = {
			"temperature": self.temp,
			"pressure": self.pressure
		}

		# Login and send apis urls
		apiLoginUrl = "http://127.0.0.1:8000/api/station/login"
		apiSendUrl = "http://127.0.0.1:8000/api/station/send"

		print("Preparing to login...")	
		# send station's id with POST
		credentials = {"id": self.id}
		try:
			rlogin = requests.post(apiLoginUrl, data=credentials)
		except requests.exceptions.InvalidSchema:
			print("Failed! Check Login API URL.")
		except requests.exceptions.ConnectionError:
			print("Failed! Check Login API URL.")
		else:
			print("Login ended with success. JWT Token acquired!")

			print("Preparing to send station's data...")
			# grab jwt token
			token = rlogin.json()["token"]

			# send station's data and jwt token in header
			header = {"Authorization": "Bearer {}".format(token)}

			try:
				rsend = requests.post(apiSendUrl, headers=header, data=measurements)
			except requests.exceptions.ConnectionError:
				print("Failed! Check Send API URL.")
			else:
				print("Data successfully sent to server!")