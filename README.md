# Control Linux desktop by Arduino sensors

This project takes ultrasonic sensor for example.

## Requirement

GNU/Linux with Python and `xdotool`.

## How to run

1. Burn `serialSensor.ino` into Arduino.
2. Set serial port name and baud rate in `serialDesktopCtl.sh`.
3. Run command:
        ./seralDesktopCtl.sh

## How it works

1. Arduino send sensor data to serial port.
2. Python read from serial port and control the PC desktop through system command `xdotool`.
3. `xdotool` send keyboard stokes to the operating system.

## License

Public Domain. You can do whatever you want with the code.
