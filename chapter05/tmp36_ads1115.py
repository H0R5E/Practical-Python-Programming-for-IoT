"""
File: chapter05/tmp36_ads1115.py

Read TMP36 from an ADS1115 ADC I2C module.

Dependencies:
  pip3 install pigpio adafruit-circuitpython-ads1x15

Built and tested with Python 3.7 on Raspberry Pi 4 Model B
"""
from time import sleep

# Below imports are part of Circuit Python and Blinka
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus & ADS object.
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, gain=2)

# Analog Inputs on Channels 0 (A0 on breakout board)
temp_ch = AnalogIn(ads, ADS.P0)  #ADS.P0 --> A0

if __name__ == '__main__':
    try:
        while True:
            output = ("TMP36 (A0) value={:>5} volts={:>5.3f}")
            output = output.format(temp_ch.value, temp_ch.voltage)

            print(output)
            sleep(0.05)

    except KeyboardInterrupt:
        i2c.deinit()