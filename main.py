from MobileTerminal import MobileTerminal
import time
import schedule

if __name__ == "__main__":
	mt1 = MobileTerminal(1)
	def job1():
		mt1.get_data()
		mt1.send_data(show_info=True)
	
	schedule.every(5).seconds.do(job1)

	while True:
		schedule.run_pending()
