import loadweb
import itertools
from bs4 import BeautifulSoup

#import UserDict

CigarModel = {
            "binder":"",
            "brand":"",
            "color":"",
            "filler":"",
            "html_attributes":"",
            "labels": "",
            "manufacturer": "",
            "name": "",
            "notes": "",
            "origin": "",
            "photos" : "",
            "price": 0.00,
            "profile": "",
            "rating": 0.0,
            "ratingCount": 0,
            "shapes": "",
            "smoking-notes": "",
            "strength": "",
            "productID": "",
            "productURL": ""
        }
cigars = []
#kount = 0

def ProcessCigarSamplerItem(cigarItemTag):
    cigar = CigarModel
    try:
        name = cigarItemTag.find(itemprop="name").text
    except:
        name = ""

    try:
        productURL = cigarItemTag.find(itemprop="url").get("content")
    except:
        productURL = ""
    
    try:
        notes = cigarItemTag.find("div", {"class": "listing_descriptions"}).text
    except:
        notes = ""

    try:
        photo = cigarItemTag.find(itemprop="image").get("content")
    except expression as identifier:
        photo = ""
    
    try:
        productID = cigarItemTag.find("button", {"class": "pr_ddBtn"}).get("id")
    except:
        productID = ""

    if productID != "":
        productID = productID.replace("btn", "")

    try:
        rating = cigarItemTag.find(itemprop="ratingValue").get("content")
    except:
        rating = 0.0

    try:
        ratingCount = cigarItemTag.find(itemprop="ratingCount").get("content")
    except:
        ratingCount = 0.0
    
    try:
        price = cigarItemTag.find(itemprop="price").get("content")
    except:
        price = 0.00

    cigar["name"] = name
    cigar["photos"] = photo
    cigar["notes"] = notes
    cigar["rating"] = rating
    cigar["ratingCount"] = ratingCount  #number of raters
    cigar["price"]  = price
    cigar["productID"] = productID  
    cigar["productURL"] = productURL

    # you should comment out the following line in production releasse
    # print(cigar)

    cigars.append(cigar)
    #"""

"""
    ScrapeWeb(url, max_errors=3)
    url - the base paging URL, without the querystring for pageSize and page
    
    max_errors - maximum number of consecutive download errors allowed
    call_back - a function to parse a specific page (e.g. ProcessCigarSamplerItem above that parses the cigar sampler page)
                with this, we can now scrape other pages filtered by manufacturer, origin, price, etc.
"""
def ScrapeWeb(baseUrl, call_back=ProcessCigarSamplerItem, max_errors=3):
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        searchPart = "nb=%d&pg=%d" % (48, page)
        url = baseUrl + searchPart
        html = loadweb.LoadWeb(url)
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum number of
                # consecutive errors so exit
                break
        else:
            # success - can scrape the result
            # ...
            soup = BeautifulSoup(html.content, 'html.parser')
            for prod in soup.findAll("div", {"class": "product_item"}):
                #ProcessCigarSamplerItem(prod)
                call_back(prod)

            num_errors = 0
        
        # to quickly return for a test scenario
        # please, enable the comment for production
        #"""
        if page == 20:
            break
        #"""
   
if __name__ == "__main__":
    #TO DO: Convert the list to a JSON doc, instead of print as the code below does
    try:
        ScrapeWeb('https://www.neptunecigar.com/search?text=cigar list&;', ProcessCigarSamplerItem, 3)
    except:
        pass

    print(cigars)