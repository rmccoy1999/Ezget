import urllib.request as urllib2
from bs4 import *
from urllib.parse  import urljoin

# will need to do pip install bs4 to use imported modules 
# https://docs.python.org/2/library/urllib2.html
# Beautifulsoup saves links in plain text

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


website=["https://google.com"]
urls = crawlin(website, depth=1)
print(urls)