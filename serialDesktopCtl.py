import argparse
import os
import serial

class DesktopCtl():
    def __init__(self, device, port):
        self.ser = serial.Serial(device, port)
        self.currDistance = 1000
        self.lastDistance = 1000
    def read(self):
        while True:
            # Read from serial
            line = self.ser.readline()
            # Safe cast float number
            try:
                self.currDistance = float(line)
                print(self.currDistance)
                return
            except ValueError:
                continue
    def run(self):
        # Infinite loop keep monitoring serial port
        while True:
            self.read()
            # Trigger condition
            if self.currDistance < 50 and self.currDistance > 30:
                print("-------")
                self.read()
                self.read()
                self.read()
                self.read()
                self.read()
                self.read()
                if self.currDistance < 25:
                    print("Trigger")
                    cmd = "xdotool key super+Tab"
                    os.system(cmd)
            if self.lastDistance > 30 and self.currDistance < 10:
                print("Trigger")
                #cmd = "xdotool key super"
                #cmd = "xdotool key ctrl+alt+Down"
                cmd = "xdotool key Escape"
                os.system(cmd)
            self.lastDistance = self.currDistance
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Control Linux Desktop by Arduino over serial port.')
    parser.add_argument('device', help='Device, e.g. /dev/ttyACM0')
    parser.add_argument('port', help='Port, e.g. 9600')
    args = parser.parse_args()

    desktopCtl = DesktopCtl(args.device, args.port)
    desktopCtl.run()
