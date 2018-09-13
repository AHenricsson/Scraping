from lxml import html
import requests
from pprint import pprint
import unicodecsv as csv
from traceback import format_exc
import argparse
#import certifi
import urllib3
import datetime
import os

#http = urllib3.PoolManager(
#cert_reqs='CERTR_REQUIRED', 
#ca_certs=certifi.where())

urllib3.disable_warnings()

def save_html(html_txt, filename):
    #Saves HTML to autamatically generated filename.
    file = open(filename,  "w+")
    file.write(html_txt)
    file.close()
    
def make_filename(brand):
    now = datetime.datetime.now()
    directory = "./{0}_SavedHTML".format(brand)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "{0}/{1}.html".format(directory,  now.isoformat())
    return filename
    
def file_search(file_str,  search_str):
    file = open(file_str,  "r")
    lines = []
    for line in file:
        #print("Searching line: {0}".format(line))
        if search_str in line:
            print("found line: {0}".format(line)) #Testing
            lines.append(line)
        else: print("found nothing in this line")
    return lines
            
def parse(brand):
	for i in range(5):
##		try:
			url = 'http://www.ebay.com/sch/i.html?_nkw={0}&_sacat=0'.format(brand)
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
			print ("Retrieving %s"%(url))
			response = requests.get(url, headers=headers, verify=False)
			print ("Parsing page")
			text = response.text
			filename = make_filename(brand)
			save_html(text,  filename)
#          print ("response: {0}".for<mat(response.text))
			print("search results:{0}".format(file_search(filename, 's-item__price')))
#            
#          <div class="s-item__detail s-item__detail--primary"><span class="s-item__price">177.24 SEK</span></div>
#          <li id="srp-river-results-listing1" class="s-item" data-view="mi:1686|iid:1>
#
#			raw_result_count = parser.xpath("//span[@class='rcnt']//text()")
#			result_count = ''.join(raw_result_count).strip()
#			print ("Found {0} results for {1}".format(result_count,brand))
#
#			scraped_products = []
#
#			for product in product_listings:
#				raw_url = #?
#				raw_title = #?
#				raw_price = #?
#				price  = #?
#				title = #?
#				data = {
#							'url':raw_url[0],
#							'title':title,
#							'price':price
#				}
#				scraped_products.append(data)
#			return scraped_products
##		except Exception as e:
##			print (format_exc(e))
#
#if __name__=="__main__":
#	
#	argparser = argparse.ArgumentParser()
#	argparser.add_argument('brand',help = 'Brand Name')
#	args = argparser.parse_args()
#	brand = args.brand
#
#	scraped_data =  parse(brand)
#	print ("Writing scraped data to %s-ebay-scraped-data.csv"%(brand))
#	
#	with open('%s-ebay-scraped-data.csv'%(brand),'wb') as csvfile:
#		fieldnames = ["title","price","url"]
#		writer = csv.DictWriter(csvfile,fieldnames = fieldnames,quoting=csv.QUOTE_ALL)
#		writer.writeheader()
#		for data in scraped_data:
#			writer.writerow(data)
parse("IBM")
