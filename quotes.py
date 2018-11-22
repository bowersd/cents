from lxml import html
import requests
import sys

#todo: retrieve different attributes of a stock symbol, using argparse

def last_close(symbol):
    #departed from usual ban against one-time use variables, function-internal data shunting for readability
    content = requests.get('https://finance.yahoo.com/quote/{}?p={}'.format(symbol, symbol))
    parser = html.fromstring(content.text)
    summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
    return float(summary_table[0].xpath('.//td[contains(@class,"Ta(end)")]//text()')[0])

if __name__ == "__main__":
    for x in sys.argv[1:]:
        print x, "{:9.2f}".format(last_close(x))
