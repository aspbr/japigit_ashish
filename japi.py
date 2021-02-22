import urllib.request
import requests
import json

def getStockData(symbol):
    nasdaqAppleURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ symbol +'&apikey=5I8WBMVNZE0UP84T'
    connection = urllib.request.urlopen(nasdaqAppleURL)
    responseString = connection.read().decode()
    pyObj = json.loads(responseString)
    returnObject = {
        'symbol': symbol,
        'price': pyObj['Global Quote']['05. price']
    }

    return returnObject

def main():
    
    while True:
        symbol = input('Enter Symbol: ')
        if symbol != 'quit':
            details = getStockData(symbol)
            print('The current price of ' + details['symbol'] +' is: $' + details['price'] +'')
        else:
            print('Stock Quotes retrieved successfully!')
            break

if __name__ == "__main__":
    main()


