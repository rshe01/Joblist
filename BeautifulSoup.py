# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:50:12 2021

@author: richa
"""
import requests 
from bs4 import BeautifulSoup

url = "https://www.indeed.com/q-Internship-jobs.html"

#makes get request for the page we are looking at 
page = requests.get(url)

#BS parses the html
soup = BeautifulSoup(page.text, "html.parser")

#displays the text of the parsed page
print(soup.text)