import urllib.request as urllib2
from bs4 import *
import validators
import urllib
from urllib.parse  import urljoin
from urllib.parse import urlparse
import urllib.parse as up
import time
import threading
import sys
import requests

# will need to do pip install bs4 to use imported modules 
# https://docs.python.org/2/library/urllib2.html
# Beautifulsoup saves links in plain text

def String_checker(website):
  '''
    if (website[0:7] != 'https://'):
    print('You need to add "https://" to the beginning')
    return False
  elif((website[-4:]) != ('.com/' or '.org/')):
    print('You are missing the ".whatever" at the end")
    return False
  else:
    return True
    '''
  try:
      result = urlparse(website)
      return all([result.scheme, result.netloc, result.path])
  except:
      return False

def HTML_checker(website: str) -> bool:
    try:
      with requests.get(website, stream=True) as response:
        try:
          response.raise_for_status()
          return True
        except requests.exceptions.HTTPError:
          return False
    except requests.exceptions.ConnectionError:
        return False

def crawlin(pages, depth):
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

print("Welcome to Ezget.")
website = input('Enter your website url here: ')

while((String_checker(website) is not True) or (HTML_checker(website) is not True)):
  print('your website is not correct.')
  website = input('Try again. Enter your website url here: ')

tries = 0
onions_have_layers = input('Enter your depth: ')
while((not int(onions_have_layers.isdigit())) or (int(onions_have_layers) > 1000)):
  tries += 1
  if (not int(onions_have_layers.isdigit())):
    print("I'm no mathmatician but that ain't a numba g")
    if(tries > 1):
      onions_have_layers = input('Sigh... Try again. Enter your depth: ')
    else:
      onions_have_layers = input('Enter your depth: ')
    onions_have_layers = input('Try again. Enter your depth: ')
  elif int(onions_have_layers) > 1000:
    print("You're not downloading the entire internet are ya. Needs to be less then 1000")
    if(tries > 1):
      onions_have_layers = input('Sigh... Try again. Enter your depth: ')
    else:
      onions_have_layers = input('Enter your depth: ')

print(onions_have_layers)
if((String_checker(website) is True) and (HTML_checker(website) is True)):
  print ("The Matrix has you... Quantifying Metacortex Initialization Phase.... ")
  time.sleep(2)
  web_array = [website]
  urls = crawlin(web_array, int(onions_have_layers))
  print(urls)
else:
  print ('Error 502, blue pill ends the story')



    
  

  

