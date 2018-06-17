# Finance Information Extractor

This is a python script that allows one to extract financial data for any company from [Religare](http://religare.com)(India's leading diversified financial services group). This is written compliant only to the Indian [National Stock Exchange](https://www.nseindia.com/) since no official API provides this information for the Indian stock market. This script downloads the financial data for the top 500 NSE companies.
This is an information scraper written with the Beautiful Soup package for Python.

### Following information is extracted for the company
  - Balance Sheet
  - Cashflow 
  - Quarterly Earnings
  - Half Earnings
  - Key-Ratio
  - Profit-Loss 
###### (In Consolidated and Standalone type)
###### (All the data is scraped and stored in .csv format)

### Dependencies and Tools

* [Beautiful Soup](https://readthedocs.org/projects/beautiful-soup-4/) - For HTML/XML Parsing 
* [Requests](http://docs.python-requests.org/en/master/) - Python HTTP Library
* [Selenium](http://selenium-python.readthedocs.io/) - Browser automation library 
* [CSV](https://docs.python.org/2/library/csv.html) - For manipulating CSVs
* [PhantomJS](http://phantomjs.org/download.html) - Headless browser for automation

### Steps Involved
* Extraction of the URLs for each company using browser automation.
  PhantomJS(Headless Browser) is being used for the browser automation part. (Any other browser can also be used)
* Scraping the data from each URL and storing in CSVs.

Install the dependencies and run the scripts.

Install Beautiful Soup 4,Selenium and Requests using pip.
```sh
$ pip install bs4
$ pip install requests
$ pip install selenium
```

### Else download manually here:

* [Requests](https://pypi.python.org/pypi/requests/)
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)
* [Selenium](https://pypi.org/project/selenium/)

### Run the scripts:  

Add the path to the Browser Driver in the in the url-extractor script.

```sh 
$ python url-extractor.py
$ python extract.py
```
### License

The MIT License (MIT)

Copyright (c) 2018 Chaitanya Rahalkar
