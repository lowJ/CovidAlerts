import sqlite3
conn = sqlite3.connect('users.db')

#Adds a user
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
 
#Deletes all of the user's sign ups
def clear_user(phone_num):
    #add error catching
    #if user doesnt exist, do nothing.
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM subscribers WHERE phone = " + "'" + str(phone_num) + "'")
    conn.commit()
    conn.close()
    

#Deletes a user county pair
def del_user(phone, state, county):
    pass


#clears all rows from subscribers
def clear_subscribers():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM subscribers")
    conn.commit()
    conn.close()


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
    tableSize = 0
    for row in c.execute('SELECT phone FROM subscribers'):
        tableSize += 1
        if row not in check:
            check.append(row)

    if len(check) == tableSize:
        conn.close()
        return True
    else:
        conn.close()
        return False



#Checks to see if there is a duplicate phone/county pair
#returns true if there is and false if there isn't
def checkDuplicate(phone, county, state):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    check = c.execute(f'SELECT * from subscribers where phone = "{phone}" and county = "{county}" and state = "{state}"')
    if len(check.fetchall()) > 0:
        return True
    conn.close()
    return False

