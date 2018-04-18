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
            "shapes": "",
            "smoking-notes": "",
            "strength": "",
            "productID": "",
            "productURL": ""
        }
cigars = []
#kount = 0

def ProcessCigarItem(cigarItemTag):
    cigar = CigarModel
    #print(cigar)

    name = cigarItemTag.find(itemprop="name").text
    productURL = cigarItemTag.find(itemprop="url").get("content")
    notes = cigarItemTag.find("div", {"class": "listing_descriptions"}).text
    photo = cigarItemTag.find(itemprop="image").get("content")

    try:
        productID = cigarItemTag.find("button", {"class": "pr_ddBtn"}).get("id")
    except:
        productID = ""

    if productID != "":
        productID = productID.replace("btn", "")

    try:
        rating = cigarItemTag.find(itemprop="ratingValue").get("content")
    except:
        rating = 0

    try:
        price = cigarItemTag.find(itemprop="price").get("content")
    except:
        price = 0

    #print(rating)
    #""""
    cigar["name"] = name
    cigar["photos"] = photo
    cigar["notes"] = notes
    cigar["rating"] = rating
    cigar["price"]  = price
    cigar["productID"] = productID
    cigar["productURL"] = productURL
    #print(cigar)
    cigars.append(cigar)
    #"""

def ScrapeWeb(webURL, kount):
    #request = loadweb.LoadWeb(("http://neptune.cigar:7070")
    request = loadweb.LoadWeb(webURL)
    soup = BeautifulSoup(request.content, 'html.parser')

    for prod in soup.findAll("div", {"class": "product_item"}):
        ProcessCigarItem(prod)

    kount = kount + 2
    searchPart = "%s&amp;pg=%s" % (1000, kount)  # (str(1000), str(kount))
    strHref = "https://www.neptunecigar.com/search?text=cigar%20list&amp;nb=" + searchPart
    try:
        ScrapeWeb(strHref, kount)
    except:
        return
   
if __name__ == "__main__":
    """
    try:
        searchPart = "%s&amp;pg=%s" % (40, kount)  # (str(1000), str(kount))
        strHref = "https://www.neptunecigar.com/search?text=cigar%20list&amp;nb=" + searchPart
        ScrapeWeb(strHref, kount)
        except:
            print("Oooh! Some error")
        finally:
            print(cigars)
    """

    # maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        searchPart = "%d&amp;pg=%d" % (12, page)
        url = 'https://www.neptunecigar.com/search?text=cigar%20list&amp;nb=' + searchPart
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
                ProcessCigarItem(prod)

            num_errors = 0

    print(cigars)