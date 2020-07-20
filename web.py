from flask import Flask, redirect, url_for
from flask import render_template, request
import data_processing
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():

    if(request.method == "POST"):
        phone_num = request.form["phone_num"]
        county_get = request.form["county"]
        #return redirect(url_for("succ", phone=phone_num, county=county_get))
        #Add Check user info to see if everything is valid
        #If something not valid, ask to re enter info

        #Else:
            #ad info to db
            #redirect to success page

    else:
        #update stats and county list 
        states_list = ["10, me", "2,w e", "3"] #create function that returns list of all states
        counties_list = data_processing.listcounties()
        #check that list value is correct
        return render_template("index.html", states = states_list, counties = counties_list)

# @app.route("/<succ>")
# def succ(phone, county):
#     return f"<h1>{phone}{county}</h1>"


if __name__ == "__main__":
    app.run()

