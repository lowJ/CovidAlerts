from flask import Flask, redirect, url_for
from flask import render_template, request
import db_interface
import data_processing
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        phone_num = request.form["phone_num"]
        county_get = request.form["county"]

        if(0):#county invalid):
            usr_msg = county_get + " is an invalid county"
            return render_template("success.html", msg = usr_msg)
        if(0):#phone num invalid):
            return render_template("success.html", msg = "invalid phone number")
        if(0):#phon num and county combo exists):
            usr_msg = "you are already registered to recieve covid-19 alerts for" + county_get
            return render_template("success.html", msg = usr_msg)
        else:
            usr_msg = "successfully signed up " + phone_num + " do recieve alerts for " +  county_get
            #double check filtering before calling .add_user
            db_interface.add_user(phone_num, "rm state col", county_get)
            return render_template("success.html", msg = usr_msg)

    else:
        states_list = ["10, me", "2,w e", "3"] 
        counties_list = data_processing.listcounties()
        #figure out how to list counties in the format "Los Angles (CA)"
        return render_template("index.html", states = states_list, counties = counties_list)

if __name__ == "__main__":
    app.run()

