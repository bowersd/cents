from lxml import html
import requests
import argparse


def get_attribute(symbol, attribute):
    #departed from usual ban against one-time use variables, function-internal data shunting for readability
    content = requests.get('https://finance.yahoo.com/quote/{}?p={}'.format(symbol, symbol))
    parser = html.fromstring(content.text)
    summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
    return summary_table[attribute].xpath('.//td[contains(@class,"Ta(end)")]//text()')[0]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('symbols', nargs='+',  help="symbols to retrieve")
    parser.add_argument('-pc', '--previous-close',  action='append_const', dest='options', const = "Previous Close", help="the previous close price")
    parser.add_argument('-ytd', '--ytd-return',  action='append_const', dest='options', const = "Year to Date Return", help="the return calculated over the calendar year")
    parser.add_argument('-er', '--expense-ratio',  action='append_const', dest='options', const = "Expense Ratio", help="net expense ratio")
    parser.add_argument('-c', '--category',  action='append_const', dest='options', const = "Category", help="fund type")
    parser.add_argument('-lcg', '--last-cap-gain',  action='append_const', dest='options', const = "Last Capital Gain", help="last capital gain")
    parser.add_argument('-mr', '--morningstar-rating',  action='append_const', dest='options', const = "Morningstar Rating", help="morningstar rating")
    parser.add_argument('-mrr', '--morningstar-risk-rating',  action='append_const', dest='options', const = "Morningstar Risk Rating", help="morningstar risk rating")
    parser.add_argument('-sr', '--sustainability-rating',  action='append_const', dest='options', const = "Sustainability Rating", help="sustainability rating")
    parser.add_argument('-na', '--net-assets',  action='append_const', dest='options', const = "Net Assets", help="net assets")
    parser.add_argument('-b', '--beta',  action='append_const', dest='options', const = "Beta", help="beta (3Y monthly)")
    parser.add_argument('-y', '--yield',  action='append_const', dest='options', const = "Yield", help="yield")
    parser.add_argument('-ar', '--5-year-average-return',  action='append_const', dest='options', const = "5 Year Average Return", help="five year average return")
    parser.add_argument('-ht', '--holdings-turnover',  action='append_const', dest='options', const = "Holdings Turnover", help="holdings turnover")
    parser.add_argument('-ld', '--last-dividend',  action='append_const', dest='options', const = "Last Dividend", help="last dividend")
    parser.add_argument('-ac', '--average-for-category',  action='append_const', dest='options', const = "Average for Category", help="average for category")
    parser.add_argument('-id', '--inception-date',  action='append_const', dest='options', const = "Inception Date", help="inception date")
    parser.add_argument('-o', '--open',  action='append_const', dest='options', const = "Open", help="open price")
    parser.add_argument('-bp', '--bid-price',  action='append_const', dest='options', const = "Bid", help="bid price")
    parser.add_argument('-a', '--ask-price',  action='append_const', dest='options', const = "Ask", help="ask price")
    parser.add_argument('-dr', '--days-range',  action='append_const', dest='options', const = "Day's Range", help="day's range")
    parser.add_argument('-wr', '--52-week-range',  action='append_const', dest='options', const = "52 Week Range", help="52 week range ")
    parser.add_argument('-v', '--volume',  action='append_const', dest='options', const = "Volume", help="Volume")
    parser.add_argument('-av', '--average-volume',  action='append_const', dest='options', const = "Average Volume", help="Average Volume")
    parser.add_argument('-mc', '--market-cap',  action='append_const', dest='options', const = "Market Cap", help="market cap")
    parser.add_argument('-per', '--pe-ratio',  action='append_const', dest='options', const = "PE Ratio", help="PE ratio")
    parser.add_argument('-eps', '--eps',  action='append_const', dest='options', const = "EPS", help="EPS")
    parser.add_argument('-ed', '--earnings-date',  action='append_const', dest='options', const = "Earnings Date", help="earnings date")
    parser.add_argument('-fdy', '--forward-dividend-yield',  action='append_const', dest='options', const = "Forward Dividend and Yield", help="forward dividend and yield")
    parser.add_argument('-edd', '--ex-dividend-date',  action='append_const', dest='options', const = "Ex-Dividend Date", help="ex-dividend date")
    parser.add_argument('-te', '--1-year-target-estimate',  action='append_const', dest='options', const = "1 Year Target Estimate", help="1y target est")
    return parser.parse_args()

names_to_pos = {
        "Previous Close": 0,
        "Year to Date Return": 1,
        "Expense Ratio": 2,
        "Category": 3,
        "Last Capital Gain": 4,
        "Morningstar Rating": 5,
        "Morningstar Risk Rating": 6,
        "Sustainability Rating": 7,
        "Net Assets": 8,
        "Beta": 9,
        "Yield": 10,
        "5 Year Average Return": 11,
        "Holdings Turnover": 12,
        "Last Dividend": 13,
        "Average for Category": 14,
        "Inception Date": 15,
        #Stocks
        "Open":1,
        "Bid":2,
        "Ask":3,
        "Day's Range":4,
        "52 Week Range":5,
        "Volume":6,
        "Average Volume":7,
        "Market Cap":8,
        "PE Ratio":10,
        "EPS":11,
        "Earnings Date":12,
        "Forward Dividend and Yield":13,
        "Ex-Dividend Date":14,
        "1 Year Target Estimate":15,
        }

if __name__ == "__main__":
    args = get_args()
    if not args.options: 
        print("Previous Close")
        for x in args.symbols: print(x.upper(),"    "+get_attribute(x, names_to_pos["Previous Close"]))
    else:
        for y in sorted(args.options): 
            print(y)
            for x in args.symbols: print(x.upper(),"    "+get_attribute(x, names_to_pos[y]))
