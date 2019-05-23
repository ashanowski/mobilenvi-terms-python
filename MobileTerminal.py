import random
import requests
import json


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
		base_url = "http://192.168.43.10:8000"
		apiLoginUrl = base_url + "/api/station/login"
		apiSendUrl = base_url + "/api/station/send"

		print("Station {}: Preparing to login...".format(self.id))
		# send station's id with POST
		credentials = {"id": self.id}
		try:
			rlogin = requests.post(apiLoginUrl, data=credentials)
			token = rlogin.json()["token"]
		except requests.exceptions.InvalidSchema:
			print("Station {}: Failed! Check Login API URL.".format(self.id))
		except requests.exceptions.ConnectionError:
			print("Station {}: Failed! Check Login API URL.".format(self.id))
		except json.decoder.JSONDecodeError:
			error = "Station {}: Failed! Station hasn't been authorized. It may not be in database.".format(self.id)
			print(error)
			return error
		else:
			print("Station {}: Login ended with success. JWT Token acquired!".format(self.id))

			print("Station {}: Preparing to send station's data...".format(self.id))

			# send station's data and jwt token in header
			header = {"Authorization": "Bearer {}".format(token)}

			try:
				rsend = requests.post(apiSendUrl, headers=header, data=measurements)
			except requests.exceptions.ConnectionError:
				print("Station {}: Failed! Check Send API URL.".format(self.id))
			else:
				print("Station {}: Data successfully sent to server!".format(self.id))
