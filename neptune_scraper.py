#import loadweb
#import itertools
import datawriter_csv
import paged_html_scraper
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

def ProcessCigarListItem(cigarItemTag):
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

    return cigar


def ProcessCigarsItem(cigarItemTag):
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
        html_attributes = cigarItemTag.find("div", {"class":"parent_single_attrs_toshow"}).text
    except:
        html_attributes = None

    if (html_attributes is not None) and (len(html_attributes) > 0):
        #print("processing html_attributes...")
        attribs = html_attributes.split(',')
        attribs = ["%s" % v.strip() for v in attribs]
        cigar["shapes"] = attribs[0]
        cigar["strength"] = attribs[1]
        cigar["color"] = attribs[2]
        cigar["origin"] = attribs[3].replace("from ", "")
        cigar["html_attributes"] = html_attributes or ""
        #print("end of processing html_attributes...")

    try:
        photo = cigarItemTag.find(itemprop="image").get("content")
    except:
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
        price = 0.0

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

    #cigars.append(cigar)
    return cigar


def CigarList():
    cigars.clear()  # clear the current content
    try:
        cigars = paged_html_scraper.ScrapeWeb('https://www.neptunecigar.com/search?text=cigar list&;', ProcessCigarListItem, 3, -1, "nb=%d&pg=%d")
    except:
        print("Unexpected error encountered while scraping Cigar List")
    else:
        print(cigars)
        try:
            if len(cigars) > 0:
                datawriter_csv.write_to_csv(cigars, ["html_attributes", "filler", "smoking_notes", "binder", "brand", "color", "filler", "html_attributes", "labels", "manufacturer"])
        except (IOError, AttributeError, OSError) as ex:
            print("Unexpected error encountered while writing to the data store. Reason: ")
            print(ex)
        

def Neptune_Cigars():
    try:
        #print("starting to scrape neptune cigars...please wait")
        cigarProds = paged_html_scraper.ScrapeWeb('https://www.neptunecigar.com/cigars?sort=BeS&amp;', ProcessCigarsItem, 3, 24, "nb=%d&amp;pg=%d")
    except (OSError, IOError, AttributeError) as ex:
        print("Unexpected error encountered during the scraping operation.")
        print(ex)
        cigarProds = None
    else:
        #print(cigars)
        try:
            if cigarProds is not None and len(cigarProds) > 0:
                print(cigarProds)
                #datawriter_csv.write_to_csv(cigarProds, ["html_attributes", "filler", "smoking_notes", "binder", "brand", "color", "filler", "html_attributes", "labels", "manufacturer"])
        except (IOError, AttributeError, OSError) as ex:
            print("Unexpected error encountered while writing to the data store. Reason: ")
            print(ex)    

if __name__ == "__main__":
    Neptune_Cigars()