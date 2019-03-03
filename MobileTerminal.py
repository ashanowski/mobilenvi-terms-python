import random
import json
import datetime

class MobileTerminal:
	
	def __init__(self, id: int):
		self.id = id

	def get_data(self):
		self.temp = int(random.normalvariate(16, 5))
		self.pressure = int(random.normalvariate(1011, 15))

	def info(self):
		print("======================")
		print("Stacja {} melduje się!".format(self.id))
		print("Aktualna temperatura: {} C".format(self.temp))
		print("Aktualne ciśnienie: {} hPa".format(self.pressure))
		print("======================")

	def save_json(self):

		data = {"id" : self.id,
				"temp" : self.temp,
				"pressure" : self.pressure}

		now = datetime.datetime.now()

		filename = "term{}_{}.json".format(self.id, now.strftime("%Y-%m-%d_%H-%M"))

		with open(filename, 'w') as outfile:
			json.dump(data, outfile)
