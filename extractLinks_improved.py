import requests
import re
from bs4 import BeautifulSoup               # install BeautifulSoup if required

url = input()
while not re.search("^(https?://)(www\.)?([a-zA-Z0-9_-])+(\.([a-zA-Z0-9_])+)+([a-zA-Z0-9_/])+$" , url) :   #if Invalid url
    url = input("Enter a valid Url")

def extract_social_links(url):
    try:
        page = requests.get(url)
    except:
        return {'Error', 'The Request could not be processed, please try again'}
    soup = BeautifulSoup(page.content, "lxml")      #parsing the html page by passing it into the BeautifulSoup constructor
    all_links = soup.find_all('a', href = True)     #find all anchor tags having href
    social_links = {}
    social_sites = ['twitter.com', 'linkedin.com', 'facebook.com', 'youtube.com', 'instagram.com']  #list of social sites
    for link in all_links:
        if len(social_links) == len(social_sites):  #if all links grabbed, break
            break
        href = link['href']
        for social_site in social_sites:
            if (social_site.lower() + '/') in (href.lower()):
                social_links[social_site] = link['href']

    return social_links

print(extract_social_links(url))
