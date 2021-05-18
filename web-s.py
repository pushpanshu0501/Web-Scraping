from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver") #Set the path to chromedriver

names=[] #List to store name of the product 
organisation=[] #List to store price of the product 
projectName=[] #List to store rating of the product 
driver.get("https://summerofcode.withgoogle.com/projects/")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")
all_projects = soup.findAll('a',href=True, attrs={'class':'funded-projects-list'})

for laptop in all_projects:
    name=laptop.find('div', attrs={'class':'pos-rel'})
    organisationName=laptop.find('div', attrs={'class':'md-soc-theme'})
    project=laptop.find('div', attrs={'class':'md-soc-theme'})
    names.append(name.text.strip())
    # print(name+"  "+organisationName+"  "+project)
    organisation.append(organisationName.text.strip())
    projectName.append(project.text.strip()) 

df = pd.DataFrame({'Student Name':names,'Organisation':organisation,'Project Name':projectName}) 
df.to_csv('laptop_details.csv', index=False, encoding='utf-8')
