# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:50:12 2021

@author: richa
"""
import requests 
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=Computer+Science+Internship"
info = []
titles = []
locations = []
companies = []
summaries = []

#makes get request for the page we are looking at 
page = requests.get(url)

#BS parses the html
soup = BeautifulSoup(page.content, "html.parser")

elem = soup.find_all("div",class_='jobsearch-SerpJobCard')

def title(elem):
    title_elem = elem.find("h2", class_='title')
    title = title_elem.find("a", class_='jobtitle').text.strip()
    return title

def location(elem):
    rating_location_elem = elem.find('div', class_='sjcl')
    location = rating_location_elem.find("span", class_='location').text.strip()
    return location
    
#rating is funky...
def rating(elem):
    rating_location_elem = elem.find('div', class_='sjcl')
    rating = rating_location_elem.find("span", class_='ratingsContent')
    return rating

def company(elem):
    rating_location_elem = elem.find('div', class_='sjcl')
    company = rating_location_elem.find("span", class_='company').text.strip()
    return company

#does not work since salarySnippet does not exist in the soup. wtf??
def salary(elem):
    salary_elem = elem.find('div', class_='salarySnippet holisticSalary')
    salary = salary_elem.text.strip()
    return salary

def summary(elem):
    summary_elem = elem.find("div", class_='summary')
    summary = summary_elem.text.strip()
    return summary
    
for job_elem in elem:
    titles.append(title(job_elem))
    locations.append(location(job_elem))
    #job_set.append(rating(job_elem))
    companies.append(company(job_elem))
    #job_set.append(salary(job_elem))
    summaries.append(summary(job_elem))
    
info.append(titles)
info.append(locations)
info.append(companies)
info.append(summaries)
print(info)
