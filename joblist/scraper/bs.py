import requests 
from bs4 import BeautifulSoup
import re

def bs(url):
    url = url
    
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
        if rating_location_elem.find("span", class_='location') is None:
            return "N/A"
        else:
            return rating_location_elem.find("span", class_='location').text.strip()

    def company(elem):
        rating_location_elem = elem.find('div', class_='sjcl')
        company = rating_location_elem.find("span", class_='company').text.strip()
        return company

    def summary(elem):
        summary_elem = elem.find("div", class_='summary')
        summary = summary_elem.text.strip()
        return summary
        
    def date(elem):
        date_elem = elem.find("div", class_='jobsearch-SerpJobCard-footer')
        date = date_elem.find("span", class_="date")
        num = int(re.search(r'\d+', date.text.strip()).group())
        return num
    
    temp=[]
    desired_locations = ['VA', 'Virginia', "Remote", "DC"]
    for job_elem in elem:
        temp2=[]
        if(date(job_elem)<30):
            for i in desired_locations:
                if(i in location(job_elem)):
                    temp2.append(title(job_elem))
                    temp2.append(job_elem.get("data-jk"))
                    temp2.append(location(job_elem))
                    temp2.append(company(job_elem))
                    temp2.append(summary(job_elem))
                    temp.append(temp2)
    return temp