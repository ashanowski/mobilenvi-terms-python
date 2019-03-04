import random
import requests

class MobileTerminal:
	
	def __init__(self, id: int):
		self.id = id

	def get_data(self):
		self.temp = int(random.normalvariate(16, 5))
		self.pressure = int(random.normalvariate(1011, 15))

	def info(self):
		print("======================")
		print("Stacja {} melduje się!".format(self.id))
		print("Atrybuty stacji: {}".format(vars(self)))
		print("Aktualna temperatura: {} C".format(self.temp))
		print("Aktualne ciśnienie: {} hPa".format(self.pressure))
		print("======================")

	def send_data(self):
		measures = vars(self)

		credentials = {'login' : self.id,
					   'pass' : "xxxxx"}

		apiUrl = "localhost:8000/api/terminal"

		r = requests.post(apiUrl, args=credentials)

		# TODO: wyciągnąć token z r
		token = 12345

		r = requests.post(apiUrl, data=measures, headers={'Authorization': "Bearer {}"\
																		   .format(token)})