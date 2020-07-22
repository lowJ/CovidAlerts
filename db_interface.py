import sqlite3
conn = sqlite3.connect('users.db')

def add_user(phone_num, state, county):
    #add error catching
    #if phone_num invalid... do...
    #if state/county invalid ... do...
    #if number exists already...
    conn = sqlite3.connect('users.db')          
    c = conn.cursor()        
    c.execute("INSERT INTO subscribers VALUES ('" + str(phone_num) + "','" + str(state) + "','" + str(county) + "')" )
    conn.commit()
    conn.close()

def del_user(phone_num):
    #add error catching
    #if user doesnt exist, do nothing.
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM subscribers WHERE phone = " + "'" + str(phone_num) + "'")
    conn.commit()
    conn.close()

#clears all rows from subscribers
def clear_subscribers():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM subscribers")
    conn.commit()
    conn.close()

def get_user(phone_num):
    return 0

#Calls func on each row
#passes args as -> func(phone, state, county)
def call_on_all_phone_num(func):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM subscribers'):
        func(row[0], row[1], row[2])
    conn.close()

def print_subscribers():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM subscribers'):
        print(row)
    conn.close()
    
    
#makes sure theres no duplicate number/county pairs
def checkDuplicateNumber():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    check = []
    for row in c.execute('SELECT * FROM subscribers'):
        if row not in check:
            check.append(row)
    
    if len(check) == len(c.execute('SELECT * FROM subscribers')):
        conn.close()
        return True
    else:
        conn.close()
        return False
                        

def checkDuplicate():
    pass
