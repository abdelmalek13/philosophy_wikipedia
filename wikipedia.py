import bs4, requests, re, time,sys
from argparse import ArgumentParser

def getInput(starter_url):
    '''
    responsible for stripping input from so it fits the rest of the code
    Input: url , the url of the starting wikipedia page
    output: url, the same url after removing "wikipedia.org"
    and only keep the rest
    '''
    url = starter_url.split("wikipedia.org/")[-1]
    return url

def fetchPage(url):
    '''
    Get the page after adding the english wikipedia domain
    Input: url, the url of the page
    Output: response object containing the content, ok and header info
    '''
    response = requests.get("https://en.wikipedia.org/"+url)
    time.sleep(1)
    response.raise_for_status()
    return response

def crawlPage(response):
    '''
    search and extract the contents of the page for links
    Input: response, responce object containing content,ok, and header of the page
    Output: False, in case there's no content
            links, the links whithin the page
    '''
    html_content = bs4.BeautifulSoup(response.text,'lxml')
    soup = html_content.select(".mw-content-ltr")
    if not checkContent(soup):
        return False
    links = {x.get('href') for x in soup[0].findAll('a',attrs={'href':re.compile("/wiki/|/w/")})}
    links=list(filter(lambda x: removeUnwanted(x), links))
    if checkLinks(links):
        return links


def removeUnwanted(link):
    '''
    Remove the unwanted pages like help, files etc
    Input: link, the link of the page
    Output: the links that don't contain any stop_strings
    '''
    stop_strings=["Wikipedia:","#","User:","Help:","File:",'index.php',"Template_talk:","Template:"]
    return all([x not in link for x in stop_strings])

def checkContent(soup):
    '''
    Check if there is content or not
    Input: soup, BeautifulSoup object that contains the html content
    Output: True, if there is content
    '''
    if soup:
        return True

def checkLinks(links):
    '''
    Check if there are links or not
    Input: links, the links inside one page
    Output: True, if there are links
    '''
    if len(links) !=0:
        return True

def checkTarget(page):
    '''
    Check if the goal was reached
    Input: the page we read
    Output: True, if this page was "Philosophy"
    '''
    if 'Philosophy' == page.split('/')[-1]:
        return True

# def Found(flag):
#     '''
#
#     '''
#     if not flag :
#         printPage("not found")

def printPage(page):
    '''
    Format the name of the page and print it
    Input: page, the page link
    '''
    if page:
        name = page.split('/')[-1]
        print(' '.join(name.split('_')))

if __name__ == "__main__":

    ## initiating argparse variables (default variables)
    starter_url = "https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy"
    max_pages = 100

    ## Argparse section
    parser = ArgumentParser()
    parser.add_argument('-u','--url',action='store',type=str,help='Choose\
     the starting wikipedia url(the default ishttps://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy)')
    parser.add_argument('-m','--pages', action='store',type=int,help="Select\
     the number of maximum number of pages the code shoul access before stopping(the default is 100)")

    args = parser.parse_args()
    if args.url: #if the user entered an url, then store it
        starter_url = args.url
    if args.pages:#if the user entered max. number of pages, then store it
        max_pages = args.pages

    url=getInput(starter_url)
    unvisited_pages = set([url,])   #add the starter_url to the unvisited pages set
    visited_pages = set()
    count = 0
    while len(unvisited_pages) != 0 and count != max_pages:
        for site in unvisited_pages :

            res = fetchPage(site)
            pages = crawlPage(res)
            if pages :
                visited_pages.update([site,])
                printPage(site)
                if checkTarget(site):
                    sys.exit()

            count += 1
            if count == max_pages:
                break

        unvisited_pages = set(pages) - visited_pages

    print("Not Found") #if the code reached that far then it wasn't found 
