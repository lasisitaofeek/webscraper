import loadweb
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
r = 0

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

    if not productID == "":
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

def ScrapeWeb(webURL):
    #r = r + 1
    #print(r)
    #request = loadweb.LoadWeb(("http://neptune.cigar:7070")
    request = loadweb.LoadWeb(webURL)
    soup = BeautifulSoup(request.content, 'html.parser')

    for prod in soup.findAll("div", {"class": "product_item"}):
        ProcessCigarItem(prod)

#"""
    #TO DO
    
    #print("Ready for NEXT!")
    for nextPage in soup.findAll("a", {"class": "pagination_buttons"})[-1].parent:
        #print(nextPage.get("href"))
        if not nextPage == None:
            print(nextPage.get("href"))
            ScrapeWeb("https://www.neptunecigar.com" + nextPage.get("href"))
        else:
            return ""

        """
         if r==3:
            print("got here!")
            
            print(cigars)
            exit
        """
        #print(nextPage.get("href"))
#""" 


if __name__ == "__main__":
    #("http://neptune.cigar:7070")
    ScrapeWeb("https://www.neptunecigar.com/deals/spring-2018-sampler-sale")
    print(cigars)