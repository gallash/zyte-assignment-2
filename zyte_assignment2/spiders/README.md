# Zyte-Assignment-2

Spider with JavaScript

Developed by Phillip Gallas, as a coding challenge for Zyte (formerly known as ScrapingHub).
This spider project renders in HTML the dynamically created page in JavaScript and scrapes it for the information on the quotes' authors, tags and the quotes themselves spread in the page.

This spider was written based on the excellent documentation for the products provided by Zyte itself.

## Pre-requisites
### Installation of pre-requisites
In order for the spider to work with the heavily JavaScripted page, the following modules are necessary.

Firstly, install the scrapy module by executing:
```sh
$ pip3 install scrapy
```
We also need to install Splash, the headless browser that will take care of executing the JavaScript in the webpage. For that, make sure to have docker already installed on your machine. Pulling the Splash image
```sh
$ sudo docker pull scrapinghub/splash
```
And then, start the container
```sh
$ sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```
Communication with Splash will be done in port 8050.
We will use `scrapy-splash` for connecting the two modules above, rendering in HTML the JavaScript page.

```sh
pip install scrapy-splash
```

### Alterations made to scrapy-splash/request.py
If when running the spider, the terminal returns an error related to deprecated function `to_native_str`, substitute it for `to_unicode` in the line 42 of the `scrapy-splash/request.py` file:
```python3
url = to_unicode(url)
```
Then, go to the top of the file and import the function to the very script:

```python3
from scrapy.utils.python import to_unicode
```


## Running the spider

To run the spider via the Terminal (saving the output), run:
```sh
$ scrapy crawl quotes.py -o scraped_books.csv
```
