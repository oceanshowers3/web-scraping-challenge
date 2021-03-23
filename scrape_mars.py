# dependencies
import pandas as pd
from pprint import pprint 
import time
import requests as req
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 

# set up browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
    time.sleep(5) # sleep before next task 

# ---------------------------------------------------------------------------------------------

# Scraping

# ---------------------------------------------------------------------------------------------

# define function to scrape everything 
def scrape():
    browser = init_browser()

    # ---------------------------------------------------------------------------------------------

    # NASA Mars News

    # ---------------------------------------------------------------------------------------------

    # set up url for NASA news site, browser, and html
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(2) # sleep before next task 
    news_html = browser.html

    # parse with BeautifulSoup
    news_soup = bs(news_html, 'html.parser')

    # find the latest news article
    latest_article = news_soup.find('li', class_='slide')

    # find the latest news article title
    article_title = latest_article.find('div', class_='content_title').find('a').text

    # find the latest news article paragraph text
    article_p = latest_article.find('div', class_='article_teaser_body').text

    # print the title and the paragraph text
    print(article_title)
    print(article_p)

    # ---------------------------------------------------------------------------------------------

    # JPL Mars Space Images - Featured Image

    # ---------------------------------------------------------------------------------------------

    # set up url for JPL Featured Mars Image, browser, and html
    image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(image_url)
    time.sleep(2) # sleep before next task 
    image_html = browser.html

    # go to 'FULL IMAGE', set the new browser link, and html
    browser.links.find_by_partial_text('FULL IMAGE').first.click()
    time.sleep(2) # sleep before next task 
    full_image_html = browser.html

    # parse with BeautifulSoup
    image_soup = bs(full_image_html, 'html.parser')

    # scrape the URL
    feature_url = image_soup.find('img', class_='fancybox-image')['src']

    # print the url for the full image version of the Featured Mars Image
    base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    featured_image_url = f'{base_url}{feature_url}'
    print(featured_image_url)

    # ---------------------------------------------------------------------------------------------

    # Mars Facts

    # ---------------------------------------------------------------------------------------------

    # set up url for Mars Facts and browser
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(2) # sleep before next task 

    # use Pandas to parse facts url to find all tables
    facts_table_list = pd.read_html(facts_url)

    # select the correct table from the list of tables
    facts_table = facts_table_list[0]

    # rename the columns with appropriate headings
    facts_table.columns = ['Variable', 'Value']

    # convert the data to an HTML string
    facts_string = facts_table.to_html(index=False)
    print(facts_string)

    # ---------------------------------------------------------------------------------------------

    # Mars Hemispheres

    # ---------------------------------------------------------------------------------------------

    # set up url for USGS Astrogeology, browser, and html
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(2) # sleep before next task
    html_hemispheres = browser.html

    # set up base url
    hemispheres_base_url = 'https://astrogeology.usgs.gov'

    # parse with BeautifulSoup
    hemispheres_soup = bs(html_hemispheres, 'html.parser')

    # retrieve the all items (contains all info for hemispheres)
    hemispheres_items = hemispheres_soup.find_all('div', class_='item')

    # empty list for titles and image urls
    hemispheres_data = []

    # loop through items containing all the hemispheres' info
    for item in hemispheres_items: 
        
        # find and store titles
        title = item.find('h3').text
        
        # find link that leads to full res image
        hemispheres_full = item.find('a', class_='itemLink product-item')['href']
        
        # navigate to site containing full res image
        browser.visit(hemispheres_base_url + hemispheres_full)
        time.sleep(2) # sleep before next task 
        
        # save the html of site containing each hemisphere's full res image
        full_res_url = browser.html
        
        # parse each hemisphere's html with BeautifulSoup
        hemispheres_soup = bs(full_res_url, 'html.parser')
        
        # save the path to full res image
        full_res_path = hemispheres_soup.find('img', class_='wide-image')['src']
        
        # save the url to the full res image 
        img_url = f'{hemispheres_base_url}{full_res_path}'
        
        # append title and full res image url to hemispheres dictionary
        hemispheres_data.append({'Title' : title, 'Link to article' : img_url})  
        
    # print the hemispheres dictionary
    print(hemispheres_data)

    # ---------------------------------------------------------------------------------------------

    # close the browser
    browser.quit()

    # ---------------------------------------------------------------------------------------------

    # create a dictionary to store everything scraped

    # ---------------------------------------------------------------------------------------------

    mars_info = {
        'article_title': article_title,
        'article_p': article_p,
        'featured_image_url': featured_image_url,
        'facts_tables': facts_string, 
        'hemispheres_data': hemispheres_data
    }

    # --- Return results ---
    return mars_info



