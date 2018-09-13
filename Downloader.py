########################################################
# Downloads Search pages from Ebay
# Doesn't save images!!!
# Doesn't save individul pages!!!
#
########################################################

import requests
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
    
def make_filename(brand, page, time):
    directory = "./{0}_SavedHTML/{1}".format(brand, time)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = "{0}/page_{1}.html".format(directory, page)
    return filename
    
def parse(brand):
    now = datetime.datetime.now()
    time = now.isoformat()
    for i in range(5):
    ##		try:
            url = 'http://www.ebay.com/sch/i.html?_nkw={0}&_sacat=0'.format(brand)
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
            print ("Retrieving %s"%(url))
            response = requests.get(url, headers=headers, verify=False)
            print ("Parsing page")
            text = response.text
            filename = make_filename(brand,  i, time)
            save_html(text,  filename)
            
parse("IMB Model M")
