"""
    Main script creating instance of a terminal
    and using its functions

"""
from time import sleep
from mobile_terminal import MobileTerminal


if __name__ == "__main__":
    STATION = MobileTerminal(14)
    while True:
        STATION.get_data()
        STATION.send_data()
        sleep(30 * 60)
