from flask import Flask, redirect, url_for
from flask import render_template
import data_processing
app = Flask(__name__)

@app.route("/")
def home():
    #update stats and county list 
    states_list = ["10, me", "2,w e", "3"] #create function that returns list of all states
    counties_list = data_processing.listcounties()
    #check that list value is correct
    return render_template("index.html", states = states_list, counties = counties_list)

if __name__ == "__main__":
    app.run()

