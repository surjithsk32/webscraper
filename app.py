from flask import Flask
from lxml import html
import requests
import sys
app = Flask(__name__)

@app.route('/')
def indexes():
    return "Hello this is scraper"

@app.route('/<ndc>', methods=['GET'])
def index(ndc):
    try:        
        ndcis =  ndc
        print(ndcis)
        page = requests.get('https://connect.medlineplus.gov/demo/service?knowledgeResponseType=text%2Fxml&mainSearchCriteria.v.cs=2.16.840.1.113883.6.69&mainSearchCriteria.v.c=+'+ndcis+'&mainSearchCriteria.v.dn=&informationRecipient.languageCode.c=en')
        print("page")
        tree = html.fromstring(page.content)
        print("tree")
#This will create a list of buyers:
        if tree.xpath('//div[@class="entry"]/text()'):
            print("if")
            content = tree.xpath('//div[@class="entry"]/text()')
            print("content")
        else:
            content = ""
        print(content)
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
        if(len(content)>3):
            return content[4]
        else:
            return "No response"
    except:
        return str(sys.exc_info()[0])

#print(prices)


if __name__ == '__main__': 
   app.run(debug=False,host="0.0.0.0") # application will start listening for web request on port 5000
