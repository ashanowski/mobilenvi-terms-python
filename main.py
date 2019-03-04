from MobileTerminal import MobileTerminal
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
	
	mt1.info()