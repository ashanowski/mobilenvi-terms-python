# Mobilenvi - Mobile terminals powered by Raspberry Pi and Python

## About project
Mobilenvi is my university assignment project which integrates Raspberry Pi with our little, custom-made Internet of Things system. Data flows from Adafruit BME280 sensor to the [server written in Laravel](https://github.com/SztukowskiAdam/Mobilenvi-server) and then to the [client app written in Angular](https://github.com/SztukowskiAdam/Mobilenvi-client).

## Modules
* [requests](https://2.python-requests.org/en/master/) for HTTP GET and POST, being more readable than urllib3
* [Adafruit's BME280 module](https://github.com/adafruit/Adafruit_CircuitPython_BME280) providing API to work with the sensor

## Documentation
Currently the documentation is only availaible through inside-code docstrings.

## Usage
Clone the repository to Raspberry Pi with BME280 connected through I2C at address 0x76. Application works only for given API architecture, laying on the server side.
