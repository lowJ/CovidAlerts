import csv
import urllib.request as request
import time
import sms
import db_interface
import data_processing

#Helper to send text message
def sendMessage(phone, state, county):
    r = data_processing.getday(state, county)
    if r is None:
        to_send = f"Could not find {county}, {state} in database."
    else:
        cases, deaths = r
        to_send = f"Todays confirmed cases in {county} {state}: " + str(cases) + " confirmed deaths: " + str(deaths)

    sms.send_message(phone, to_send)

    
def update():
    try:
        #updated live file
        r = request.urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv").read().decode('utf8').split("\n")
        reader = csv.reader(r)

        with open("live-us-counties.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in reader:
                writer.writerow(line)

        #update the past file
        r2 = request.urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv").read().decode('utf8').split("\n")
        reader2 = csv.reader(r2)

        with open("ago-us-counties.csv", "w", newline="") as csvfile2:
            writer2 = csv.writer(csvfile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in reader2:
                writer2.writerow(line)

        #Sends out texts to all users if update was successful
        db_interface.call_on_all_phone_num(sendMessage)
        return True

    except:
        return False



if __name__ == "__main__":
    mins = 0
    update()

    #Continues to run the script until it is able to update
    while update() != True:
        #Keeps track of each min that passes
        time.sleep(60)
        mins += 1

        #Runs the script again every 5 mins
        if mins % 5 == 0:
            update()
