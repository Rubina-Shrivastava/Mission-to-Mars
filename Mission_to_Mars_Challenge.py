#!/usr/bin/env python
# coding: utf-8




# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the NASA Mars News Site


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)



# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


slide_elem.find("div", class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars','Earth']
df.set_index('description', inplace=True)
df

df.to_html()

# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# Deleverie 1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
  
#Empty list
hemisphere_image_urls = []

#Cerberus
browser.visit(url)
browser.links.find_by_partial_text('Cerberus').click()
html = browser.html
cerberus_soup = soup(html, 'html.parser')
cerberus_url = cerberus_soup.select_one('div.downloads a').get("href")
cerberus_title = cerberus_soup.select_one('div.content h2').text

#dictionary:
cerberus_dict = {
        "img_url": cerberus_url,
        "title": cerberus_title
    }

hemisphere_image_urls.append(cerberus_dict)

#Schiaparelli
browser.visit(url)
browser.links.find_by_partial_text('Schiaparelli').click()
html = browser.html
schiaparelli_soup = soup(html, 'html.parser')
schiaparelli_url = schiaparelli_soup.select_one('div.downloads a').get("href")
schiaparelli_title = schiaparelli_soup.select_one('div.content h2').text

#dictionary:
schiaparelli_dict = {
        "img_url": schiaparelli_url,
        "title": schiaparelli_title
    }

hemisphere_image_urls.append(schiaparelli_dict)

#Syrtis
browser.visit(url)
browser.links.find_by_partial_text('Syrtis').click()
html = browser.html
syrtis_soup = soup(html, 'html.parser')
syrtis_url = syrtis_soup.select_one('div.downloads a').get("href")
syrtis_title = syrtis_soup.select_one('div.content h2').text

#dictionary:
syrtis_dict = {
        "img_url": syrtis_url,
        "title": syrtis_title
    }

hemisphere_image_urls.append(syrtis_dict)


#Valles
browser.visit(url)
browser.links.find_by_partial_text('Valles').click()
html = browser.html
valles_soup = soup(html, 'html.parser')
valles_url = valles_soup.select_one('div.downloads a').get("href")
valles_title = valles_soup.select_one('div.content h2').text

#dictionary:
valles_dict = {
        "img_url": valles_url,
        "title": valles_title
    }

hemisphere_image_urls.append(valles_dict)


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()





