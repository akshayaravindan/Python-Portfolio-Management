import controller.controller as controller
import dao.repository as repository
import plotter.line as linePlot
import plotter.bar as barPlot
import matplotlib.pyplot as plt

import copy

if __name__ == '__main__':
    filename = "dao/AAPL.csv"
    startingBalance = 10000
    aggregationPeriod = "Monthly"
    startDate = "1/2/2020"
    endDate = "6/30/2020"

    rawData = controller.getData(filename)
    data = controller.removeNullRows(rawData)
    dailyDataframe = copy.deepcopy(data)
    monthlyDataframe = copy.deepcopy(data)
    yearlyDataframe = copy.deepcopy(data)

    print("===== Getting Daily Data =====")
    print()
    dailyData = repository.splitDataByDates(dailyDataframe, startDate, endDate)
    dailyData = repository.splitDataByAggregationPeriod(dailyData, "Daily")
    numberOfDays = len(dailyData)

    print("===== Getting Montly Data =====")
    print()
    monthlyData = repository.splitDataByDates(monthlyDataframe, startDate, endDate)
    monthlyData = repository.splitDataByAggregationPeriod(monthlyData, "Monthly")
    numberOfMonths = len(monthlyData)

    print("===== Getting Annual Data =====")
    print()
    yearlyData = repository.splitDataByDates(yearlyDataframe, startDate, endDate)
    yearlyData = repository.splitDataByAggregationPeriod(yearlyData, "Annual")
    numberOfYears = len(dailyData) / 252

    print("===== Adding Total Return Column =====")
    print()
    dailyData = controller.addTotalReturnColumn(dailyData)
    monthlyData = controller.addTotalReturnColumn(monthlyData)
    yearlyData = controller.addTotalReturnColumn(yearlyData)

    print("===== Adding Portfolio Amount Column =====")
    print()
    dailyData = controller.addPortfolioAmountColumn(dailyData, startingBalance)
    monthlyData = controller.addPortfolioAmountColumn(monthlyData, startingBalance)
    yearlyData = controller.addPortfolioAmountColumn(yearlyData, startingBalance)

    print("===== Adding Return Column =====")
    print()
    dailyData = controller.addReturnColumn(dailyData)
    monthlyData = controller.addReturnColumn(monthlyData)
    yearlyData = controller.addReturnColumn(yearlyData)

    print("===== Adding Std Dev Column =====")
    print()
    dailyData = controller.addStdDevColumn(dailyData)
    monthlyData = controller.addStdDevColumn(monthlyData)
    yearlyData = controller.addStdDevColumn(yearlyData)

    print("===== Adding Min and Max Column =====")
    print()
    dailyData = controller.addMinAndMaxColumns(dailyData)
    monthlyData = controller.addMinAndMaxColumns(monthlyData)
    yearlyData = controller.addMinAndMaxColumns(yearlyData)

    print("===== Adding Drawdown Column =====")
    print()
    dailyData = controller.addDrawdownColumn(dailyData)
    monthlyData = controller.addDrawdownColumn(monthlyData)
    yearlyData = controller.addDrawdownColumn(yearlyData)
    
    print( "Max Drawdown (Daily): " + str( min(repository.getColumn(dailyData, 'Drawdown')) ) )
    print( "Max Drawdown (Montly): " + str( min(repository.getColumn(monthlyData, 'Drawdown')) ) )
    print()

    print( "CAGR (Daily): " + str( controller.getTotalGrowthRate(dailyData, numberOfYears) - 1) )
    print( "CAGR (Monthly): " + str( controller.getTotalGrowthRate(monthlyData, numberOfYears) - 1) )
    print()

    print( "Std Dev (Daily): " + str( controller.getAnnualStdDev(dailyData, divideBy=250) ) )
    print( "Std Dev (Monthly): " + str( controller.getAnnualStdDev(monthlyData, divideBy=12) ) )
    print()

    print( "Number of Years: " + str( numberOfYears ) )

    # fig, axs = plt.subplots(2)
    # linePlot.plotter(data['Date'], data['Portfolio Amount'], axs[0])
    # barPlot.plotter([1, 2, 3], [1, 2, 3], axs[1])

    # plt.show()