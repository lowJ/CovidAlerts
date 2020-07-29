from flask import Flask, redirect, url_for
from flask import render_template, request
from phoneCheck import checkNumber, formatNumber
from countyCheck import checkCounty
import db_interface
import data_processing
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        phone_num = request.form["phone_num"]
        county_get = request.form["county"]

        #check if phone number is valid
        phone_is_valid = checkNumber(phone_num)
        if phone_is_valid:
            phone_num = formatNumber(phone_num)

        #check if county is valid
        county_get = checkCounty(county_get)
        if type(county_get) is str:
            county_is_valid = False
        else:
            county_is_valid = True
            county, state = county_get

        if(not county_is_valid):#county invalid):
            usr_msg = county_get
            return render_template("success.html", msg = usr_msg)
        if(not phone_is_valid):#phone num invalid):
            return render_template("success.html", msg = "Invalid phone number.")
        if(0):#phon num and county combo exists):
            usr_msg = "you are already registered to recieve covid-19 alerts for" + county_get
            return render_template("success.html", msg = usr_msg)
        else:
            usr_msg = "Successfully signed up " + phone_num + " to recieve alerts for " +  county_get[0] + ", " + county_get[1]
            #double check filtering before calling .add_user
            db_interface.add_user(phone_num, county_get[1], county_get[0])
            return render_template("success.html", msg = usr_msg)

    else:
        states_list = ["10, me", "2,w e", "3"] 
        counties_list = data_processing.listcounties()
        #figure out how to list counties in the format "Los Angles (CA)"
        return render_template("index.html", states = states_list, counties = counties_list)

if __name__ == "__main__":
    app.run()

