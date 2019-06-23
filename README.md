# philosophy_wikipedia

## Overview 
The program should receive a Wikipedia link as an input, go to another normal link and repeat this process until either Philosophy page is reached, or we are in an article without any outgoing Wikilinks, or stuck in a loop.

## Prerequisites
* [Python 3.x](https://www.python.org/downloads)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://2.python-requests.org/en/master/)

## Usage 
To run the program with default settings on
```bash 
cd ../philosophy_wikipedia
py -3 wikipedia.py
```
### Optional parameters
| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -m 	       |	100           |The maximum number of pages it should look up before exit
| -u          | https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy           | The starting link, where the code will start it's search 


## Example
```bash
User ../philosophy_wikipedia> py -3 wikipedia.py -m 10
Wikipedia:Getting to Philosophy
Hannah Fry
Phenomenon
The Guardian
Language
Attractor
Node.js
Xkcd
Philosophy
```
