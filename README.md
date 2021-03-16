# web-scraping-challenge

# Step 1 - Scraping
Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
- Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of our scraping and analysis tasks. The following outlines what was scraped.

## NASA Mars News
- Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collected the latest News Title and Paragraph Text. Assigned the text to variables that we can reference later.

## JPL Mars Space Images - Featured Image
- Visited the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
- Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.
- Made sure to find the image url to the full size .jpg image.

## Mars Facts
- Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Used Pandas to convert the data to a HTML table string.

## Mars Hemispheres
- Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
- Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys img_url and title.
- Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.


# Step 2 - MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
- Started by converting our Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of our scraping code from above and returned one Python dictionary containing all of the scraped data.
- Next, we created a route called /scrape that will import your scrape_mars.py script and call your scrape function.
- Stored the return value in Mongo as a Python dictionary.
- Created a root route / that will query your Mongo database and passed the mars data into an HTML template to display the data.
- Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
