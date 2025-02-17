from requests_html import HTML, HTMLSession

# Nike SNKRS Lauch Calendar
NIKE_SNKRS_URL = 'https://heat-mvmnt.de/releases'
# Create requests-html session Object
s = HTMLSession() 
# Create response for Nike SNKRS Launch
r = s.get(NIKE_SNKRS_URL) 
# Contains the HTML 
html_of_site = r.html 

# Functions 
def get_nike_shoes(html_of_site=html_of_site): 
    '''Return the first ten shoes in the launch calendar.''' 
    select = "div[class='mb-5 sm:mb-2']"  # Selector to scrape
    shoes_and_releases = html_of_site.find(select)  # Gets the css elements
    list_of_shoes = []  # Contains the shoes and its release

    for shoe_and_release in shoes_and_releases: 
        list_of_shoes.append(shoe_and_release.text)

    return list_of_shoes[0:10]

def get_links(html_of_site=html_of_site): 
    '''Return the first ten links for the shoes in the launch calendar.'''
    select = "a[class^='mb sm mb']"  # Selector to scrape
    links_for_shoes = html_of_site.find(select)  # Gets the css elements
    list_of_links = []  # Contains the links for the shoes

    for link in links_for_shoes: 
        list_of_links.append(list(link.absolute_links)[0])
    
    return list_of_links[0:10] 
