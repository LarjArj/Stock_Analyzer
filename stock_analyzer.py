from alpha_vantage.timeseries import TimeSeries
import requests
import json
import math

def writeToJson():
    stocks = getStockInfo()
    with open('stocks.json', 'w') as fp:
        json.dump(stocks, fp)



def getStocks():
    f = open("tickers.txt","r")
    return f.read().splitlines()


def getStockInfo():

    stocks = getStocks()

    stockInfo = {}
    for stock in stocks:
        try:

            if getAnnualizedReturn(stock) == None:
                continue
            avgPrice,annualizedReturn,standardDeviation = getAnnualizedReturn(stock)
        except:
            print("error")

        
        stockInfo[stock] = {"avgPrice":avgPrice,"annualizedReturn": annualizedReturn,"standardDeviation":standardDeviation}
        print(stock) 
        print(stockInfo[stock])


    return stockInfo




def callAPI(stock):
    start = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="
    stock = stock
    end = "&apikey=UJ5ZFHNSAGEVGEY6"
    response = requests.get(start+stock+end)
    return response.json()


def getDatePrice(apiCall):
    price2_Date = {}
    try:
        for key in apiCall['Monthly Time Series']:
            price2_Date[key] = apiCall['Monthly Time Series'][key]['2. high']

    except:
        print("Invalid Name")
    

    return price2_Date


def getAnnualizedReturn(stock):
    stockFromAPI = callAPI(stock)
    stockTable = getDatePrice(stockFromAPI)

    counter = 1
    month2Price = {}
    for key in stockTable:
        if counter > 13:
            break
        month2Price[key] = stockTable[key]
        counter += 1
    prices = []

    for key in month2Price:
        prices.append(int(float(month2Price[key])))
    if len(prices):
        annualizedReturn  = (prices[0] - prices[-1]) / prices[0]
        isNegative = annualizedReturn < 0
        if isNegative:
            annualizedReturn *= -1 

        annualizedReturn *=  100

        averagePrice = 0 
        for price in prices:
            averagePrice += price
        averagePrice /= len(prices)

        standardDeviation = 0
        for price in prices:
            standardDeviation += (price - averagePrice) ** 2

        standardDeviation /= len(prices)

        return (averagePrice,annualizedReturn,math.sqrt(standardDeviation))
    else:
        return None





















##{'2021-03-05': {'1. open': '120.3500', '2. high': '123.7500', '3. low': '118.7550', '4. close': '122.8300', '5. adjusted close': '122.8300', '6. volume': '32662092', '7. dividend amount': '0.0000'}





    ##"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=UJ5ZFHNSAGEVGEY6"



        








