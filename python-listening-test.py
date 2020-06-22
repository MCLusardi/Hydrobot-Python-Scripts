#python reading test script

import serial
from time import sleep #for sleep and time
import re #regular expression operators

serialString = ""
val = '0.00'
list = []
#file = open("data.txt", "w") #opening file for writing
serialNumber = ""

serialPort = serial.Serial("COM3", baudrate = 9600)


while(1):
    #Wait until there is data waiting in serial buffer
    if(serialPort.in_waiting > 0):
        #Read data out of the buffer until carriage return / newline
        serialString = serialPort.readline()
        
        #Print the contents of serial data
        print(serialString.decode('Ascii'))
        
        #decoding into ascii for testing splitting
        serialStringAscii = serialString.decode('Ascii')
        
        
        #reg exp to pull out the value from the sensor to write to file
        '''serialNumber = (re.search(r'\d+\.\d+', serialString.decode('utf-8')).group())
        #print(serialNumber)
        
        #writing to data.txt file to store
        #format as %f %DATE_RECORDED
        file.write(serialNumber)
        file.write(',') # so to split string by ':' when parsing for graphs
        file.write(time.asctime(time.localtime(time.time())))
        file.write('\n')'''
        

        
        
        
      
        #sleep(1) #for testing   
        
        #Tell we recieved data, commented out of example
        #serialPort.write(b"Thank you for sending data \r\n")
        #the b in front of string indicates to send bytes!