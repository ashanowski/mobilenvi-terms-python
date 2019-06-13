"""
    Main script creating instance of a terminal
    and using its functions

"""
from time import sleep
from mobile_terminal import MobileTerminal


if __name__ == "__main__":
    STATION = MobileTerminal(14)
    while True:
        STATION.get_data(temp_precision=1, pressure_precision=1)
        STATION.send_data()
        sleep(5)
