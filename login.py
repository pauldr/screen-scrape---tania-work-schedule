# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
url = 'https://webscheduler.ucsd.edu/signin.do'

page = urllib2.urlopen(url)
print(page)
