import dao.repository as repository
import service.shares as shares
import service.balance as balance

import numpy as np

def getData(filename):
    return repository.convertDataFromCsvToPandas(filename)

def removeNullRows(data):
    newData = data.dropna().reset_index()

    return repository.removeColumn(newData, "index")

def addDailyTotalReturnColumn(data):
    price = repository.getColumn(data, 'Adj Close')

    dailyTotalReturn = []
    dailyTotalReturn.append(np.nan)

    for i in range(1, len(data)):
        dailyTotalReturn.append( price.iloc[i] / price.iloc[i - 1] )

    return repository.addColumn(data, 'Daily Total Return', dailyTotalReturn)

def addPortfolioAmountColumn(data, startingBalance):
    dailyTotalReturn = repository.getColumn(data, 'Daily Total Return')

    portfolioAmount = []
    portfolioAmount.append(startingBalance)
    
    for i in range(1, len(data)):
        portfolioAmount.append( dailyTotalReturn[i] * portfolioAmount[-1] )

    return repository.addColumn(data, 'Portfolio Amount', portfolioAmount)

def plotAnnualReturnsAndPortfolioGrowth():
    pass
