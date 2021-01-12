from flask import Flask
from lxml import html
import requests

app = Flask(__name__)

@app.route('/<ndc>')
def index(ndc):
    ndcis =  ndc
    page = requests.get('https://connect.medlineplus.gov/demo/service?knowledgeResponseType=text%2Fxml&mainSearchCriteria.v.cs=2.16.840.1.113883.6.69&mainSearchCriteria.v.c=+'+ndcis+'&mainSearchCriteria.v.dn=&informationRecipient.languageCode.c=en')
    tree = html.fromstring(page.content)

#This will create a list of buyers:
    content = tree.xpath('//div[@class="entry"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
    if(len(content)>3):
        return content[4]
    else:
        return "No response"

#print(prices)


if __name__ == '__main__': 
   app.run(threaded = True,port=5000, debug=True) # application will start listening for web request on port 5000