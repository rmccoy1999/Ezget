import urllib.request as urllib2
from bs4 import *
import validators
import urllib
from urllib.parse  import urljoin
import urllib.parse as up
import time
import threading
import sys

# will need to do pip install bs4 to use imported modules 
# https://docs.python.org/2/library/urllib2.html
# Beautifulsoup saves links in plain text

def checker(website):
  covid_screener = urllib2.urlopen(website)
  if covid_screener.code == 200:
    print ("The Matrix has you... Quantifying Metacortex Initialization Phase.... ")
  else:
    print ("Error 503, blue pill ends the story")
  '''a = 'https://www.'
  b = '.com'
  if ((website[0:11] != a):
    #replace or add string a to beginning of website
  elif(website[-3:] != b):
    #replace or add string b to end of website
  valid=validators.url(website)
  if valid==True:
    print("URL is valid")
    #crawlin(website, depth=1)
  else:
    print("URL is not valid. Try again.");
    website = input('Enter your website url here: ')
    checker(website);
'''
  web_array = [website]  
  urls = crawlin(web_array, depth=3)
  print(urls)

def crawlin(pages, depth=None):
    url_void = []               # creates list for storing crawled through html websites
    for i in range(depth):  # used to set how many layers of urls to append to list
        for page in pages: # used to set how many sub layers of urls to append to list
            if page not in url_void:
                url_void.append(page) # adds new url to list if not added already
                try:
                    site = urllib2.urlopen(page) # attempts to open url, storing it as site
                except:
                    print (page % "%s, ain't able to open bruh") # acts as throwing exception
                    continue
                soup = BeautifulSoup(site.read(), "html.parser") # reads contents of webpage, storing it in the main class of soup
                Tree = soup('a')          # after reading, it finds the sub-links to store

                for Branch in Tree:
                    if 'href' in dict(Branch.attrs):          # H(yper)link Ref(erence) in dictionary
                        url = urljoin(page, Branch['href'])   # parses base url with another anchored webpage
                        if url.find("'") != -1:           # fetches last string
                                continue
                        url = url.split('#')[0]         # gets filename of url keeping its parameters
                        if url[0:4] == 'http':              # seperates "real" urls from garbage
                                url_void.append(url)     # adds to url list
        pages = url_void
    return url_void


#website='https://www.google.com'
#urls = crawlin(website, depth=1)
#print(urls)
# Your foo function

'''def countdown():
  print('Working1')
  nuke = 5
  start_time = time.time()
  while(start_time > nuke):
    website = input('Enter your website url here: ')
  else:
    end_time = time.time()
    print("\nBOOOM. The nuke exploded. Bye bye.")
    sys.exit()
  return website, end_time'''
    
def prompt():
    print("Working2")
    print("Welcome to Ezget.")
    website = input('Enter your website url here: ')
    global input_tick
    input_tick = 'True'
    #print("success")
    #return input_tick
    checker(website)


if __name__ == '__main__':
  input_tick = 'False'
  count = threading.Thread(target=prompt)
  #site = Thread(target = prompt).start()
  count.daemon == True
  count.start()
  time.sleep(3)
  if (input_tick == 'False'):
    print("\nBOOOM. The nuke exploded. Bye bye.")
    sys.exit()
    
  


  