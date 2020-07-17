from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    #update stats and county list 
    states_list = ["1", "2", "3"] #create function that returns list of all states
    counties_list = ["a", "b", "c"] 
    
    #check that list value is correct
    return render_template("index.html", states = states_list, counties = counties_list)

if __name__ == "__main__":
    app.run()

