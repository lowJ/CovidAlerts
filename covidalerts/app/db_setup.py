#Execute this script once if users.db is empty
import sqlite3
conn = sqlite3.connect('users.db')

c = conn.cursor()
c.execute('''CREATE TABLE subscribers
             (phone, state, county)''')


conn.commit()

conn.close()