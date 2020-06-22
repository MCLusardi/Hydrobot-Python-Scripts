# Test Python control program

import serial
from time import sleep

dev = serial.Serial("COM3", timeout= None baudrate = 9600)
sleep(1)
#dev.write(b'M D 10')
#print("Command sent!")
#sleep(5)

data = []
for _ in range(10):
    #dev.write(b'M D 1')
    sleep(1)
    line = dev.inWaiting()
    data.append(line)
    
    print(data)
