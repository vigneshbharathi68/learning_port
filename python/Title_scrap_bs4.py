#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Functions: prettify(), requests.get(url).text, 

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Make the request to fetch the ram html content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify()) # print the parsed data of html


# In[ ]:


print(soup.title.text) # List of countries by GDP (nominal) - Wikipedia

for link in soup.find_all("a"):
    print("Inner Text {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))


# In[14]:


# Let's first get all three table headings:
#tr and td refers rows and cells respectively in html

gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr") # Contains 2 rows, first row is title, secound row

# Will get all headings and store it into set form

headings = []

for td in gdp_table_data[0].find_all("td"):
    print(td)
    headings.append(td.b.text.replace('\n', ' ').strip())

print(headings) # ['Per the International Monetary Fund (2019 estimates)',
                # 'Per the World Bank (2019)',
                # 'Per the United Nations (2018)']


# In[12]:


# tr tag has all the table contents so we shoul scrap that and store it into a dictionary

data = {}
for table, heading in zip(gdp_table_data[1].find_all("table"), headings)


# In[ ]:




