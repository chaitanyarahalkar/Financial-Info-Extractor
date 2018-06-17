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
  PhantomJS(Headless Browser) is used being used for the browser automation part. (Any other browser can also be used)
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

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
