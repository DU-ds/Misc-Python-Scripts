# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:37:14 2018

@author: Kenneth Collins
"""


"""
based upon:		
file:///R:/Git/VAM-Python/VAM.html

from this git repository:
https://github.com/rjweiss/VAM-Python
"""

#%%
from IPython.display import HTML
import requests as R

presidency_platforms_url = 'http://www.presidency.ucsb.edu/platforms.php'
HTML("<iframe src=" + presidency_platforms_url + " width=100% height=400px></iframe>")
#print("<iframe src=" + presidency_platforms_url + " width=100% height=400px></iframe>")

req = R.get(presidency_platforms_url)
print(type(req.status_code))
print ("Server response status code = " + str(req.status_code))

"""
If you write a script to automate scraping, check for status code = 200. Otherwise, you might get junk data!
"""
#%%
import pprint
print(req.encoding)
headers = req.headers
pprint.pprint(headers.items() )

"""
FYI, the server sees a lot of information from you as well !
"""

r = R.get('http://httpbin.org/user-agent') # Website that allows you to test for HTTP behaviors
r.text 
r = R.get("http://httpbin.org/ip")
print(r.content())
print(r.json())
import json
print(r.json()['origin'])

"""
http://validator.w3.org/
"""

#%%

from bs4 import BeautifulSoup as bs
r = R.get(presidency_platforms_url)
soup = bs(r.text)
print(type(soup))
print(soup.prettify()[0:1000]) #html from the url
print(soup.title)
print(soup.meta)
print(soup.a)
print(soup.p)
"""
references: 
    https://www.w3.org/DOM/
    https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model

"""
#%%
"""
extract every link URL on the page.
"""
allLinks = []
for i in soup.findAll("a"):
    allLinks.append(i.get("href"))
print("All link hrefs in a list from a for loop: " + str(len(allLinks)))
#more like the number of link hrefs, right?
all_links_comprehension = [i.get('href') for i in soup.findAll('a')]

print('All link hrefs in a list from a list comprehension: ' + str(len(all_links_comprehension)))

"""
BeautifulSoup has a .get_text() method that extracts the text attribute from every tag.
"""

print(soup.get_text()[0:5000])

allLinks[:]

#%%

"""
This next part gave me trouble. I think the tutorial is in python 2, not 3.
https://docs.python.org/3/library/stdtypes.html#str.split
https://docs.python.org/3/library/string.html
"""

valid_links = []
for link in allLinks:
    final_url_element = str(link).split(sep = "/")[-1] #[-1] indexes the last element
    if str(final_url_element).startswith('index.php'):
        valid_links.append(link)
print('There are {} valid links.'.format(len(valid_links)))


from datetime import datetime # Another standard library module.
for link in valid_links[:10]: # Limited for demonstration.  Also check out import time; time.sleep()
    r = R.get(link)

print('{time}\t{link}\t{status}'.format(time=datetime.isoformat(datetime.now()), link=link, status=r.status_code))


"""
However, that previous example will print to stdout (that's what print() does).

If you execute this as a script at the command line, 
it would be better to have this write to a file, 
so let's open up a text file and write the output to that:
"""
#%%
import os
os.chdir("R:/Git/VAM-Python/Practice1")
file = open('practicepresidency_platforms_scraping.log', 'w' )
print(type(file))
file.write('Timestamp\tURL\tStatus Code\n')

for link in validLinks[:]:
    r = R.get(link)
    R_event_string = '{time}\t{link}\t{status}\n'.format(time=datetime.isoformat(datetime.now()), link=link, status=r.status_code)
    file.write(R_event_string)
    
file.close()

os.listdir(os.getcwd())

#writes code to a bash console
%%bash
cd R:/Git/VAM-Python/Practice1
head presidency_platforms_scraping.log




 #%%   
"""
Some ideas of what I want to practice scraping another time:
https://www.gutenberg.org/ebooks/search/?query=voltaire
https://www.gutenberg.org/ebooks/search/?query=voltaire+cat.audio
https://www.gutenberg.org/ebooks/search/?query=cat.audio+l.english&start_index=101
https://www.gutenberg.org/ebooks/26228
https://www.gutenberg.org/ebooks/20594
https://www.gutenberg.org/ebooks/6556
https://www.gutenberg.org/ebooks/19505
"""
 









