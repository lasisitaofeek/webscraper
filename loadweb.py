import requests
from bs4 import BeautifulSoup

def LoadWeb(WebUrl):
    """ This loads the HTML doc of the website url submitted.
        It accepts one parameter -- the URL
    """
    user_agent = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    request = requests.get(WebUrl, headers = user_agent)
    return request

if __name__ == "__main__":
    """ This is to Unit Test, if the module is used in another module
        this If-block will be ignored
    """
    request = LoadWeb("http://softpro.new:7070")
    soup = BeautifulSoup(request.content, 'html.parser')
    #print(soup)
    for link in soup.find_all("a"):
        print(link.get("ui-sref") or link.get("href") or link.text)
