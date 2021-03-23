# dependecies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# set up Flask
app = Flask(__name__)

# set up Mongo 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# set up root route 
@app.route("/")
def root():

    # Return template and data
    return render_template("index.html")

# set up scrape route
@app.route("/scrape")
def scrape():

    # set up Mongo Mars data
    mars_info = mongo.db.mars_info

    # save scrape function as variable
    mars_data = scrape_mars.scrape()

    # update Mongo Mars data
    mars_info.update({}, mars_data, upsert=True)

    # redirect to root
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)