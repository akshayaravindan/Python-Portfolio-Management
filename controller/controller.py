import dao.repository as repository
import service.shares as shares
import service.balance as balance

def getPortfolioReturns(filename, startingBalance, aggregationPeriod, startDate, endDate):
    data = getData(filename)

    numberOfShares = getNumberOfShares(data, startingBalance)

    finalBalance = getFinalBalance(data, numberOfShares)

    return startingBalance, finalBalance

def getPortfolioGrowthDataFrame(filename, startingBalance, startDate, endDate):
    data = getData(filename)

    numberOfShares = getNumberOfShares(data, startingBalance)

    price = repository.getColumn(data, 'Adj Close')

    portfolioGrowth = []
    portfolioGrowth.append(startingBalance)
    for i in range(1, len(data)):
        previousPrice = price.iloc[i - 1]
        currentPrice = price.iloc[i]

        growth = ( numberOfShares * (currentPrice - previousPrice) ) + portfolioGrowth[-1]

        portfolioGrowth.append(growth)
    
    repository.addColumn(data, 'Portfolio Growth', portfolioGrowth)

    return data

def plotAnnualReturnsAndPortfolioGrowth():
    pass

def getData(filename):
    return repository.convertDataFromCsvToPandas(filename)

def getNumberOfShares(data, startingBalance):
    startingPriceOfSecurity = repository.getColumn(data, 'Adj Close').iloc[0]
    return shares.calculateSharesFromBalance(startingPriceOfSecurity, startingBalance)

def getFinalBalance(data, numberOfShares):
    startingPriceOfSecurity = repository.getColumn(data, 'Adj Close').iloc[0]
    finalPriceOfSecurity = repository.getColumn(data, 'Adj Close').iloc[-1]

    return balance.calculateFinalBalance(startingPriceOfSecurity, finalPriceOfSecurity, numberOfShares)
