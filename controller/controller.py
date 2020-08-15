import dao.repository as repository
import service.shares as shares
import service.balance as balance

import numpy as np

def getData(filename):
    return repository.convertDataFromCsvToPandas(filename)

def removeNullRows(data):
    newData = data.dropna().reset_index()

    return repository.removeColumn(newData, "index")

def getTotalGrowthRate(data, numberOfYears):
    portfolioAmount = repository.getColumn(data, 'Portfolio Amount')

    overallGrowthRate = portfolioAmount.iloc[-1] / portfolioAmount.iloc[0]

    return (overallGrowthRate ** (1 / numberOfYears))

def getAnnualStdDev(data, divideBy):
    return repository.getColumn(data, 'Std Dev').iloc[-1] * np.sqrt(divideBy)

def addTotalReturnColumn(data):
    price = repository.getColumn(data, 'Adj Close')

    totalReturn = []
    totalReturn.append(np.nan)

    for i in range(1, len(data)):
        totalReturn.append( price.iloc[i] / price.iloc[i - 1] )

    return repository.addColumn(data, 'Total Return', totalReturn)

def addPortfolioAmountColumn(data, startingBalance):
    totalReturn = repository.getColumn(data, 'Total Return')

    portfolioAmount = []
    portfolioAmount.append(startingBalance)
    
    for i in range(1, len(data)):
        portfolioAmount.append( totalReturn[i] * portfolioAmount[-1] )

    return repository.addColumn(data, 'Portfolio Amount', portfolioAmount)

def addReturnColumn(data):
    totalReturn = repository.getColumn(data, 'Total Return')

    cagr = []
    cagr.append(np.nan)

    totalProduct = 1
    for i in range(1, len(data)):
        totalProduct *= totalReturn[i]

        cagr.append( totalProduct ** (1 / i) )
    
    return repository.addColumn(data, 'Return', cagr)

def addStdDevColumn(data):
    totalReturn = repository.getColumn(data, 'Total Return')

    stdDevCol = []
    stdDevCol.append(np.nan)

    for i in range(1, len(data)):
        stdDevCol.append( np.std(totalReturn[1 : i + 1], ddof=1) )

    return repository.addColumn(data, 'Std Dev', stdDevCol)

def addMinAndMaxColumns(data):
    totalReturn = repository.getColumn(data, 'Total Return')

    minCol = []
    maxCol = []
    minCol.append(np.nan)
    maxCol.append(np.nan)

    for i in range(1, len(data)):
        minCol.append( min(totalReturn[1 : i + 1]) )
        maxCol.append( max(totalReturn[1 : i + 1]) )

    data = repository.addColumn(data, 'Min', minCol)
    
    return repository.addColumn(data, 'Max', maxCol)

def addDrawdownColumn(data):
    portfolioAmount = repository.getColumn(data, 'Portfolio Amount')

    drawdown = []
    drawdown.append(0)

    for i in range(1, len(data)):
        drawdown.append( (portfolioAmount[i] / max(portfolioAmount[0 : i + 1])) - 1 )
    
    return repository.addColumn(data, 'Drawdown', drawdown)