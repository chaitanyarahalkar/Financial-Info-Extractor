# Finance Information Extractor

This is a python script that allows one to extract financial data for any company from Religare.com. This is written compliant only to the Indian [National Stock Exchange](https://www.nseindia.com/).
This is an information scraper written with the Beautiful Soup package for Python.

### Following information is extracted for the company
  - Balance Sheet
  - Cashflow 
  - Quarterly Earnings
  - Half Earnings
  - Key-Ratio
  - Profit-Loss 
###### (In Consolidated and Standalone types) 

### Dependencies and Tools

* [Beautiful Soup](https://readthedocs.org/projects/beautiful-soup-4/) - For HTML/XML Parsing 
* [Requests](http://docs.python-requests.org/en/master/) - Python HTTP Library
* [Selenium](http://selenium-python.readthedocs.io/) - Browser automation library 
* [CSV](https://docs.python.org/2/library/csv.html) - For manipulating CSVs
* [PhantomJS](http://phantomjs.org/download.html) - Headless browser for automation

### Steps Involved
* Extraction of the URLs for each company using browser automation
  PhantomJS(Headless Browser) is used being used for the browser automation part. (Any other browser can also be used)
* Scraping the data from each URL and storing in CSVs.

Install the dependencies and run the scripts.

```sh
$ python url-extractor.py
$ python extract.py
```
License
----
MIT
