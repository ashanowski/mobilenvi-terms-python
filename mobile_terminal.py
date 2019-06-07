"""
    Module containing class representing MobileTerminal
    that is used to gather environment data of Temperature
    and pressure.

"""
import json
import logging
import requests
try:
    import board
    import busio
    import adafruit_bme280
except NotImplementedError:
    logging.error('Application needs to be run on a Raspberry Pi!')


class MobileTerminal:
    """ Raspberry Pi terminal gathering data from the BME280 sensor,
        and sending it to the external server.

        Attributes
        ----------
            terminal_id : int
                Identity number of a terminal

            sensor : Adafruit_BME280_I2C
                Object representing BME280 sensor connected with I2C,
                gathering data from environment

            temperature : float
                Temperature gathered by BME280 sensor

            pressure : float
                Pressure gathered by BME280 sensor
    """

    def __init__(self, terminal_id: int):
        self.terminal_id = terminal_id
        self.sensor = adafruit_bme280.Adafruit_BME280_I2C(
                        busio.I2C(board.SCL, board.SDA), 118)
        self.temp, self.pressure = 0.0, 0.0

    def get_data(self, temp_precision=0, pressure_precision=0):
        """ Gather data from the sensor

            Arguments
            ---------
                temp_precision : int
                    Precision of temperature

                pressure_precision : int
                    Precision of pressure
        """
        self.temp = round(self.sensor.temperature, temp_precision)
        self.pressure = round(self.sensor.temperature, pressure_precision)

    def info(self):
        """ Print info about station """
        print('======================')
        print('Station {} is online!'.format(self.terminal_id))
        print('Temperature: {} C'.format(self.temp))
        print('Pressure: {} hPa'.format(self.pressure))
        print('======================')

    def send_data(self, show_info=False):
        """ Send data gathered by terminal's sensor to the external server

            Arguments
            ---------
                show_info : bool
                    Print station's info to console
        """

        if show_info:
            self.info()

        # data gathered by station
        measurements = {
            'temperature': self.temp,
            'pressure': self.pressure
        }

        base_url = 'http://192.168.43.10:8000'
        api_login_url = base_url + '/api/station/login'
        api_send_url = base_url + '/api/station/send'

        logging.info('Station %s: Preparing to login...', self.terminal_id)
        credentials = {'terminal_id': self.terminal_id}
        try:
            login_request = requests.post(api_login_url, data=credentials)
            token = login_request.json()['token']
        except requests.exceptions.Invalterminal_idSchema:
            logging.error('Station %s: Failed! Check Login API URL.',
                          self.terminal_id)
        except requests.exceptions.ConnectionError:
            logging.error('Station %s: Failed! Check Login API URL.',
                          self.terminal_id)
        except json.decoder.JSONDecodeError:
            logging.error('Station %s: Failed! Station not authorized.',
                          self.terminal_id)
        else:
            logging.info('Station %s: Login successful. JWT Token acquired!',
                         self.terminal_id)
            logging.info('Station %s: Preparing to send station\'s data...',
                         self.terminal_id)

            header = {'Authorization': 'Bearer {}'.format(token)}

            try:
                send_request = requests.post(api_send_url, headers=header,
                                             data=measurements)
            except requests.exceptions.ConnectionError:
                logging.error('Station %s: Failed! Check Send API URL.',
                              self.terminal_id)
            else:
                logging.info('Station %s: Data successfully sent to server!',
                             self.terminal_id)
