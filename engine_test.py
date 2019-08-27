#!/usr/bin/env python

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #
from time import sleep

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Each of the following BP.get functions return a value that we want to display.
print("Manufacturer    : ", BP.get_manufacturer()    ) # read and display the serial number
print("Board           : ", BP.get_board()           ) # read and display the serial number
print("Serial Number   : ", BP.get_id()              ) # read and display the serial number
print("Hardware version: ", BP.get_version_hardware()) # read and display the hardware version
print("Firmware version: ", BP.get_version_firmware()) # read and display the firmware version
print("Battery voltage : ", BP.get_voltage_battery() ) # read and display the current battery voltage
print("9v voltage      : ", BP.get_voltage_9v()      ) # read and display the current 9v regulator voltage
print("5v voltage      : ", BP.get_voltage_5v()      ) # read and display the current 5v regulator voltage
print("3.3v voltage    : ", BP.get_voltage_3v3()     ) # read and display the current 3.3v regulator voltage

def find_extreme_position(direction):

    previous_extreme = None
    while True:
        BP.set_motor_power(BP.PORT_D, direction * 20)
        time.sleep(0.05)

        new_extreme = BP.get_motor_encoder(BP.PORT_D)
        if previous_extreme ==  new_extreme:
            return previous_extreme

        print(new_extreme)
        previous_extreme = new_extreme

try:
    try:
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
    except IOError as error:
        print(error)

    extreme_left = find_extreme_position(1)
    extreme_right = find_extreme_position(-1)
    center = int((extreme_left + extreme_right) / 2)

    while True:
        BP.set_motor_position(BP.PORT_D, center)
        time.sleep(0.02)

        BP.set_motor_power(BP.PORT_B, 100)
        BP.set_motor_power(BP.PORT_C, -100)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.