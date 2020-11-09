import serial
import time
import re

#string to hold data from arduino
serialString = ""

#Open the file for writing data (will create file if it doesn't exist yet)
file = open("testECPHoutput.txt", "w")

#Opens the serial port where the arduino sends and receives data
serialPort = serial.Serial("COM3", baudrate = 9600)
print("Hello there") #print statements go to the terminal. Useful for debugging.
print(serialPort.name)
serialPort.write(b"C,1") #tell arduino to send data every 5 seconds
print("Sent message to serialPort")
serialPort.flush()
