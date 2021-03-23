# dependecies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# set up Flask
app = Flask(__name__)

# set up Mongo and Mars data
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mars_data = mongo.db.mars_data

# set up root route 
@app.route("/")
def root():

    return render_template("index.html")

# set up scrape route
@app.route("/scrape")
def scrape():

    # save scrape function as variable
    mars_dict = scrape_mars.scrape()

    # update Mongo Mars data
    mars_data.update({}, mars_dict, upsert=True)

    # redirect to root
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)