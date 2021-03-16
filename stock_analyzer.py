from alpha_vantage.timeseries import TimeSeries
import requests
import json
import math
import time
import random


def writeToJson(stock):
    stocks = getStockInfo(stock)
    with open('stocksFile.json', 'w') as fp:
        json.dump(stocks, fp)


def getRandomStocks(stocks,inputtedStock):
    seen = {}
    length = len(stocks)
    output = []
    for i in range(10):
        
        idx = random.randint(0,length)
        if idx in seen and stocks[idx] == inputtedStock:
            continue
        seen[idx] = True
        output.append(stocks[idx])
    return output





def getStocks():
    f = open("tickers.txt","r")
    return f.read().splitlines()


def getStockInfo(inputtedStock):

    stocks = getStocks()
    randomStocks = getRandomStocks(stocks,inputtedStock)

    stockInfo = {}
    for stock in randomStocks:
        print(stock)
        time.sleep(60)
        if getAnnualizedReturn(stock) == None:
            continue
        avgPrice,annualizedReturn,standardDeviation = getAnnualizedReturn(stock)

        stockInfo[stock] = {"avgPrice":avgPrice,"annualizedReturn": annualizedReturn,"standardDeviation":standardDeviation}
        #print(stock) 
       #print(stockInfo[stock])


    return stockInfo




def callAPI(stock):
    start = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="
    stock = stock
    end = "&apikey=UJ5ZFHNSAGEVGEY6"
    response = requests.get(start+stock+end)
    return response.json()


def getDatePrice(apiCall):
    price2_Date = {}
    for key in apiCall['Monthly Time Series']:
        price2_Date[key] = apiCall['Monthly Time Series'][key]['2. high']

    #except:
        #print("Invalid Name")
    

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
        
    if counter > 1:
        return calculateStatistics(month2Price)
    else:
        return None
    ##prices = 


def calculateStatistics(month2Price):
    prices = []
    for key in month2Price:
        prices.append(int(float(month2Price[key])))

    annualizedReturn = (prices[0] - prices[-1]) / prices[0]
    isNegative = annualizedReturn < 0 
    if isNegative:
        annualizedReturn *= -1
    annualizedReturn *= 100

    averagePrice = 0
    for price in prices:
        averagePrice += price
    averagePrice /= len(prices)

    standardDeviation = 0
    for price in prices:
        standardDeviation += (price - averagePrice) ** 2
    standardDeviation /= len(prices)
    return (averagePrice,annualizedReturn,math.sqrt(standardDeviation))























##{'2021-03-05': {'1. open': '120.3500', '2. high': '123.7500', '3. low': '118.7550', '4. close': '122.8300', '5. adjusted close': '122.8300', '6. volume': '32662092', '7. dividend amount': '0.0000'}





    ##"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=UJ5ZFHNSAGEVGEY6"



        








