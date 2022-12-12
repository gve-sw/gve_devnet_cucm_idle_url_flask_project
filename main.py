""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

# Import Section
from flask import Flask, Response, send_file
import config
from pywttr import Wttr
from datetime import datetime
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.dom import minidom
import feedparser
import ssl

# Global variables
app = Flask(__name__)

@app.route('/text')
def text():

    # query RSS news feed
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    NewsFeed = feedparser.parse(config.rss_feed_link)

    # grab first news entry 
    entry = NewsFeed.entries[1]

    # parse summary of news
    summary = str(entry.summary)
    print(summary)

    # query weather forecast
    wttr = Wttr(config.city)
    forecast = wttr.en()
    forecast = forecast.weather[0]
    
    forecast_string = "AVG: " + str(forecast.avgtemp_c) + " MIN: " + str(forecast.mintemp_c) + " MAX: " + str(forecast.maxtemp_c)
    
    # query the time
    now = datetime.now()
    current_time = "Current Time : " + now.strftime("%H:%M:%S")

    print(current_time)
    print(forecast_string)

    tree = ET.parse('xml_files/text.xml')

    tree.find('Title').text = config.title
    tree.find('Prompt').text = config.motd
    tree.find('Text').text = forecast_string + " " + current_time + "\n" + summary

    tree.write('xml_files/screensaver.xml')

    with open('xml_files/screensaver.xml', 'r') as f:
        data = f.read()

    return Response(data, mimetype='text/xml')

@app.route('/idle')
def idle():

    # query RSS news feed
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    NewsFeed = feedparser.parse(config.rss_feed_link)

    # grab first news entry 
    entry = NewsFeed.entries[1]

    # parse summary of news
    summary = str(entry.summary)
    print(summary)

    # query weather forecast
    wttr = Wttr(config.city)
    forecast = wttr.en()
    forecast = forecast.weather[0]
    
    forecast_string = "AVG: " + str(forecast.avgtemp_c) + " MIN: " + str(forecast.mintemp_c) + " MAX: " + str(forecast.maxtemp_c)
    
    # query the time
    now = datetime.now()
    current_time = "Current Time : " + now.strftime("%H:%M:%S")

    print(current_time)
    print(forecast_string)

    tree = ET.parse('xml_files/image.xml')

    tree.find('Title').text = forecast_string + " " + current_time
    tree.find('Prompt').text = summary

    tree.write('xml_files/image.xml')

    # Reading the data inside the xml file to a variable under the name data
    with open('xml_files/image.xml', 'r') as f:
        data = f.read()

    return Response(data, mimetype='text/xml')

@app.route('/image')
def image():
    # this view is to render the image for the image.xml file
    return send_file('screensavers/logo.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)