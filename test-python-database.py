#A minimal SQLite shell for experiments

import sqlite3

con = sqlite3.connect('test.db')
con.isolation_level = None
cur = con.cursor()

buffer = ""

cur.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

print("Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line to exit.")

while True:
    line = input()
    if line == "": #if nothing entered
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer) #sends command to database

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()