from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "" # Path to the driver's executable 

driver = webdriver.PhantomJS(PATH)

search_id = "Menu_ctrlAutoCompleteExtender1_TxtAutoComplete"


xpath = "/html/body/ul/li[1]/a/div" 

URL = "http://www.religareonline.com/"


with open('ind_nifty500list.csv','r') as f:
	data = f.read()

companies = data.split("\n")
urls = []

with open("company_urls.txt",'a') as f:
	for company in companies:
		try:
			driver.get(URL)
			driver.find_element_by_id(search_id).clear()
			input_s = driver.find_element_by_id(search_id)
			input_s.send_keys(company)
			time.sleep(1)
			driver.find_element_by_xpath(xpath).click()
			f.write(driver.current_url + "\n")
			print("done")
		except:
			continue 
		




