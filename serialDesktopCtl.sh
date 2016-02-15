#!/bin/bash

# Control PC desktop via serial port

# Set the serial port name
PORT=/dev/ttyACM0
# Set the serial port baud rate
BAUD=9600

python serialDesktopCtl.py $PORT $BAUD
