#python sensor controller listener
#Need to add sending commands to while loop
#Need to add try-catch excepts for messing up with data
#Need to connect and disconnect from serial port if errors occurs

import serial #for serial communication
import time #for sleep and other time related functions
import datetime #for dates
import re #regex
import os #operating system functions
import sqlite3 #for sqlite database
from sqlite3 import Error #for errors

serialString = "" #holds recieving string from arduino mega
ECvalue = 0.00 #value of EC sensor
DOvalue = 0.00 #value of DO sensor
PHvalue = 0.00 #value of PH sensor

#Serial port for Arduino MEGA
serialPort = serial.Serial("COM3", baudrate = 9600)

#from https://www.sqlitetutorial.net/sqlite-python/create-tables/
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

#from https://www.sqlitetutorial.net/sqlite-python/create-tables/
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#from (loosely) https://www.sqlitetutorial.net/sqlite-python/insert/
def insert_data(conn, data, table_name):
    """
    Inserts data from sensors into data table
    :param conn: Connection object
    :param data: data to insert into table
    """
    try:
        sql = '''INSERT INTO ''' + table_name + ''' (PH, DiO, Cond, Date) VALUES(?,?,?,?)'''
        c = conn.cursor()
        c.execute(sql, data)
    except Error as e:
        print(e)

def main(): #main function
    data = [] #array for data
    
    #connecting to database
    conn = create_connection(r'C:\Users\Landon\Desktop\test.db') #connection for sqlite3 database
    
    #opening new table in database
    table_name = "sensorData_"
    table_name = table_name + datetime.datetime.now().strftime("%d%b%Y")
    #for some reason sqlite does not like DO being used in a command...
    table_create_command = "CREATE TABLE IF NOT EXISTS " + table_name + " (PH REAL, DiO REAL, Cond REAL, Date TEXT);"
    
    #print(table_create_command) #for debugging
    
    #creates table to store data
    if conn is not None:
        #create data table
        create_table(conn, table_create_command)
    else:
        print("Error in opening database, cannot create database connection")

    #infinite loop for recieving data
    while(1):
        #sending commands if any
        #TODO
        #if(serialPort2.in_waiting > 0): #anything recieved from command computer
            #Then send the communication wherever it should be
    
        #Wait until there is data waiting in serial buffer
        if(serialPort.in_waiting > 0):
            #Read data out of the buffer until carriage return / newline
            serialString = serialPort.readline()
            
            #Print the contents of serial data, debugging
            #print(serialString.decode('Ascii'))
            
            #decoding into ascii for testing splitting
            serialStringAscii = serialString.decode('Ascii')
            
            #split at ':'
            splitString = serialStringAscii.split(':')
            
            #Puts respective sensor values into sensor data array in order then
            #writes to file at EC value
            if splitString[0] == "PH":
                PHvalue = (re.search(r'\d+\.\d+', serialString.decode('utf-8')).group())
                data.append(PHvalue)
            elif splitString[0] == "DO":
                DOvalue = (re.search(r'\d+\.\d+', serialString.decode('utf-8')).group())
                data.append(DOvalue)
            elif splitString[0] == "EC":
                COvalue = (re.search(r'\d+\.\d+', serialString.decode('utf-8')).group())
                data.append(COvalue)
                data.append(time.asctime(time.localtime(time.time())))
                #writing to file below
                '''file = open("data.txt", "a")
                for x in data:
                    file.write(x)
                    file.write(",")
                #writing time recorded
                file.write(time.asctime(time.localtime(time.time())))
                file.write('\n')
                data = []'''
                #writing to database
                insert_data(conn, data, table_name)
                conn.commit()
                data = []
                #may need to close database connection
                
    conn.commit()
    conn.close()

    
#runs main function
if __name__ == "__main__":
    main()