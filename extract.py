from bs4 import BeautifulSoup
import requests
import os 
import csv

file_headers_1 = ['key-ratio','balance-sheet','profit-loss','cashflow','quarterly','half']
file_headers_2 = ['consolidated','standalone']

filenames = []

for i in file_headers_1:
	for j in file_headers_2:
		filenames.append(i + "(" +j + ")" + ".csv")

FILE = "" #Path of the text file containing the extracted URLs

with open(FILE,'r') as f:
	data = f.read()
	urls = data.split("\n")

for url in urls:
	temp = url.split("/")
	company = temp[4]
	temp.insert(5,"ratio")
	url = "/".join(temp)
	if not os.path.exists(company):
		os.makedirs(company)
	os.chdir(company)

	resp = requests.get(url)
	soup = BeautifulSoup(resp.content,'html5lib')
	tables = soup.findAll("table")
	sub_counter = 0
	counter = 0
	for table in tables:
		if counter % 2 == 0:
			if sub_counter == 12:
				break
			headers = [th.text for th in table.select("tr th")]
			with open(filenames[sub_counter], "w") as f:
				wr = csv.writer(f)
				wr.writerow(headers)
				wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])
			sub_counter+=1
		counter+=1
	print("Done")
	os.chdir("..")







