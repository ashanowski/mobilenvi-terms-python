from MobileTerminal import MobileTerminal
import schedule
import time

if __name__ == "__main__":

	mt1 = MobileTerminal(1)
	mt1.get_data()

	mt2 = MobileTerminal(2)
	mt2.get_data()
	
	def job1():
		mt1.get_data()
		mt1.info()

	def job2():
		mt2.get_data()
		mt2.info()

	schedule.every(5).seconds.do(job1)
	schedule.every(5).seconds.do(job2)

	mt1.save_json()