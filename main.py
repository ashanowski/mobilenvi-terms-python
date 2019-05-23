from MobileTerminal import MobileTerminal
import time
import requests

if __name__ == "__main__":

    station = MobileTerminal(14)
    while True:
        station.get_data()
        station.send_data()

        sleep(5)
