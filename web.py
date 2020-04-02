from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd



my_url = 'https://summerofcode.withgoogle.com/archive/2019/projects/'

uClient = uReq(my_url)
page_html = uClient.read()
#print(page_html)
uClient.close()
page_soup = soup(page_html,"html.parser")

names=[] #List to store name of the person
organisation=[] #List to store organisation name
projects=[] #List to store name of the project


for a in page_soup.findAll('a',href=True, attrs={'class':'md-padding archive-project-card__header archive-project-card__header--mod-0'}):
    name=soup.find_all('h4', attrs={'class':'archive-project-card__student-name'})
    organisation=a.find_all('div', attrs={'class':'None'})
    project=a.find_all('div', attrs={'class':'None'})
    names.append(name.text)
    organisation.append(organisation.text)
    projects.append(project.text) 
    
df = pd.DataFrame({'Name':names,'Organisation':organisation,'Projects':projects})
df.to_csv('products.csv', index=False, encoding='utf-8') 